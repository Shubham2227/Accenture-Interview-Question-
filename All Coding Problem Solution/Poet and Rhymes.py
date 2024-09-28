
Full explanation checkout Youtube "Debug With Shubham"
Poet and Rhymes

A poet has asked you for assistance in writing poems. He has given you a string S and a dictionary D and he asks you to find, from the dictionary, a word which rhymes
best with S. Words are said to rhyme when the last syllables of the words are the same, like "cave" and "gave",
', or "typical" and "critical." The words will be deemed to
rhyme best if the last few characters of the words match the most.
Your task is to find and return a string value denoting the word which rhymes best with S, from the dictionary D. If no such word is found, return the string "No Word"
Note
• If all the characters match, it is the same word and not a rhyming word.
• All the given words are in lowercase.
• If multiple rhyming words are found, then choose the word with the least index.
Input Specification:
input1: A string value S, representing a single word input2: A string array D, representing the dictionary 
input3: An integer value representing the length of array D
Output Specification:
Return a string value denoting the word which rhymes best with S from the dictionary D. If no such word is found, return the string "No Word".
Example 1:
input1 : thunder input2 : (puzzle,thunder,powder,blender,under)
input3: 5
Output : under
Explanation:
Here, the given word S is "thunder." We can find the rhyming word/s from the dictionary in the following way:
• The first word "puzzle" does not rhyme at all and has no common characters with the word "thunder". at the end.
• The second word "thunder" is exactly the same word as the given word, so it will not be considered as a rhyming word.
• The third word is "powder" and has the 3 letters "der" in common at the end and is the least rhymina amona the list.
The fourth word is "blender" and has the 4 letters "nder" in common at the
end and is the second most rhyming among the list.
• The last word is "under" and it is the most rhyming word as it has the 5 letters under" in common with the word at the end.
Since "under" is the most rhyming word among those in the given dictionary, under is returned as the output.
Example 2: inputi: pole
input2 : (kilo, super, cake} input3 : 3
4030
Output : cake
Explanation:
Here, the given word S is "pole". We can find the rhyming word from the dictionary in the following way:
• The word "cake" has a single letter common in the end with "pole" and the rest of the words don't match.
Since "cake" is the most rhyming word among those in the given dictionary, cake is returned as the output


def find_rhyming_word(S, D, n):
    best_word = "No Word"
    best_match_length = 0
    for word in D:
        if word == S:
            continue
        match_length = 0
        min_len = min(len(S), len(word))
        for i in range(1, min_len + 1):
            if S[-i] == word[-i]:
                match_length += 1
            else:
                break
        if match_length > best_match_length:
            best_match_length = match_length
            best_word = word
    return best_word
S1 = "thunder"
D1 = ["puzzle", "thunder", "powder", "blender", "under"]
n1 = len(D1)
print(find_rhyming_word(S1, D1, n1))  

S2 = "pole"
D2 = ["kilo", "super", "cake"]
n2 = len(D2)
print(find_rhyming_word(S2, D2, n2))  

