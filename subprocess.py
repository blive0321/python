#child process
import subprocess

ret = subprocess.call('route -n',shell=True)
print(type(ret))
print(ret)

res = subprocess.call(['route','-n'])
print(res)