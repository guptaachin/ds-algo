class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        spl_1 = [int(x) for x in version1.split(".")]
        spl_2 = [int(x) for x in version2.split(".")]
        p1, p2 = 0, 0
        while p1 < len(spl_1) and p2 < len(spl_2):
            if spl_1[p1] > spl_2[p2]:
                return 1
            elif spl_1[p1] < spl_2[p2]:
                return -1
            p1 += 1
            p2 += 1
        if p1 < len(spl_1):
            if sum(spl_1[p1:]) > 0:
                return 1
        elif p2 < len(spl_2):
            if sum(spl_2[p2:]) > 0:
                return -1
        return 0
        
