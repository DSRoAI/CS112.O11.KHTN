def solution(array):
    if len(array) == 1:
        return 1
    array = sorted(array)
    case_list = []
    # Delete first element
    case_1 = array[1] + array[-1]
    case_list.append(case_1)
    # Delete last element
    case_2 = array[-2] + array[0]
    case_list.append(case_2)
    # Delete any middle element
    case_3 = array[0] + array[-1]
    case_list.append(case_3)
    case_list = sorted(case_list)
    # Iterate each case above
    for case in case_list:
        # Two pointers
        left_idx, right_idx, temp, pass_away = 0, len(array) - 1, 0, 0
        while(1):
            if left_idx > right_idx:
                break
            sum = array[left_idx] + array[right_idx]
            # If sum of left element and right element < case => the left element might be the redundant element
            if sum < case:
                pass_away += 1
                temp = left_idx
                left_idx += 1
            # If sum of left element and right element > case => the right element might be the redundant element
            elif sum > case:
                pass_away += 1
                temp = right_idx
                right_idx -= 1
            # Otherwise, there is no redundant element => just skip
            else:
                left_idx += 1
                right_idx -= 1
        # After iterating all elements in one case, if case - middle element > 0
        if pass_away <= 1:
            # If there is no redundant element, then the redundant element is the middle element itself, so result = case - middle
            if (pass_away == 0) & (case - array[left_idx] > 0):
                return case - array[left_idx]
            # If there is 1 redundant element, result = case - redundant element
            elif case - array[temp] > 0:
                return case - array[temp]
    # Otherwise, there is no answer
    return -1


num_test = int(input()) 

for i in range(num_test):
    N = int(input()) 
    array = list(map(int, input().split())) 
    answer = solution(array)
    if answer <= 0:
        answer = -1
    print(f"Case #{i + 1}: {answer}")
