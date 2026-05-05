class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for word in strs:
            val = []
            for i in range(0, 26):
                val.append(0)

            for c in word:
                ind = ord(c) - 96 - 1
                print(ind)
                val[ind] += 1

            valt = tuple(val)
            if valt in m.keys():
                m[valt].append(word)
            else: 
                m[valt] = [word]
        groups = []
        for k in m.keys():
            groups.append(m[k])

        return groups

        
        

        