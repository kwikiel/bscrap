# Refactoring
from myspider import loaned_amount
from myspider import Borrower, db
from queue import Queue
from threading import Thread

# Magic numbers below
num_worker_threads = 8
BEGIN = 1
END = 15


def worker():
    while True:
        item = q.get()
        try:
            la = loaned_amount(item)
            if la > -1:
                # Database insertion here
                borrower = Borrower(id=item, active=la)
                db.session.add(borrower)
                db.session.commit()
                print(item, loaned_amount(item))
        except:
            pass

        q.task_done()
q = Queue()
for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for item in range(BEGIN, END):
    q.put(item)

q.join()
