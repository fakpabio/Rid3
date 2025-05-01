from threading import Thread
from queue import Queue
from navigation import navigation
from gps import getGPS
from detection import getSensorData
import time

def main():
    gpsLo = [None,None]
    
    t2 = Thread(target=getGPS, args=(gpsLo,), daemon=True)
    t3 = Thread(target=getSensorData, args=(), daemon=True)
    t1 = Thread(target=navigation, args=(gpsLo,), daemon=True)

    t2.start()
    t3.start()
    time.sleep(1)
    t1.start()

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Exiting program...")

if __name__ == "__main__":
    main()
