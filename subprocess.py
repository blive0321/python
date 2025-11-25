#child process
import subprocess

# ret = subprocess.call('route -n',shell=True)
# Hi from AWS = )
# Hi from AWS 2 = )
# Hi from AWS 3 = )
# Hi from AWS 4 PR = )
print(type(ret))
print(ret)

res = subprocess.call(['route','-n'])
print(res)
