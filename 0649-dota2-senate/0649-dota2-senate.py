from collections import Counter , deque 
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        queue = deque(senate)
        skipped_r = 0 
        skipped_d = 0
        while queue:
            i = queue.popleft()
            if i=="R":
                if count["D"] == 0:
                    return "Radiant"
                else:
                    if skipped_r>0:
                        skipped_r-=1
                    else:
                        count["D"]-=1 
                        skipped_d+=1 
                        queue.append("R")
            else:
                if count["R"] == 0:
                    return "Dire"
                else:
                    if skipped_d>0:
                        skipped_d-=1
                        continue 
                    else:
                        count["R"]-=1
                        skipped_r+=1
                        queue.append("D")
        
        print(count)
        if count["R"] > count["D"]:
            return "Radiant"
        elif count["D"] > count["R"]:
            return "Dire"
        else:
            if senate[-1] == "R":
                return "Dire"
            else:
                return "Radiant"