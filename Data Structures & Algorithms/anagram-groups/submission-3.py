class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict=defaultdict(list)

        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]=count[ord(j)-ord('a')]+1
            anagram_dict[tuple(count)].append(i)
        return list(anagram_dict.values())