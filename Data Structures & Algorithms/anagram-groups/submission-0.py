class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strsdict = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in strsdict:
                strsdict[key] = []
            strsdict[key].append(word)
        return list(strsdict.values())
           


        
    


        

        