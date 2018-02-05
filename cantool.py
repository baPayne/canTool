"""Connect to CANable; print and echo any received frames"""
from canard import can
from canard.hw import cantact
import sys

dev = cantact.CantactDev("/dev/ttyACM0") # Connect to CANable that enumerated as ttyACM0
dev.set_bitrate(250000) # Set the bitrate to a 1Mbaud
dev.start() # Go on the bus
count = 0

while True:
    count += 1
    frame = dev.recv() # Receive a CAN frame
    dev.send(frame) # Echo the CAN frame back out on the bus
    print(str(count) + ": " + str(frame)) # Print out the received frame
    
    #monitor keyboard to stop execution
   
   # cmd = raw_input()
    #if cmd > 0:
    	#print(cmd)
    	
    #if cmd == 's':
    	#dev.stop()
    	#sys.exit()
    	#print("Program closed")
    	
    	
    	
    

	





