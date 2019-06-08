# Constant
print(123)
print(98.6)
print('Hello World')

# Variables
x = 12.2
y = 14
x = 100

# Expressions
xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

x = 1 + 2 * 3 - 4 / 5 ** 6
x = 1 + 2 ** 3 / 4 * 5

# Variable Type
ddd = 1 + 4
print(ddd)
eee = 'hello ' + 'there'
print(eee)
eee = eee + 1
type(eee)
type('hello')
type(1)

# Type Conversions
print(float(99) + 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)

sval = '123'
type(sval)
print(sval + 1)
ival = int(sval)
type(ival)
print(ival + 1)
nsv = 'hello ben'
niv = int(nsv)

# Integer Division
print(10 / 2) 
print(9 / 2) 
print(99 / 100) 
print(10.0 / 2.0) 
print(99.0 / 100.0) 

# User Input
nam = input('Who are you? ')
print('Welcome', nam)

# ===============================
# Exercise --> Ex1.1.py
# ===============================

# Conditional Statement
x = 5
print('Before 5')
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

# try / except
astr = 'Bob'
try:
    print('Hello') 
    istr = int(astr)
    print('There') 
except:
    istr = -1

print('Done', istr)

# ===============================
# Exercise --> Ex1.2.py
# ===============================

# Functions
def add_numbers(x, y):
    return x + y
add_numbers(1, 2)

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
print(add_numbers(1, 2, flag=True))

# ===============================
# Exercise --> Ex1.3.py
# ===============================

# While Loop
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# For Loop
professors = ['Ben', 'Michael', 'Tony']
for professor in professors : 
   print('Happy New Year:', professor)
print('Done!')

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num > largest_so_far :
      largest_so_far = the_num
   print(largest_so_far, the_num)
print('After', largest_so_far)

# ===============================
# Exercise --> Ex1.4.py
# ===============================

# Strings
fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

zot = 'abc'
print(zot[5])

print(len(fruit))

for letter in fruit: 
    print(letter)

# Slicing
s = 'Writing Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])
	
# Concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

# Logical Operation
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:	print('Found it!')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
	
# Importance in import str
import str

fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

greet = 'Hello Ben'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

greet = 'Hello Ben'
nstr = greet.replace('Ben','Tony')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

greet = '   Hello Ben  '
greet.lstrip()
greet.rstrip()
greet.strip()

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')

# ===============================
# Exercise --> Ex1.5.py
# ===============================

# DateTime
import datetime as dt

dtnow = dt.datetime.now()
print(dt.datetime.now())
type(dtnow)
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

today = dt.date.today()
print(today)
delta = dt.timedelta(days = 100)
print(delta)
today - delta
today > today - delta

date0 = dt.datetime.strptime('2019-01-02 03:04:05', '%Y-%m-%d %H:%M:%S')
print(dt.datetime.strftime(dtnow, '%H:%M:%S %Y%m%d'))

import time

time.time()
time.gmtime(0)

starttime = time.time()
time.sleep(10)
endtime = time.time()
print(endtime-starttime, 'sec past.')

# ===============================
# Exercise --> Ex1.6.py
# ===============================

# Files
handle = open('welcome.txt')
print(handle)
handle2 = open('goodbye.txt')

stuff = 'Hello\nWorld!'
print(stuff)
len(stuff)

for line in handle:
    print(line)
lines = handle.read()
print(len(lines))

handle.close()

file = open("testing.txt","w") 
file.write("Hello World") 
file.write("This is a Python Programming class") 
file.write("Happy coding.") 
file.write("Cheers, Alan.")  
file.close() 

# ===============================
# Exercise --> Ex1.7.py
# ===============================

# ===============================
# Assignment 1 --> Asg1.py
# ===============================

