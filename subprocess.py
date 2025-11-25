#child process
import subprocess

# ret = subprocess.call('route -n',shell=True)
# Hello, this is Brandon from AWS!!!!!!!!!
# Hello, this is Brandon from AWS!!!!!!!!! ( Test 2 )
# Hello, this is Brandon from AWS!!!!!!!!! ( Test 3 )
print(type(ret))
print(ret)

res = subprocess.call(['route','-n'])
print(res)
