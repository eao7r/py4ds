import time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

tick = time.time()
time.sleep(1)
tock = time.time()

print("This program took ", str(tock - tick), " seconds to run.")


w = True
while w is True:
    print('Enter your name:')
    x = input()
    if x.isalpha():
        w = False
        print('Hello, ' + x)

print('Enter a number:')
x = input()
try:
    y = float(x)
    print('Yes, ', x, " is a number")
except:
    print(x, " is not a number")

print('Enter a list of things, each separated by a space:')
x  = input()
y = x.split()
print("This is the list you entered:")
for n in y:
    print(n)