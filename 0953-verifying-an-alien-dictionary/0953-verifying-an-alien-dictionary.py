class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dic = {c : i for i , c in enumerate(order)}
        for i in range(1 , len(words)):
            word1 , word2 = words[i-1] , words[i]
            if len(word1) == len(word2):
                if word1 == word2:
                    continue
                j = 0 
                while j < len(word1):
                    if word1[j] !=word2[j]:
                        break 
                    j+=1 
                print(j)
                if dic[word2[j]] - dic[word1[j]] <0:
                    return False 

            elif len(word1) < len(word2):
                if word1 == word2[:len(word1)]:
                    continue
                j = 0 
                while j < len(word1):
                    if word1[j]!=word2[j]:
                        break 
                    j+=1 

                if dic[word2[j]] - dic[word1[j]] <0:
                    return False
            else:
                if word2 == word1[:len(word2)]:
                    return False 
                else:
                    j=0 
                    while j<len(word2):
                        if word2[j]!=word1[j]:
                            break 
                        j+=1
                    if dic[word2[j]] - dic[word1[j]] < 0:
                        return False 
        return True     