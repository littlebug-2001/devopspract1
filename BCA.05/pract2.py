def checkcommon(list1,list2):
    for ele in list1:
        if ele in list2:
            return True
    return False

limit = int(input("Enter the length of the list:"))    
list1=list()

print("ELEMENTS OF LIST1")
for i in range(0,limit):
    print(f"Enter the number {i+1}:",end=" ")
    list1.append(int(input())) 



list2=list()
print("ELEMENTS OF LIST2")
for i in range(0,limit):
    print(f"Enter the number {i+1}:",end=" ")
    list2.append(int(input())) 

if checkcommon(list1,list2):
    print("There are common elements")
else:
    print("There are no common elements")

        
