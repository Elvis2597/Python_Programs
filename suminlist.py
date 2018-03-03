def fun(l1):
    
    Sum=0
    c=0
    for i in l1:
        try:
            
            Sum=Sum+i
            c+=1
        except TypeError:
            pass
    try:
        
        av=float(Sum/c)
        print av
    except ZeroDivisionError:
        print'List is Empty'
    

            
     

        
  
    
