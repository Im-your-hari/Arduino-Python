q='''############################################
     #           Arduino-Meets-Python           #
     # Code by: Harikrishnan KB , Kerala ,India #
     #     Think Different Make it Awesome      #
     ############################################
'''

import serial
import time 
 
ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2) 

print(q)
print(ArduinoSerial.readline())
print("MENU ::\n1 -> TURN ON\n0 -> TURN OFF")

 
while True: 
    var = input("Enter 1 or 2 : ")
    print("you entered", var)
    if(var == '1'): 
        ArduinoSerial.write(b'1') #send 1->b'1' used to encode the sending data
        print("LED turned ON")
        time.sleep(1)
    
    if(var == '0'):
        ArduinoSerial.write(b'0') #send 0->b'0' used to encode the sending data
        print("LED turned OFF")
        time.sleep(1)
