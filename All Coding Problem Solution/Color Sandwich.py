Color Sandwich
Sam is a cook and he has colored breads and stuffing with which he had made some sandwiches. A sandwich can be made by keeping multiple or no stuffing between two same-colored breads like,
gabeq (where abc represents stuffing and q represents coloured bread). The sandwiches are placed one over the other represented by a string 5 where each character depicts either bread or 
the stuffing. Your task is to find and retur a string value representing the colour of the breads used in all sandwiches.
Input Specification:
inputl: A string 5 representing the sandwiches,
Output Specification:
Retum a string value representing the colour of the breads used in all sandwiches
Example 1: input1: qezcquu
Output : qu

********************   Solution-1 Brute Force ***************

def find_bread_colors(s):
    bread_colors = set()
    n = len(s)

    # Iterate through the string to find matching bread pairs
    for i in range(n):
        start_bread = s[i]
        for j in range(i + 1, n):
            if s[j] == start_bread:
                bread_colors.add(start_bread)
                break  # Stop looking once we find the matching bread

    # Convert the set of bread colors to a sorted string
    return ''.join(sorted(bread_colors))

# Example input
input_str = "qezcquu"
output = find_bread_colors(input_str)
print(output)  # Output: qu


********************   Solution-2 Best CASE ***************


def find_bread_colors(s):
    # A set to store the unique bread characters
    bread_colors = set()

    # Iterate through the string
    n = len(s)
    i = 0

    while i < n:
        # Check if the current character can form a pair
        current_bread = s[i]
        j = i + 1

        # Find the next occurrence of the same bread character
        while j < n and s[j] != current_bread:
            j += 1

        # If a pair is found, add it to the set
        if j < n:
            bread_colors.add(current_bread)
        
        # Move to the next character after the found pair
        i = j + 1

    # Convert the set to a sorted string
    return ''.join(sorted(bread_colors))

# Test cases
print(find_bread_colors("qezcquu"))  # Expected output: qu
print(find_bread_colors("aabaa"))    # Expected output: a
print(find_bread_colors("abcdef"))   # Expected output: (empty string)
print(find_bread_colors("bbbbbb"))   # Expected output: b
print(find_bread_colors("qpqrsqp"))  # Expected output: pq

