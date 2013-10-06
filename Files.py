#opening a file
fhand = open('test.txt','r')
stuff = 'X\nY'
print stuff
print len(stuff)
#read each line in a file
for line in fhand:
    print line
print '--------------'    
#count lines in a file
fhand = open('test.txt','r')
count = 0
for line in fhand:
    count = count + 1
    
print 'Line Count', count
print '--------------'
#read the Whole file
fhand = open('test.txt','r')
inp = fhand.read()
print len(inp)
print inp[:20]
print inp
print '--------------'
#searching through a file
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line
        
print '--------------'
#skipping with 'continue'
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):#skip what you need
        continue
    print line#print what you need

print '--------------'
#using 'in' to select lines
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print line
    
print '--------------'
#promt for file name
fname = raw_input('Enter a file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print 'There were %d subject lines in %s' % (count,fname)
print '--------------'
#catch a bad file name
fname = raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were', count,'subject lines in', fname
print '--------------'


print '--------------'

fname = raw_input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print line.upper()
    
print '--------------'
print '--------------'
fname = raw_input('Enter file name: ')
fhand = open(fname)
count = 0
sum = 0
average = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        sppos = line.find('.')
        strNum = line[sppos - 1:]
        floatNum = float(strNum)
        sum = sum + floatNum
average = sum / count
print "Average spam confidence:",average