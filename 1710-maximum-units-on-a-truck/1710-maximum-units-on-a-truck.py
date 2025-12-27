class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key = lambda x : x[1] , reverse = True)
        total_num_boxes = 0 
        num_units = 0
        for (num_box , num_units_per_box) in boxTypes:
            if (total_num_boxes == truckSize):
                return num_units
            if (total_num_boxes + num_box) < truckSize:
                total_num_boxes+=num_box
                num_units+=(num_box * num_units_per_box)
            elif (total_num_boxes < truckSize):
                extra_required = truckSize - total_num_boxes 
                total_num_boxes+=extra_required 
                num_units+=(num_units_per_box * extra_required)
        
        return num_units
            


"""
[1 , 3] , [2 , 2] , [3 , 1]
"""