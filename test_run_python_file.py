from functions.run_python_file import run_python_file

print('Result of "calculator", "main.py":')
print(run_python_file("calculator", "main.py"))

print('Result of "calculator", "main.py", with args ["3 + 5"]:')
print(run_python_file("calculator", "main.py", args=["3 + 5"]))

print('Result of "calculator", "tests.py":')
print(run_python_file("calculator", "tests.py"))

print('Result of "calculator", "../main.py":')
print(run_python_file("calculator", "../main.py"))


print('Result of "calculator", "nonexistent.py":')
print(run_python_file("calculator", "nonexistent.py"))


print('Result of "calculator", "lorem.txt":')
print(run_python_file("calculator", "lorem.txt"))
