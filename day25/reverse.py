from tqdm import trange

def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject
        value = value % 20201227
    return value

def brute_force_transform(subject, target):
    value = 1
    loops = 0
    while value != target:
        value = value * subject
        value = value % 20201227
        loops += 1
    return loops

def part_1():
    
    # Brute force the card loop secret
    #target = 5764801
    card_pub = 13135480
    door_pub = 8821721
    card_secret = brute_force_transform(7, card_pub)
    door_secret = brute_force_transform(7, door_pub)

    enc_key1 = transform(door_pub, card_secret)
    enc_key2 = transform(card_pub, door_secret)
    assert(enc_key1 == enc_key2)
    return enc_key1

if __name__ == "__main__":
    print(part_1())