str = "hello how are you! "

f = open("myfile.txt" , "w")

f.write(str)

f.close()

f1 = open("myfile.txt" , "r")
data = f1.read()
print(data)

f1.close()

f2 = open("myfile.txt" , "a")
str2 = "you are amazing !"
f2.write(str2)

f2.close()

with open("myfile.txt") as f3:
    print(f3.read())