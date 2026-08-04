def display(list1):
    threshold = int(input("Enter threshold value:"))
    counter = 0
    #print("Elements less than threshold are:")
    for x in list1:
        if x < threshold: 
            counter+=1 

    return counter        
limit = int(input("Enter the length of the list:"))
list1=list()
for i in range(0,limit):
    print(f"Enter the number {i+1}:",end=" ")
    list1.append(int(input())) 
print("The no. of elements less than threshold are",display(list1))    
