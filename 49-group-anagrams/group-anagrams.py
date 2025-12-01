class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            temp = "".join(sorted(str))
            if temp in dic:
                dic[temp].append(str)
            else:
                dic[temp] = [str]
        ans = []
        for key in dic.keys():
            ans.append(dic[key])
        return ans

    