class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for _ in numbers:
            if target-_ in numbers:
                if target-_==_:
                    return [numbers.index(_)+1,numbers.index(_,numbers.index(_)+1)+1]
                else:
                    return [numbers.index(_)+1,numbers.index(target-_)+1]