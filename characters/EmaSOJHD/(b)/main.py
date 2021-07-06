import os

for filename in os.listdir():
    print(filename)
    if filename.endswith(".gif"):
        newname = filename.split(')')[1]
        os.rename(filename, newname)
        print("success " + newname)
