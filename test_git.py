# from github import Github
# #asscess token
# g = Github("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")
# #Lấy thông tin repo
# repo = g.get_repo("HQHuy/Learn-IT")

# #Create File
# contents = "Nội Dung File"
# path = "C:\\Users\\TGDD\\Documents\\GitHub\\lad-cloud\\data\\test_github.txt"
# message = "Add data"
# branch = "main"

# # Update file to created
# # contents = "Nội dung mới của file"
# # path = "path/to/file.txt"
# # message = "Cập nhật file"
# # branch = "main"
# file = repo.get_contents(path)
# repo.update_file(file.path, message, contents, file.sha, branch=branch)

import subprocess
from pexpect import popen_spawn

user = 'HQHuy'
password = '2345Nbvc'

cmd = "cd C:\\Users\\TGDD\\Documents\\GitHub\\lad-cloud\\data\\test_github.txt"
subprocess.call(cmd, shell=True)

subprocess.call("git add .", shell=True)
subprocess.call('git commit -m "python project update"', shell=True)
subprocess.call("git remote set-url origin hennrile/lab-cloud", shell=True)

child_process = popen_spawn.PopenSpawn("git push")
child_process.expect('User')
child_process.sendline(user)
child_process.expect('Password')
child_process.sendline(password)

print('end of commands')