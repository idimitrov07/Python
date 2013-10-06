fruit = 'banana'
letter = fruit[1]
last = fruit[-1]

#printing with for loop
index = 0
for char in fruit:
    print index,char
    index = index + 1
print '-------------------'
#printing starting from first position
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index,letter
    index = index + 1
print '-------------------'    
#printing starting from last position    
print 'backwords:'
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print index,letter
    index = index - 1
    
print '-------------------'
#type conversion str to int
str3 = '123'
x = int(str3) + 1
print x
print '-------------------'
#count char occurances in a string
word = 'bananas'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count
print '-------------------'
#slicing strings - endind index is "up to, but not including"
s = 'Monty Python'
print s[0:4]
print s[6:7]
print s[6:20]
print s[:2]
print s[8:]
print s[:]
print '-------------------'
#string concatinatio
a = 'Hello'
b = a + 'There'
print b
c = a + ' ' + 'There'
print c
fruit = 'banana'
print 'n' in fruit
print 'm' in fruit
print 'nan' in fruit
if 'a'in fruit:
    print 'Found it!'
print '-------------------'
#string comparison
if word == 'banana':
    print 'All right, bananas.'
if word < 'banana':
    print 'Your word,' + word + ', comes before banana.'
elif word > 'banana':
    print 'Your word,' + word + ', comes after banana'
else:
    print 'All rigth, bananas.'
print '-------------------'
#string Library
greet = 'Hello Bob'
zap = greet.lower()
print zap
print greet
print 'Hi There'.lower()
greet = greet.lower()
print greet

pos = fruit.find('na')
aa = fruit.find('z')
print pos,aa

print greet.upper()

nstr = greet.replace('bob','Jane')
print nstr
nstr = greet.replace('o','X')
print nstr

greet = ' Hello Bob '
print greet.lstrip()

print greet.rstrip()
print greet.strip()

line = 'Please have a nice day!'
print line.startswith('Please')
print line.startswith('p');
print '-------------------'
#small examples
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
#extract host in e-mail address
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos)
print sppos
host = data[atpos + 1:sppos]
print host

print '-------------------'
#string formatting
camels = '42'
print 'I have spotet %s camels' % camels
print 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
print '-------------------'