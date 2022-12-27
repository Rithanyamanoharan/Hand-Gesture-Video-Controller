import serial #Serial imported for Serial communication

import time #Required to use delay functions

import pyautogui

 
ArduinoSerial = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData

time.sleep(2) #wait for 2 seconds for the communication to get established




while 1:

    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line

    print (incoming)



    
    if 'Rewind' in incoming:

        pyautogui.hotkey('ctrl', 'left')  



    if 'Forward' in incoming:

          pyautogui.hotkey('ctrl', 'right') 


 
    #if 'Volume Increased' in incoming:

        #pyautogui.hotkey('ctrl', 'up')

        


    #if 'Volume Decreased' in incoming:

        #pyautogui.hotkey('ctrl', 'down')

    #if 'play/pause' in incoming:
 
        #pyautogui.hotkey('ctrl', 'p')
        

    
        

    incoming = "";

    

 

