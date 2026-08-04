def checkpangram (str2):
    for x in "quvwxyzabcdefghijklmnoprst":
        if x not in str2:
            return False
    return True

line = input("Enter your sentence:")
str2 = line.lower()
if checkpangram(str2):
    print("This sentence is a Pangram.")
else:
    print("This sentence is not a Pangram.")

     