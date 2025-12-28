from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for card in sorted(counter):
            f = counter[card]
            if counter[card] > 0:
                for next_card in range(card , card + groupSize):
                    if counter[next_card] < f:
                        return False 
                    counter[next_card]-=f
        return True
            