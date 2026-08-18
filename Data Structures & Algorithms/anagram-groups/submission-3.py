'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]* 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d={}
        for i in strs:
            s="".join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        return list(d.values())

