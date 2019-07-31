# Variables
mark=0
count=0 # No. of students.
passes=0 # No. students who have passes.
total=0 # Total of all the marks.
all_marks=[] # List to hold all marks.
stats=[] # List to hold all statistics. eg: average, highest-mark, lowest-mark
# Category Counters
category1=0 # 70-100
category2=0 # 40-69
category3=0 # 30-39
category4=0 # 0-29
# Common counter
def counter(mymark):
    global total, count, passes, all_marks
    count+=1
    total+=mymark
    all_marks.append(mymark)
    if mymark>=40:
        passes+=1
# Counter
while mark>=0:
    try:
        mark=int(input("Enter mark for student "+str(count+1)+" : "))
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
# Statistics Assignment
try: # Average mark check
    stats.insert(0,total/count)
except:
    stats.insert(0,"No marks were entered.")
try: # Highest mark check
    stats.insert(1,max(all_marks))
except:
    stats.insert(1,"No marks were entered.")
try: # Lowest mark check
    stats.insert(2,min(all_marks))
except:
    stats.insert(2,"No marks were entered.")
# Vertical histogram printing
print("\n"+"-"*10+"Histogram"+"-"*10)
print("\n 0-29 30-39 40-69 70-100")
for i in range(1,max(category1,category2,category3,category4)+1):
    if i<category4+1:
        print(" ","*"," "*2,end="")
    else:
        print(" "*6,end="")
    # 30-39
    if i<category3+1:
        print(" ","*"," "*2,end="")
    else:
        print(" "*6,end="")
    # 40-69
    if i<category2+1:
        print(" ","*"," "*2,end="")
    else:
        print(" "*6,end="")
    # 70-100
    if i<category1+1:
        print(" ","*")
    else:
        print(" ")
print("\n",count,"students in total.")
print("\n"+"-"*9+"Statistics"+"-"*10,"\n")
print("Average mark \t:", stats[0])
print("Students passed :", passes)
print("Highest mark \t:", stats[1])
print("Lowest mark \t:", stats[2])
