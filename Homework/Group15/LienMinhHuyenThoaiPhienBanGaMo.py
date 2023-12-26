# Input the dimensions of the script and the number of values to process
n, m = map(int, input().split())

# Initialize an array to store the count of each character in the script
value = [0] * 121  # Using 121 to account for ASCII values of characters 'q', 'w', 'e', 'r'

# Input the script as a string
script = input()

# Iterate through the values to process
for _ in range(m):
    temp = int(input())

    # Update the count of each character in the script
    for j in range(temp):
        value[ord(script[j])] += 1

    # Check if the entire script has been processed
    if temp == len(script):
        print(value[ord('q')], value[ord('w')], value[ord('e')], value[ord('r')])
        break

# Process the remaining characters in the script
for k in range(len(script)):
    value[ord(script[k])] += 1

# Print the count of each character 'q', 'w', 'e', 'r'
print(value[ord('q')], value[ord('w')], value[ord('e')], value[ord('r')])

