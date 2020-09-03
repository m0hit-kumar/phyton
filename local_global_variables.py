# WAP to demonstrate local and global variables under a function


a=5
def local():
    a=10
    print(a)
    
print(a)
local()
