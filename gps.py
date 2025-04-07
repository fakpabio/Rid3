from queue import Queue
import time

def getGPS(q: Queue):
    while True:
        time.sleep(1)
        lat,lon = time.time(), time.time()+1
        q.put((item := (lat, lon)))
        print(f"sending lat,lon")