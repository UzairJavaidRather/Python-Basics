
"""The 'codes.py' module will print a list of any dimension """

def print_list(mylist, level):
    """The function 'print_list(arg1,arg2)' takes 2 arguments as list and level. The purpose is to print the list"""
    for i in mylist:
        if isinstance(i,list):
            print_list(i,level+1)
            
            for j in range(level):
                print("\t",end = '')
        else:
            print(i)