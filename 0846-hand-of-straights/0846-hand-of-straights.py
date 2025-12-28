from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        num_groups = len(hand)//groupSize 
        group_num = 0 
        hand.sort()
        for i in range(len(hand)):
            char = hand[i]
            if counter[char]>0:
                num = char
                flag = None
                for j in range(groupSize):
                    if not(num+j in counter and counter[num+j] > 0):
                        flag = True
                        return False 
                if flag is None:
                    group_num+=1
                    for i in range(groupSize):
                        counter[char]-=1
                        char+=1 
        
        print(group_num , num_groups)
        if group_num == num_groups:
            return True 
        return False
