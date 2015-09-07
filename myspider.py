from lxml import html
import requests
from queue import Queue
from threading import Thread

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///scraping.db'
db = SQLAlchemy(app)


class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Float)

    def __init__(self, id, active):
        self.id = id
        self.active = active

    def __repr__(self):
        return '<Id: {0}, Active: {1}>'.format(self.id, self.active)


URL = 'https://bitlendingclub.com/user/index/id/'
SUFFIX = ''
XPATH = '//*[@id="tabs"]/div[1]/table/tbody/tr[5]/td[2]/div[4]/text()'
BEGIN = 1
END = 18000


def loaned_amount(id):
    page = requests.get("http://bitlendingclub.com/user/index/id/"+str(id))
    tree = html.fromstring(page.text)
    XPATH = '//span[@class="profile-summary-label"]//following-sibling::text()'
    return float(tree.xpath(XPATH)[3].split(" ")[1])


def face(id):
    page = requests.get(URL + str(id) + SUFFIX)
    tree = html.fromstring(page.text)
    face_id = tree.xpath(XPATH)
    return face_id[0].get('href') if face_id else 'Empty'


def worker():
    while True:
        item = q.get()
        try:
            la = loaned_amount(item)
            if la>-1:
                # Database insertion here
                borrower = Borrower(id=item, active=la)
                db.session.add(borrower)
                db.session.commit()
                print(item, loaned_amount(item))
        except:
            pass

        q.task_done()

q = Queue()
num_worker_threads = 2
for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for item in range(BEGIN, END):
    q.put(item)

q.join()
