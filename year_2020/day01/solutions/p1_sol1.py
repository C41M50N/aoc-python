
from .common import transform_input

def run (lines: list[str]) -> int:
    nums = transform_input(lines)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == 2020:
                    return nums[i] * nums[j]
