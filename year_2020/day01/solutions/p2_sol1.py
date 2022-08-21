
from .common import transform_input

def run (lines: list[str]) -> int:
    nums = transform_input(lines)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                a = nums[i]
                b = nums[j]
                c = 2020 - a - b
                try:
                    c_index = nums.index(c)
                    if c_index != i and c_index != j:
                        return a * b * c
                except:
                    pass
