#dictionaries
purse = dict()
purse['money'] = 12#key:money,value:12
purse['candy'] = 3
purse['tissues'] = 75
print purse
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse
print purse['money']
print "====================="

#examples comparing lists and dicts.
lst = list()#list
lst.append(21)
lst.append(183)
print lst
lst[0] = 23
print lst#keys:[0],[1],[2]....
#dictionaries(they use keys)
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print ddd
ddd['age'] = 23
print ddd

#keys: age,course
#lists maintain order, dictionaries don't maintain order
jjj = {'chuck':1,'fred':42,'jan':100}
print jjj
ooo = {}
print ooo
jjj['money'] = 322
print jjj
print '============='

#most common name
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print ccc
ccc['cwen'] = ccc['cwen'] + 1
print ccc
print 'csev' in ccc
print "============="
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts

#get method for dictionary
print "=============="
if name in counts:
    print counts[name]
else:
    print 0
#the same as code above
print counts.get(name,0)
print "============="
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts
names = ['csev','cwen','csev','zqian','cwen','hello']
for name in names:
    print counts.get(name,0)
    
print "==================="

#counting pattern
counts = dict()
print 'Enter a line of text:'
line = raw_input('')
words = line.split()
print 'Words:',words
print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1

print 'Counts',counts
print "==================="

#looping in dictionaries
for key in counts:
    print key, counts[key]
    
#lists of Keys and Values
print list(counts)
print counts.keys()
print counts.values()
print counts.items()
#last one is list of tuples!!
print "==============="

#two iteration variables
for aaa,bbb in counts.items():
    print aaa,bbb
    
#nice example!!
name = raw_input("Enter file:")#enter file name
handle = open(name,'r')#open the file to READ
text = handle.read()#read the whole file
#print text
words = text.split()# split the text into words
#print words
counts = dict()#create a dict. and add the words
for word in words:
    counts[word] = counts.get(word,0) + 1
#print counts.items()
bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print bigWord,bigCount
print "==========="

#excercise 9.4
name = raw_input("Enter file: ")
handle = open(name, 'r')
words = list()
counts = dict()
for line in handle:
    if line.startswith("From "):
        lineSplit = line.split()
        words.append(lineSplit[1])
#print words
for word in words:#fill dictionary 
    counts[word] = counts.get(word,0) + 1
#print counts.items()
bigEmail = None
bigOccur = None
for email,count in counts.items():
    if bigEmail is None or count > bigCount:
        bigEmail = email
        bigCount = count
        
print bigEmail,bigCount

print "==================="


        
        