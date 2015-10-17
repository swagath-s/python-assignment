count = 0


def counter(n):
    """if type(n)!="type 'int'":
        print "invalid input. please input an integer" """
         #check for integer value
    
    if (n):
        global count
        count+=1
        counter(n/10)
    else:
        print count
        count = 0
       




        
