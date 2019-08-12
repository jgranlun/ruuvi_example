'''
Print sensor data to the screen. Update interval 2 sec.
Press Ctrl+C to quit.

2019-08-12 12:08:29.006557
Sensor: FD:E7:CD:02:C4:2B
Temperature: 25.95 C
Humidity:    48.5
Pressure:    1006.48
'''

import time
import os
from datetime import datetime
from ruuvitag_sensor.ruuvitag import RuuviTag

# Change here the MAC addresses of your RuuviTags:
mac_addresses = ['FD:E7:CD:02:C4:2B', 'FB:5C:DA:24:9C:99']

sensor1 = RuuviTag(mac_addresses[0])
sensor2 = RuuviTag(mac_addresses[1]) 

while True:
    #os.system('clear')

    #read the data from the sensors
    sensor_datas = [sensor1.update(), sensor2.update()]
 
    #print the data to screen
    os.system('clear')
    for index, sensor_data in enumerate(sensor_datas):
        line_sen = str.format('Sensor: {0}', mac_addresses[index])
        line_tem = str.format('Temperature: {0} C', sensor_data['temperature'])
        line_hum = str.format('Humidity:    {0}', sensor_data['humidity'])
        line_pre = str.format('Pressure:    {0}', sensor_data['pressure'])

        print(str(datetime.now()))
        print(line_sen)
        print(line_tem)
        print(line_hum)
        print(line_pre)
        print('\n')

    # Wait for 2 seconds and start over again
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        # When Ctrl+C is pressed execution of the while loop is stopped
        print('Exit')
        break

