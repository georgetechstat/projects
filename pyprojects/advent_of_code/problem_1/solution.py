import sys, os
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    m = f.readlines()

def solve(seq):
    sequences = seq
    nums: str = "123456789"
    nums_int: list[int] = []
    total = 0
    temp_str = ""

    for sequence in sequences:
        for ch in sequence:
            if total < 2:
                if ch in nums:
                    total += 1
                    temp_str += ch
            else:
                total = 0
        nums_int.append(int(temp_str[0] + temp_str[-1]))
        temp_str = ""

    return sum(nums_int)

print(solve(m))
