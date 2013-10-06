#udacity CS101 course excercise
def find_last(s,t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos
        
def print_multiplication_table(x):
    a = 1
    while x >= a:
        b = 1
        while x >= b:
            print "%d * %d = %d" %(a,b,a*b)
            b = b + 1
        a = a + 1  
        
        
def print_abacus(x):
    xStr = str(x)
    upperRows = 10 - len(xStr)
    
    rowString = "|00000*****   |"
    #print rowString[-4:-1]
    
    while upperRows > 0:
        print rowString
        upperRows = upperRows - 1
        
    #print upperRows
    powerFactor = len(xStr)
    #rowFactor = 10 ** (powerFactor - 1)
    #print rowFactor
    actionRows = len(xStr)
    index = 0
    while actionRows > 0:
        rowFactor = 10 ** (powerFactor - 1)
        abacusElement = int(xStr[index:]) / rowFactor
        
        startStr = rowString[:11-abacusElement] + rowString[-4:-1] + rowString[11 - abacusElement:11] + rowString[-1]
        print startStr
        actionRows = actionRows - 1
        powerFactor = powerFactor - 1
        index = index + 1
    
    
def is_leap_baby(day,month,year):    
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    #return status
def output(status,name):
    if status == True:
        print "%s is rare species. He is leap year!"%name
    if status == False:
        print "Nothing special about %s birthday. Not a leap year!"%name
        
       


                
                                             
        