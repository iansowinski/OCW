# ############
# Peek finding

peak_array = [1,1,1,2,5,7,12,12,13,19,23,35,36,77,79,84,94,100,111,90,33,31,22,21,17,14,11,5,2,1]

def find_peak(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    middle = (len(array)-1)/2
    if array[middle+1] < array[middle]:
        return find_peak(array[0:middle+1])
    else:
        return find_peak(array[middle:len(array)])

# print(find_peak(peak_array))

# ###############
# 2d peak finding

peak_array = [[1,2,3,4],
              [2,3,4,5],
              [3,4,5,6],
              [6,7,7,8]]

def find_peak_2d(array):
    print(len(array))
    if len(array) == 1:
        return find_peak(array)
    elif len(array) == 2:
        if find_peak(array[0]) > find_peak(array[1]):
            return find_peak(array[0])
        else:
            return find_peak(array[1])
    middle = (len(array)-1)/2
    global_max_val = find_peak(array[middle])
    index = array[middle].index(global_max_val)
    if array[middle-1][index] > array[middle][index]:
        return find_peak_2d(array[0:middle])
    elif array[middle][index] < array[middle+1][index]:
        return find_peak_2d(array[middle+1:len(array)])
    else:
        return find_peak(array[0])

print(find_peak_2d(peak_array))
