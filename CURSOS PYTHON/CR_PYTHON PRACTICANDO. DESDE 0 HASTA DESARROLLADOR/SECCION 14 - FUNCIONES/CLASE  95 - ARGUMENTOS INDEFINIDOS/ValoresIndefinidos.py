def argumento(*num):
    return type(num)

def argumento2(*num):
    for i in num:
        print(type(i))
    

print(argumento(56.562))
print(argumento2(1,2,3))