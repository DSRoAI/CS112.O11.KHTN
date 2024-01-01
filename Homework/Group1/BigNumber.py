def counting(value, array, idx):  
    if idx > len(array) - 1:
        return int(2e10) 
    if array[idx] >= value:
        return 0
    else:
        next_value = value - array[idx]
        idx += 1
        value -= 1
        return next_value + counting(value , array, idx)      
    
def check(array, value, max_operations):
    i = 0
    while (i < len(array)):
        if counting(value, array, i) <= max_operations:
            return True
        else:
            i += 1
    return False 
                
               
num_testcases = int(input())
i = 0
while i < num_testcases:
    i += 1
    array_size, max_operations = map(int, input().split())
    array = [element for element in map(int, input().split())]
    left_idx, right_idx, temp = 1, int(2e20), 1
    while(1):
        if left_idx > right_idx:
            break
        mid_idx = int((left_idx + right_idx) / 2)
        if check(array, mid_idx, max_operations):
            left_idx = mid_idx + 1
            temp = mid_idx
        else:
            right_idx = mid_idx - 1     
    print(temp)
