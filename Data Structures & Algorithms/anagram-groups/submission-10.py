class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            lm=[0]*26
            for j in i:
             
                lm[ord(j)-ord('a')]+=1
           
            anagrams[tuple(lm)].append(i)
        return list(anagrams.values())
                