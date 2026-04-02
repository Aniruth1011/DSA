class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.small_count = 0 
        self.med_count = 0 
        self.large_count = 0 

        self.small_size= small 
        self.med_size = medium 
        self.large_size = big
        

    def addCar(self, carType: int) -> bool:
        if carType == 3:
            if self.small_count>=self.small_size:
                return False
            else:
                self.small_count+=1

                return True 
        elif carType == 2:
            if self.med_count>=self.med_size:
                return False
            else:
                self.med_count+=1
                return True 
        elif carType == 1:
            if self.large_count>=self.large_size:
                return False
            else:
                self.large_count+=1
                return True 


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)