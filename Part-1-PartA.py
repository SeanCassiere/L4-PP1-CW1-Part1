# Variables
count=0
mark=0
category1=0
category2=0
category3=0
category4=0
# Counter
while mark>=0:
    try:
        mark=int(input("Enter mark for student: "))
    except:
        print("Enter only whole numbers.\n")
        continue
    if mark>=70 and mark<=100:
        category1+=1
        count+=1
    elif mark>=40 and mark<=69:
        category2+=1
        count+=1
    elif mark>=30 and mark<=39:
        category3+=1
        count+=1
    elif mark>=0 and mark<=29:
        category4+=1
        count+=1
    else:
        continue
print("\n0-29\t", end="")
for i in range(category4):
    print("*", end="")
print("\n30-39\t", end="")
for i in range(category3):
    print("*",end="")
print("\n40-69\t", end="")
for i in range(category2):
    print("*", end="")
print("\n70-100\t", end="")
for i in range(category1):
    print("*", end="")
print("\n"+str(count),"students in total.")
