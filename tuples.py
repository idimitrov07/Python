#tuples - like lists, non changable list!!
x = ('glen', 'sally', 'joseph')
print x[2]
y = (1,9,2)
print y
print max(y)
for i in y:
    print i
#y[2] = 3#not allowed
#print y
#tuples are like lists, and like strings(cannot change elements)
(x,y) = (4,'fred')
print x,y
a, b = (99,98)
print a
print b
#tuples and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print k,v
    
tups = d.items()
print tups
#tuples are compareble
(0,1,2) < (5,1,2)
('Jones','Sally') > ('Adams','Sam')
#sorting list of Tuples
d = {'a':10,'b':1,'c':22}
t = d.items()
print t
t.sort()
print t
#using sorted()
d = {'a':10,'b':1,'c':22}
print d.items()
t = sorted(d.items())
print t
for k,v in sorted(d.items()):
    print k,v
#sort by values instead of key
c = {'a':10,'b':1,'c':22}
temp = list()
for k,v in c.items():
    temp.append((v,k))
print temp
temp.sort(reverse=True)
print temp
#temp[1][0] = 4 #cannot do that(element is a tuple
#program finding 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
lst = list()
for key, val in counts.items():
    lst.append((val,key))
    
lst.sort(reverse=True)

for val,key in lst[:10]:
    print key,val

print "================="
#shorter vesion 
c = {'a':1,'b':22,'c':13}
print sorted([(val,key) for key,val in c.items() ])

#excericise 10.2
name = raw_input("Enter file: ")
fhand = open(name,'r')
linesList = list()
for line in fhand:
    line = line.strip()
    if line.startswith('From '):
        linesList.append(line)
    
#for line in linesList:
    #print line
    
counts = dict()
for line in linesList:
    words = line.split()
    time = words[-2].split(':')
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1
    #print hour
    
#print counts.items()
hourList = list()
for key,val in counts.items():
    hourList.append((key,val))
    
hourList.sort()
#print hourList
for hour,count in hourList:
    print hour,count
    

    