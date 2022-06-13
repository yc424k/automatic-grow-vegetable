import smbus
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
bus = smbus.SMBus(1)

def setup(Addr):
   global address
   address = Addr

def read(): 
   try:
      bus.write_byte(address, 0x40)
   except Eception as e:
      print("Address: %s" %address)
      print(e)
   return bus.read_byte(address)

if __name__ == "__main__":
   setup(0x48)
   while True:
      print("AIN0= ",read())
      print(" ")
      print(type(read()))
      if read() > 50:
         GPIO.output(4,True)
      else:
         GPIO.output(4,False)
      time.sleep(1.0)