import functions.write_file as write_file
    
print("\nResult: 'calcualtor' 'lorem.txt' 'wait, this isn't lorem ipsum!'")
print(write_file.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("\nResult: 'calculator' 'pkg/morelorem.txt' 'Lorem ipsum dolor sit amet'")
print(write_file.write_file("calculator", "pkg/morelorem.txt", "Lorem ipsum dolor sit amet"))

print("\nResult: 'calculator' '/tmp/temp.txt' 'this should not be allowed'")
print(write_file.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))