def LCS(s1, s2):
    common_substring = ""
    max_length = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
                k += 1

            if k > max_length:
                max_length = k
                common_substring = s1[i:i + k]

    return common_substring


print(LCS("ingenious", "intelligent")) 
print(LCS("philosophically", "zoophilous"))  
print(LCS("intelligent", "inconsidered")) 
print(LCS("russian", "ukrainian")) 
print(LCS("war", "love"))
print(LCS("romanian", "roman"))
