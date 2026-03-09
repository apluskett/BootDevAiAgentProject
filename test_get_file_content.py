from functions.get_file_content import get_file_content

'''
print(f"Result for Lorem ipsum:") #testing a known file with 20k words
print(get_file_content("calculator", "lorem.txt"))
'''

print(f"\nResult for 'calculator/main.py':")
print(get_file_content("calculator", "main.py"))

print(f"\nResult for 'pkg/calculator.py':")
print(get_file_content("calculator", "pkg/calculator.py"))

print(f"\nResult for '/bin/cat':")
print(get_file_content("calculator", "/bin/cat"))

print(f"\nResult for 'pkg/does_not_exist.py':")
print(get_file_content("calculator", "pkg/does_not_exist.py"))