'''
1) Addition of Array Elements
n=int(input("Enter the number of elements:"))
arr=[]
print("Enter the elements")
for i in range(n):
    element=int(input())
    arr.append(element)
sum=0
for i in arr:
    sum+=i
print("Sum of Array Elements",sum)


2) Addition of Two Arrays
n= int(input("Enter the number of elements"))
arr1=[]
arr2=[]
result=[]
print("Enter the elements of the first array:")
for i in range(n):
    arr1.append(int(input()))
print("Enter the elements of the Second array:")
for i in range(n):
    arr2.append(int(input()))
for i in range(n):
    result.append(arr1[i]+arr2[i])
print("First Array:",arr1)
print("Second Array:",arr2)
print("Sum Array:",result)
'''

#3) Matrix Creation
m1=[]
r1=int(input("Enter no. of rows for matrix 1"))
c1=int(input("Enter no. of column for matrix 1"))
for i in range(0,r1):
    a=[]
    for j in range(0,c1):
        a.append(int(input("Enter data for m1")))
    m1.append(a)
print(m1)
