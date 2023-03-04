
# ******************************
# Make your Code
# ******************************
count = []
flag = 0

for i in range(10):
    num = int(input("Enter a number: "))
    count.append(num)

totalc = 0

for i in count:
    if i % 2 == 0:
        flag = flag + 1
    else: 
        if flag > 0:
            totalc = totalc + 1
            flag = 0
if flag > 0:
    totalc = totalc + 1

    
print(totalc)
        








# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
