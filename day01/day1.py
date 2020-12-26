def get_input():
    with open('d1_input.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

def find_pair(nums):
    nums.sort()
    for num_1 in nums:
        for num_2 in nums:
            if num_1 + num_2 == 2020:
                return num_1, num_2

def find_triplet_prod(nums):
    nums.sort()
    for num_1 in nums:
        for num_2 in nums:
            for num_3 in nums:
                if num_1 + num_2 + num_3 == 2020:
                    return num_1 * num_2 * num_3


if __name__ == "__main__":
    nums = get_input()
    print(find_triplet_prod(nums))