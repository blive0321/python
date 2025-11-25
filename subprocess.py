#child process
import subprocess

# ret = subprocess.call('route -n',shell=True)
# Hi from AWS = )
# Hi from AWS 2 = )
print(type(ret))
print(ret)

res = subprocess.call(['route','-n'])
print(res)
