class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        len1 = len(word1)
        len2 = len(word2)
        shortest = min(len1, len2)
        for i in range(shortest ):
            merged += word1[i] + word2[i]
        merged += word1[shortest:] + word2[shortest:]
        return merged
    
class Solution2(object):
    def mergeAlternately2(self, word1, word2):
        i = 0
        

        while i < len(word1) and i < len(word2):
            merged += word1[i]
            merged += word2[i]
            i += 1 

        merged += word1[i:] 
        merged += word2[i:] 
        
        return merged

word1 = "ab"
word2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word1, word2))
