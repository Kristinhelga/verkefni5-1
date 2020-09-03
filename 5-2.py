
# Get input from user
# Iterate through the sequence 
# Print the length of the sequence from user input



n = int(input("Enter the length of the sequence: ")) 

first = 1
second = 2
third = 3
print(first, second, third, end=' ')

for i in range(4,n+1):
    current = first + second + third
    print(current, end= ' ')
    first = second
    second = third
    third = current