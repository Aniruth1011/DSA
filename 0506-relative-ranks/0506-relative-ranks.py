import heapq 
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        num = len(score)
        score = [-x for x in score]
        indexed_scores = [(s , i) for i , s in enumerate(score)]
        heapq.heapify(indexed_scores)
        answer = [""] * num
        rank = 1
        while indexed_scores:
            n_scores, idx = heapq.heappop(indexed_scores)
            if rank==1:
                answer[idx] = "Gold Medal"
            elif rank==2:
                answer[idx] = "Silver Medal"
            elif rank == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(rank)
            rank+=1
        return answer