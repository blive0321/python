#child process
import subprocess

# ret = subprocess.call('route -n',shell=True)
# Hi from AWS = )
print(type(ret))
print(ret)

res = subprocess.call(['route','-n'])
print(res)
