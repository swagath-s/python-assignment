def teen(prev):
    """textifies tens place of teen numbers"""
    if prev.endswith("one"):                               #
        prev = prev.replace("one", "eleven")               #
    elif prev.endswith("two"):                             # if eleven, twelve or thirteen
        prev = prev.replace("two", "twelve")               #
    elif prev.endswith("three"):                           #
        prev = prev.replace("three", "thirteen")           #
    elif prev.endswith("t"):
        prev = prev + "een"                                     #
    else:                                                       # everything else
        prev = prev + "teen"                                    # 
    return prev                                                 

def simple(dig):
    """ Converts a single numeric digit into text"""
    
    textifiedDigits = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    return textifiedDigits[dig]

def ty(dig):
    tens = ("", "teen/ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    return tens[dig]

"""def caps(line):
    temp = line[1].swapcase()
    line = line.replace(line[0:2], temp)
    return line """

denom = ("", " thousand,", " million,", " billion,")

def textify(n):
    """textifies and prints large numbers three digits at a time"""
    for k in range(4, -1, -1):
        number = n%(1000**(k+1))/(1000**k)               #FUNCTION KILLER!
        prev = ""
        for i in range(3):        
            digit = number%10
            if digit:
                if i==1:                                        #if textifying tens digit
                    if digit == 1:                              #if that digit is a one
                        prev = teen(prev)              
                    else:
                        prev = ty(digit) + " " +prev     #add 'digit-ty' to the beginning of the string
                    prev = prev+denom[k]
                elif i ==2:
                    prev = simple(digit)+" hundred and "+ prev
                else:
                    prev = simple(digit)+prev
                
            number = number/10

        
        #print caps(prev),
        print prev,

#todo:
#1.fix capital and space

