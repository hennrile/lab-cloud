import subprocess

repo_path = "/Users/huy/Desktop/lab-cloud/data"

subprocess.call("cd" + repo_path, shell=True)

# Thêm tất cả các file vào staging area
subprocess.call("git add .", shell=True)

# Commit với message "update code"
subprocess.call("git commit -m 'update code'", shell=True)

# Push lên GitHub
subprocess.call("git push", shell=True)