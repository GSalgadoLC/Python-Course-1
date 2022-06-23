import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

completed = subprocess.run(["python3", "other.py"],
                           capture_output=True,
                           text=True)
print(type(completed))

print(type("args", completed.args))
print(type("returncode", completed.returncode))
print(type("stderr", completed.stderr))
print(type("stdout", completed.stdout))
