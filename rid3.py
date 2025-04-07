from threading import Thread
from queue import Queue
from Rid3.navigation import navigation
from Rid3.gps import getGPS
from object_detection import getSensorData
import time

def main():
    q = Queue()  # Define the shared queue here
    q2 = Queue()

    t1 = Thread(target=navigation, args=(q,), daemon=True)
    t2 = Thread(target=getGPS, args=(q,), daemon=True)
    t3 = Thread(target=getSensorData, args=(q2,), daemon=True)

    t1.start()
    t2.start()
    t3.start()

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Exiting program...")

if __name__ == "__main__":
    main()