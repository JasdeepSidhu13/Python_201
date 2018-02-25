#Print statement
'''Multiline comment'''

print ("Hello World")
print ('hi')

#If else statement

x =6
if(x>5):
    print('good')
elif(x<5):
    print('ok')
else:
    print('equal')
# Loops

# While loop
x=0
while x<5:
    print("This is a while loop")
    x=x+1


#for loop

for y in range(1,5):
    print("This is a for loop")


# Functions

import time
import webbrowser
x=1
print("This program started on" +time.ctime())
while(x<=2):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=oy4GOI9vn5M&t=524s")
    x=x+1
