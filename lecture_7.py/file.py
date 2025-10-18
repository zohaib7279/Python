import os
os.remove("demo.txt")
f = open("demo.txt", "a")
f.write()
#print(f.read)
f.close()
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
with open("demo.txt", "w") as f:
    data = f.write("new data")
