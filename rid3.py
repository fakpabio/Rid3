from threading import Thread
from queue import Queue
from Rid3.navigation import navigation
from Rid3.gps import getGPS
from object_detection import getSensorData

def main():
    q = Queue()  # Define the shared queue here
    q2 = Queue()

    t1 = Thread(target=navigation, args=(q,), daemon=True)
    t2 = Thread(target=getGPS, args=(q,), daemon=True)
    t3 = Thread(target=getSensorData, args=(q2,), daemon=True)

    t1.start()
    t2.start()
    t3.start()

    import time
    time.sleep(5)
    print("Main program exiting...")

if __name__ == "__main__":
    main()
