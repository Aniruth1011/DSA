class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        start_station = 0
        total = 0
        for i in range(n):
            net = gas[i] - cost[i]
            total+=net
            tank+=net 

            if tank<0:
                start_station = i+1
                tank = 0 
        
        if total>=0:
            return start_station 
        return -1