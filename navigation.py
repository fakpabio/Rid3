from queue import Queue

def navigation(q: Queue):
    while True:
        lat,lon = q.get()
        print(f"lat {lat}, lon {lon}")
        q.task_done()
