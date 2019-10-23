import time

#Cracking PINs

pin = str(input('Type in your 4-digit PIN \n'))
pinLength = len(pin)  
solvePin = -1

pin = int(pin)

#Checking PIN Length and Cracking PIN

startTime = time.time()

if(pinLength == 4 ):
  confirmPin = int(input('Confirm your PIN \n'))
  while(confirmPin != pin):
    print('Not the same PIN\n')
    confirmPin = int(input('Please retype your PIN\n'))
  while(solvePin != confirmPin):
    solvePin += 1
    print(solvePin)
  else:
    while (pinLength != 4):
     int(input('Your PIN is too long or short, type again.\n'))


endTime = time.time()
print(' ')
print ('Elapsed time ', ((endTime - startTime)))
