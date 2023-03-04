
# ******************************
# Make your Code
# ******************************
count = 0
flag = False

for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        if flag == False:
            flag = True
        count += 1
    else:
        if flag and count > 1:
            count -= 1
        flag = False

if flag and count > 1:
    count -= 1

print(count)





# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
