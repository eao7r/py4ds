import time

localtime = time.asctime( time.localtime(time.time()) )
print("Exercise 1 local current time :", localtime)

tick = time.time()
time.sleep(1)
tock = time.time()

print("Exercise 2 program took ", str(tock - tick), " seconds to run.")

print('Enter your name:')
x = input()
print('Exercise 3 Output: Hello, ' + x)

print('Enter a number:')
x = input()
try:
    y = float(x)
    print('Exercise 4 Output:  yes, ', x, " is a number")
except:
    print('Exercise 4 Output:  ', x, " is not a number")

print('Enter a list of things, each separated by a space:')
x  = input()
y = x.split()
print("Exercise 5 Output: this is the list you entered:")
for n in y:
    print(n)