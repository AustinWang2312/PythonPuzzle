#count=50
#while count >= 0:
#	print("#")
import time
import sys
import os 
#os.system('clear') 
#done = 'false'
#here is the animation
#def animate():
#    while done == 'false':
#        print('
import random
#animate()

#count=10
#while count >= 0:
#print('Loading:#')
#time.sleep(0.1)
#print('Loading:##',)
#time.sleep(0.1)
#print('Loading:###',)
#time.sleep(0.1)
#print('Loading:####',)
#time.sleep(0.1)
#print('Loading:#####')
#time.sleep(0.1)
#print('Loading:######')
#time.sleep(0.1)
#print('Loading:#######')
#time.sleep(0.1)
#print('Loading:########')
#time.sleep(0.1)
#print('Loading:#########')
#time.sleep(0.1)
#print('Loading:##########')
#time.sleep(0.1)
#print('Loading:###########')
#time.sleep(0.1)
#print('Loading:############')
#time.sleep(0.1)
##count=count-1

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 50 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script

count =10
def loading(count):
	delay=random.uniform(.005,.05)
	print ""
	print "progress :package",10-count+1
	for i in range(101):
		time.sleep(delay)
		update_progress(i/100.0)

while count>0:
	loading(count)
	count=count-1 
	delay=random.uniform(.1,1)
	time.sleep(delay)
print ""
print "Test completed"
time.sleep(1)	
#long process here

