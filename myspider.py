from lxml import html
import requests
from queue import Queue
from threading import Thread


URL = 'https://bitlendingclub.com/user/index/id/'
SUFFIX = ''
XPATH = '//*[@id="tabs"]/div[1]/table/tbody/tr[5]/td[2]/div[4]/text()'
BEGIN = 17000
END = 18000


def loaned_amount(id):
    page = requests.get("http://bitlendingclub.com/user/index/id/"+str(id))
    tree = html.fromstring(page.text)
    return float(tree.xpath('//span[@class="profile-summary-label"]//following-sibling::text()')[3].split(" ")[1])



def face(id):
    page = requests.get(URL + str(id)+ SUFFIX)
    tree = html.fromstring(page.text)
    face_id = tree.xpath(XPATH)
    return face_id[0].get('href') if face_id else 'Empty'


def worker():
    while True:
        item = q.get()
        try:
            if loaned_amount(item)>0:
                print(item,loaned_amount(item))
        except:
            pass

        # Database insertion here
        q.task_done()

q = Queue()
num_worker_threads = 42
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in range(BEGIN,END):
    q.put(item)

q.join()

worker()
