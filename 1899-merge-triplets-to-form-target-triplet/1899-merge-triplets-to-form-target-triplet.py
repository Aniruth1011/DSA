class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a , b,  c = target 

        has_a , has_b , has_c = False,  False , False 
        for (a_ , b_ , c_) in triplets:
            if a_ > a or b_ > b or c_ > c:
                continue 
            if a_ == a:
                has_a = True 
            if b_ == b:
                has_b = True 
            if c_ == c:
                has_c = True 
        
        return has_a and has_b and has_c 
