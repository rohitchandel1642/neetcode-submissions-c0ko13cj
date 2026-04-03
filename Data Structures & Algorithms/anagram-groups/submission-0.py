class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in strs:
            v = ''.join(sorted(i))
            
            if v in hmap:
                hmap[v].append(i)
            else:
                hmap[v]=[i]
        
        return list(hmap.values())