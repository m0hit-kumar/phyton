num = int(input(" enter a number for whom you want to find factoial of :"))
def fac(num):
    if num == 0:
        return 1

    return num*fac(num-1)    
fact= fac(num)
print(fact)   
