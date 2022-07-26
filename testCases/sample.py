fo = open("sample.txt", "r+")

print("the file", fo.name)

# fo.write("am mohan form chennai\nacbdabdkvcbsdkvbdk jjkacbdajkcb\n")
a = fo.read(10)

print("read", a)

postion = fo.tell()

print(postion)

postion = fo.seek(0, 0)

b = fo.read(10)
b = fo.readline()

l = ["jjhvhjvb\n", "kjbhkb jkbj\n", "jbhkbkjb"]
c = fo.writelines(l)
print(b)

import os


os.remove()
os.mkdir()
os.chdir()

os.getcwd()
os.rmdir()



fo.close()
