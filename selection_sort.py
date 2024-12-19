# selection sort has a time complecity of O(n^2)
# it traverses through the array one by one and finds the
# smallest element of the sub array

def find_smallest_index(array):
    """_summary_

    Args:
        array (_type_): subarray for finding smallest index
    """
    try:
        if not array:
            return

        if len(array) == 1:
            return 0

        smallest_index = 0
        for i in range(1, len(array)):
            if array[i] < array[smallest_index]:
                # switch the smallest index
                smallest_index = i
        return smallest_index
    except Exception as ex:
        return str(ex)

def selection_sort(array):
    """_summary_

    Args:
        array (_type_): input array
    """
    try:
        # nothing to sort
        if not array:
            return

        # only one element present nothing to sort
        if len(array) == 1:
            return array

        sorted_array = []

        for _ in range(len(array)):
            smallest_index = find_smallest_index(array)
            sorted_array.append(array.pop(smallest_index))
        return sorted_array

    except Exception as ex:
        return str(ex)
