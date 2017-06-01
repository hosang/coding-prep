class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rest_to_idx = {rest: i for i, rest in enumerate(list1)}
        min_idx = len(list1) + len(list2)
        argmin = []
        for i, rest in enumerate(list2):
            if rest not in rest_to_idx:
                continue
            idxsum = rest_to_idx[rest] + i
            if idxsum == min_idx:
                argmin.append(rest)
            elif idxsum < min_idx:
                min_idx = idxsum
                argmin = [rest]
        return argmin
