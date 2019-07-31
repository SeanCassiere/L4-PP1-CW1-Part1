# Variables
mark=0
count=0
total=0
all_marks=[]
stats=[]
passes=0
# Category Counters
category1=0 # 70-100
category2=0 # 40-69
category3=0 # 30-39
category4=0 # 0-29
# Common counter
def counter(mymark):
    global total, count, passes
    count+=1
    total+=mymark
    all_marks.append(mymark)
    if mymark>=40:
        passes+=1
# Counter
while mark>=0:
    try:
        mark=int(input("Enter mark for student: "))
    except:
        print("Enter only whole numbers.\n")
        continue
    if mark>=70 and mark<=100:
        category1+=1
        counter(mark)
    elif mark>=40 and mark<=69:
        category2+=1
        counter(mark)
    elif mark>=30 and mark<=39:
        category3+=1
        counter(mark)
    elif mark>=0 and mark<=29:
        category4+=1
        counter(mark)
    else:
        if mark>100:
            print("Given mark exceeds maximum range of 100.\nPlease enter a valid mark.\n")
        continue
# Stats assignment
try:
    stats.insert(0,total/count)
except:
    stats.insert(0,"No marks were entered.")
try:
    stats.insert(1,max(all_marks))
except:
    stats.insert(1,"No marks were entered.")
try:
    stats.insert(2,min(all_marks))
except:
    stats.insert(2,"No marks were entered.")
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
print("Average mark:",stats[0])
print("Number of students with a pass mark of 40 or above:",passes)
print("Highest mark:",stats[1])
print("Lowest mark:",stats[2])
