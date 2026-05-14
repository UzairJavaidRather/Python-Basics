
"""The 'codes.py' module will print a list of any dimension """

def print_list(mylist, level= 0, indent = True):
    """The function 'print_list(arg1,arg2)' takes 2 arguments as list and level. The purpose is to print the list"""
    for i in mylist:
        if isinstance(i,list):
            print_list(i,level+1,indent)
        else: 
            if indent: 
                for j in range(level):
                    print("\t",end = '')
        
            print(i)
            
            
            
            
#mylist = [0,[1,2],[3,4]]   
   
       
#print_list(mylist)

def print_tuple(mytuple, level= 0, indent = True):
    """The function 'print_list(arg1,arg2)' takes 2 arguments as tuple and level. The purpose is to print the tuple"""
    for i in mytuple:
        if isinstance(i,tuple):
            print_tuple(i,level+1,indent)
        else: 
            if indent: 
                for j in range(level):
                    print("\t",end = '')
        
            print(i)

def print_set(myset, level= 0, indent = True):
    """The function 'print_list(arg1,arg2)' takes 2 arguments as set and level. The purpose is to print the set"""
    for i in myset:
        if isinstance(i,set):
            print_list(i,level+1,indent)
        else: 
            if indent: 
                for j in range(level):
                    print("\t",end = '')
        
            print(i)