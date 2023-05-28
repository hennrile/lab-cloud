import subprocess
from pexpect import popen_spawn


user = 'HQHuy'
password = '2345Nbvc'

cmd = "cd C:\\Users\TGDD\Documents\GitHub\lad-cloud\test_github"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git add ." 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "python project update"'
subprocess.call(cmd, shell=True)

cmd = "git remote set-url origin https://github.com/hennrile/lab-cloud"
subprocess.call(cmd, shell=True)

cmd = "git push "
child_process = popen_spawn.PopenSpawn(cmd)
child_process.expect('User')
child_process.sendline(user)
child_process.expect('Password')
child_process.sendline(password)
print('returned value:', returned_value)

print('end of commands')