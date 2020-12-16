from tqdm import tqdm

def part_1(start_nums):
    last_seen = {}
    time = 1
    
    prev_num = start_nums[0]
    for num in start_nums:
        last_seen[num] = [time]
        prev_num = num
        #print(f'Number {time}: {num}')
        time += 1

    with tqdm(total=30000000) as pbar:
        while time <= 30000000:
            # Generate new num
            seen = last_seen[prev_num]
            if len(seen) == 1:
                new_num = 0
            else:
                new_num = seen[1] - seen[0]

            #print(f'Number {time}: {new_num}')
            # add to dictionary
            if new_num in last_seen:
                last_seen[new_num].append(time)
                last_seen[new_num] = last_seen[new_num][-2:]
            else:
                last_seen[new_num] = [time]
            time += 1
            prev_num = new_num
            pbar.update(1)

    return prev_num

if __name__ == "__main__":
    nums = [5,1,9,18,13,8,0]
    #nums = [0, 3, 6]
    print(part_1(nums))