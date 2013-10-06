print ['red', 'yellow','blue']
print ['red',24,98.6]
print [1,[5,6],7]
for i in [5,4,3,2,1]:
    print i
    
print 'Blast'
print '----------------'
#lists are mutable
friends = ['Joseph', 'Glenn', 'Sally']
print friends[1]
lotto = [2,3,4,5,6,7,8]
lotto[2] = 432
print lotto
print len(lotto)
print '----------------'

#range function
print range(4)
print range(len(friends))
for friend in friends:
    print 'Happy New Year:',friend
print '----------------'

for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year:',friend
print '----------------'

#concatenating lists 
a = [1,2,3]
b = [4,5,6]
c = a + b
print c
d = ['s','d','f']
print c + d
print '----------------'

#list slicing
t = [9,41,12,3,74,15]
print t[1:3]
print t[3:]
print t [:]
print '----------------'
#building a list
stuff = list()
stuff.append(99)
stuff.append('book')
print stuff
stuff.append('cookie')
print stuff
stuff.pop()
print stuff
print 20 in stuff
stuff.append('hello')
print stuff
stuff.sort()
print stuff
nums = [3,41,12,9,74,15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)
print '----------------'
#read nums and print average
numlist = list()
while True:
    inp = raw_input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    
print sum(numlist)/len(numlist)
print '-------------------'
#string split and lists
abc = "with three words."
stuff = abc.split()
print stuff
print stuff[0]
print stuff[2]
for w in stuff:
    print w
    
line = 'A lot           of spaces'
etc = line.split()
print etc
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)
print"=================="
#open file, split strings,extract days of week
fhand = open('mbox-short.txt')
for line in fhand:
    line =  line.strip()
    if not line.startswith('From '):
        continue 
    words = line.split()
    print words[1]
    
print "============"
h = [1,2,[2,3,[1,2,3,4]],5,6,7]
print h[2][2][2]
print "=============="
email = words[1]
host = email.split('@')
print host[1]
print "=========="
#excercise 8.4
fname = raw_input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    lineSplit = line.split()
    for word in lineSplit:
        if word not in lst:
            lst.append(word)
lst.sort()            
print lst
print '================='
#excercise 8.5
fname = raw_input('Enter a file name: ')
fhand = open(fname)
counter = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        lineSplit = line.split()
        print lineSplit[1]
        counter = counter + 1
print "There were %d lines in the file with From as the first word" % counter