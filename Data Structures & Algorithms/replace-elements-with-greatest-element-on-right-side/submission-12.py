class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mv = arr[-1]
        l = arr[:] 
        for i in range(len(arr)-2, -1, -1):
            mv = max(arr[i+1], mv)
            l[i] = mv
        l[-1] = -1  
        return l  