class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(start , path):
            if (start == len(s) ) and  ( len(path)==4 ):
                result.append(".".join(path)) 
            if len(path)>=4:
                return 
            for length in range(1 , 4):
                if (start + length) > len(s):
                    break   
                part_of_ip = s[start:start + length]
                if (part_of_ip[0] == "0" and len(part_of_ip) > 1) or (int(part_of_ip)>255):
                    continue 
                path.append(part_of_ip)
                backtrack(start + length , path)
                path.pop()
        
        backtrack(0 , [])
        return result 


            