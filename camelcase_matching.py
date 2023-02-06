class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ## T.C = O(k.(n+m))
        ## S.C = O(1)

        res = []
        p_len = len(pattern)

        for q in queries:
            j = 0
            matched = False

            for i in range(len(q)):
                if j < p_len and q[i] == pattern[j]:
                    j += 1
                    if j == p_len:
                        matched = True
                elif ord(q[i]) >= ord('A') and ord(q[i]) <= ord('Z'):
                    matched = False
                    break
            
            res.append(matched)
        
        return res