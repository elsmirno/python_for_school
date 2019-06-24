import math
# input: list, value_for_searching
def binarySearch(arr_list, search_value):
	if len(arr_list) == 0:
		return -1
	mid_index = math.floor(len(arr_list)/2)
	if arr_list[mid_index] == search_value:
		return mid_index
	elif arr_list[mid_index] > search_value:
		return binarySearch(arr_list[0:mid_index], search_value)
	elif arr_list[mid_index] < search_value:
		return binarySearch(arr_list[mid_index+1:len(arr_list)], search_value)
