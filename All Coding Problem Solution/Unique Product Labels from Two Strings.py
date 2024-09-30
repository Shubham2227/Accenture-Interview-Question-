You are a product designer working for a company that manufactures
various products. You have two sets of product labels, represented by strings A and B. Your task is to find and return an integer value representing the number of unique product labels you can create by taking the characters individually from 'A' or 'B' or by combining the characters from
'A' and 'B'. All the characters in a product label should be the same and no two product labels should have a common character.
Input Specification:
inputt: A string value A input2: A string value B
JAV
Output Specification:
Return an integer value representing the number of unique product labels you can create by taking the characters individually from 'A' or '8' or by combining the characters from 'A' and 'B' as per the conditions mentioned above. 
Example 1:
inputi: hea
input2 : oed
an Output: 5
Explanation:
Here, string A is 'hea' and string B is 'oed'. By combining the characters from both strings, we can create the following unique product labels:
• "h"
"ee”
“a”
"о
"d"
Each of these labels has the same character throughout and no two labels
have a common character. Therefore, the number of unique product Jabeis
we can create is 5. Hence, 5 is returned as the output

*************************** Solution-1  ****************************
def unique_product_labels(A: str, B: str) -> int:
    set_A = set(A)
    set_B = set(B)
    unique_labels = set_A.union(set_B)
    return len(unique_labels)
input1 = "heaa"
input2 = "oed"
output = unique_product_labels(input1, input2)
print(output)  # Expected Output: 5

*************************** Solution-2  ****************************


def unique_product_labels_v2(A: str, B: str) -> int:
    freq = [0] * 26
    for char in A:
        freq[ord(char) - ord('a')] = 1
    for char in B:
        freq[ord(char) - ord('a')] = 1
    return sum(freq)

input1 = "abc"
input2 = "def"
output = unique_product_labels_v2(input1, input2) 
print(output)

      

      
