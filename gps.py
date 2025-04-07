from queue import Queue
import time
import serial


ser = serial.Serial(
    port='/dev/ttyAMA2',  # Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def parse_gga(gga_data):
    """Parses a $GPGGA sentence to extract latitude and longitude."""
    parts = gga_data.split(',')
    if len(parts) >= 6 and parts[0] == '$GPGGA' and parts[2] and parts[3] and parts[4] and parts[5]:
        latitude_str = parts[2]
        lat_direction = parts[3]
        longitude_str = parts[4]
        lon_direction = parts[5]

        # Convert latitude from degrees and minutes to decimal degrees
        lat_degrees = int(latitude_str[:2])
        lat_minutes = float(latitude_str[2:])
        latitude = lat_degrees + (lat_minutes / 60.0)
        if lat_direction == 'S':
            latitude *= -1

        # Convert longitude from degrees and minutes to decimal degrees
        lon_degrees = int(longitude_str[:3])
        lon_minutes = float(longitude_str[3:])
        longitude = lon_degrees + (lon_minutes / 60.0)
        if lon_direction == 'W':
            longitude *= -1

        return latitude, longitude
    else:
        return None, None

def getGPS(q: Queue):
    while True:
        try:
            x = ser.readline().decode('utf-8').strip()  # Read line, decode, and remove extra whitespace
            if x.startswith('$GPGGA'):
                latitude, longitude = parse_gga(x)
                if latitude is not None and longitude is not None:
                   q.put((latitude, longitude))
                   print(f"GPS data sent to queue: Latitude: {latitude:.6f}, Longitude: {longitude:.6f}")
                else:
                    print("Invalid $GPGGA data")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break
        except UnicodeDecodeError as e:
            print(f"Decode error: {e}, Received raw data: {x}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

