class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        i = 0 
        while i < len(flowerbed):
            print(i)
            if n == 0:
                return True 
            if flowerbed[i] == 1:
                i+=2 
            elif flowerbed[i] == 0:
                if i>0 and i<len(flowerbed)-1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                        i+=2
                    else:
                        i+=1 
                elif i == 0:
                    if len(flowerbed) == 1:
                        i+=2
                        n-=1
                    elif flowerbed[i+1] == 1:
                        i+=1
                    else:
                        flowerbed[i] = 1
                        n-=1
                        i+=2
                elif i==len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n-=1
                        i+=2
                    else:
                        i+=1
        
        if n>0:
            return False
        return True
                