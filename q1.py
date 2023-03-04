
# ******************************
# Make your Code
# ******************************
count = 0
flag = False

for i in range(10):
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        if not flag:
            count += 1
            flag = True
    else:
        flag = False     
    
    
    
    

print(count)


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
