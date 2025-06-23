class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers=[]
        hashMaps={}
        for s in strs:
            array= list(s)
            array.sort()
            sorted_array="".join(array)
            if sorted_array not in hashMaps:
                hashMaps[sorted_array]=[]    
            hashMaps[sorted_array].append(s)
        return list(hashMaps.values())