import os

#file exist?
if os.path.exists('main_count'):
    print("File exists...")
else:
    print("File not exists...")

#dir exists?
dir="/home/Brandon"
if os.path.isdir(dir):
    print("Directory exists...")
else:
    print("Directory not exists...")

#complete path?
if os.path.isabs(dir):
    print("Complete path...")
else:
    print("Incomplete path...")


os.mkdir("/home/Brandon/python")
if os.path.exists("/home/Brandon/python"):
    print("Create directory successful...")
else:
    print("Create directory failed...")
#os.rmdir("/home/Brandon/python")

path = os.path.abspath("pyhton")
print(path)


if dir == os.getcwd():
    print("The work directory is correct...")
else:
    print("cd directory first...")
