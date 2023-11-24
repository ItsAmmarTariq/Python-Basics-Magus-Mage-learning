import subprocess

code = """for i in range(1,5):
    print(f' hello world {i}')
"""

res = subprocess.run(['python'], input=code, capture_output=True, text=True)
print(res.stdout)
print(res.stdout)

