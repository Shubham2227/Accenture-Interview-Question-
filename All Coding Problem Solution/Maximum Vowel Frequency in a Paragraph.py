Maximum Vowel Frequency in a Paragraph
Most Frequent Vowel

Mike has written an English paragraph P on the white board, all in upper case. The paragraph contains vowels and consonants. His goal is to find that vowel which has occurred maximum times. He is writing the vowels as "E:19" which means E has occurred maximum times in paragraph P and the count is 19, separated with a :. Your task is to find and return a string representing that vowel and its respective occurrence If no vowel is found, then return "No vowels found". If there is a conflict between two vowels with same occurrence, then return the vowel that arrives first in lexicographic order.
Input Specification:
input1: A string value P representing the paragraph written on the white board
Output Specification:
Return a string representing the vowel with the maximum occurrence along with its respective occurrence. If no vowel is found, then return "No vowels found". If there is a conflict between two vowels with same occurrence, then return the vowel that arrives first in lexicographic order.
xample 1:
input1: THIS IS NOT AN INTEGER VALUE Output: E3
Explanation:
Here, paragraph P is "THIS IS NOT AN INTEGER VALUE",
", Below are the counts of ea
vowel:
• A:2
• E:3
• I:3
• 0:1
• U:1
We can see that the alphabet E and I occurred 3 times, which is maximum. Since E comes before lin lexicographic order, 'E' will be given the preference. Therefore, E:
returned as the output.

def max_vowel_occurrence(P):
    vowels = "AEIOU"
    count = {v: 0 for v in vowels} 
    for char in P:
        if char in count:
            count[char] += 1
    max_vowel = None
    max_count = 0
    for vowel in vowels:
        if count[vowel] > max_count:
            max_vowel = vowel
            max_count = count[vowel]
    if max_vowel:
        return f"{max_vowel}:{max_count}"
    else:
        return "No vowels found"
P = "THIS IS NOT AN INTEGER VALUE"
print(max_vowel_occurrence(P)) 

