from tqdm import trange

class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class CircularLinkedList:
    def __init__(self, items):
        self.node_map = {}
        self.current_node = Node(items[0])
        self.node_map[self.current_node.value] = self.current_node
        self.max_value = max(items)
        past = self.current_node
        for item in items[1:]:
            node = Node(item)
            self.node_map[item] = node
            past.next = node
            node.prev = past
            past = node
        
        past.next = self.current_node
        self.current_node.prev = past
    
    def __str__(self):
        s = ''
        s += f'({str(self.current_node.value)})'
        pos = self.current_node.next
        while pos != self.current_node:
            s += f' {pos.value}'
            pos = pos.next

        return s

    def find(self, value):
        return self.node_map[value]


    def move(self):
        # Trim the group out
        group_start = self.current_node.next
        group_start.prev = None
        group_end = group_start.next.next
        group = [group_start, group_start.next, group_start.next.next]

        self.current_node.next = group_end.next
        group_end.next.prev = self.current_node

        group_end.next = None

        # Look for the target
        target_value = ((self.current_node.value - 2) % self.max_value) + 1
        target = self.find(target_value)
        while target in group:
            target_value = ((target_value - 2) % self.max_value) + 1
            target = self.find(target_value)


        # Splice in the group
        target_end = target.next
        group_start.prev = target
        target.next = group_start
        group_end.next = target_end
        target_end.prev = group_end

        self.current_node = self.current_node.next

def part_1():
    clist = CircularLinkedList([5, 8, 6, 4, 3, 9, 1, 7, 2])

    for _ in range(100):
        clist.move()

    one_node = clist.find(1)
    s = ''
    current_node = one_node.next
    while current_node != one_node:
        s += str(current_node.value)
        current_node = current_node.next

    return s

def part_2():
    #nums = [3,8,9,1,2,5,4,6,7]
    nums = [5, 8, 6, 4, 3, 9, 1, 7, 2]
    nums.extend(range(10, 1000001))
    clist = CircularLinkedList(nums)

    for _ in trange(10000000):
        clist.move()

    one_node = clist.node_map[1]
    return one_node.next.value * one_node.next.next.value
        
if __name__ == "__main__":
    print(part_1())
    print(part_2())

