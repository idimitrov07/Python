import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('^From:',line):
        #print line
    #if re.search('^X.*:',line):
        #print line
    #if re.search('^X-\S+:',line):
        #print line
    
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print y
z = re.findall('[aeiou]+',x)
print z
x = 'From: Using the :character'
y = re.findall('^F.+:',x)
print y
y = re.findall('^F.+?:',x)
print y
x = 'From alohsada.dsada@gmail.co.uk sat 231 5 sfadas 432'
y = re.findall('^From (\S+@\S+)',x)
print y
data = 'From alohsada.dsada@gmail.co.uk sat 231 5 sfadas 432'
y = re.findall('@([^ ]+)',data)
print y
y = re.findall('^From .*@([^ ]*)',data)
print y

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
    
print 'Maximum:',max(numlist)

x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+',x)
print y 
