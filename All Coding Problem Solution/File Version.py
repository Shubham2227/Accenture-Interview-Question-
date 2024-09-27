
You are given a string array S that contains the names of some files along with their versions. Your task is to find and return an integer vanse representing the latest version out of all the files that are correctly named in the array. A file is considered correct if it follows the format of the file named as "File_X" (where X represents the file version number). Return -1 if there are no correct files in the array.
Note:
• A file is incorrect if the name of the file does not match the format.
• If there is no file in the files array then also return - 1.
Input Specification:
input1: A string array S, representing the names of the files. input2 : An integer value representing the size of the array.
Output Specification:
Return an integer value representing the latest version out of all the files that are correctly named in the array.

Example 1: inputt: (File 1, File 3, File 2)
input2 : 3
Output : 3
Explanation:
Here the given file array is ["File_1","File_3", "File 2"). As we can see, all the files are named using the correct file format of "File Version". The second file has the greatest file version, which is 3Jence, 3 is returned as the output.
Example 2: input1: 0
input2: 0
Output : -1
Explanation:
Here the given file array is . As we can see, there are no files in the array. Hence, -1 is returned as the output.


Solution 1 

def find_latest_version(S: list, n: int) -> int:
    if n == 0:
        return -1
    max_version = -1
    for file_name in S:
        if file_name.startswith("File_"):
            sp = int(file_name.split("_")[1])
            max_version = max(max_version , sp)
    
    return max_version
    
input1 = ["File_5", "File_3", "File_2","File_1"]
input2 = 4
print(find_latest_version(input1, input2)) 
