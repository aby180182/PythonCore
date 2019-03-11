def count_positives_sum_negatives(arr):
    """
    Return an array, where the first element is the count of positives numbers
    and the second element is sum of negative numbers.
    """
    pos_count = 0
    neg_sum = 0
    if arr:
        for i in arr:
            if i > 0:
                pos_count += 1
            else:
                neg_sum += i
        res_list = [pos_count, neg_sum]
        return res_list
    else:
        return []