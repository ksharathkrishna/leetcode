class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr

        # Create a sorted version of the array
        sorted_arr = sorted(set(arr))  # Use set to eliminate duplicates

        # Create a mapping of each unique value to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_arr)}

        # Replace each element in the original array with its corresponding rank
        return [rank_map[value] for value in arr]

        