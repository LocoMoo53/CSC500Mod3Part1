# Getting user input 
time = int(input('Enter the current time in hours:'))
alarm = int(input('Enter length of time to wait in hours:'))

# Creating variable 'wake' 
wake = (time + alarm) %24

# If/else statementt to determine time of day to wake up
if (wake <= 24):
        print ('The alarm will go off at', wake, 'hours.')
else: print ('The alarm will go off at', wake - 24, 'hours.')
