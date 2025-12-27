class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        j = 0 
        num_apples = sum(apple)
        print(capacity)
        while num_apples > 0 :
            num_apples-=capacity[j]
            j+=1 
            #print(f"Box : {j} , {num_apples} remaining , j = {j} ")
        return j
            