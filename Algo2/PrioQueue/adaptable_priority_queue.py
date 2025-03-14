class Element(object):
    def __init__(self, priority, item):
        self._priority = int(priority)
        self._element = item

    def __gt__(self, other):
        return self._priority > other._priority

    def __lt__(self, other):
        return self._priority < other._priority

class AdaptablePriorityQueue(object):
    def __init__(self):
        self._list = list()
        self._length = 0
        self._element_map = {}  # Maps elements to their indices in the list

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self._list[index] < self._list[parent_index]:
                # Swap with parent
                self._list[index], self._list[parent_index] = self._list[parent_index], self._list[index]
                # Update the element map
                self._element_map[self._list[index]._element] = index
                self._element_map[self._list[parent_index]._element] = parent_index
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < self._length and self._list[left_child_index] < self._list[smallest]:
                smallest = left_child_index

            if right_child_index < self._length and self._list[right_child_index] < self._list[smallest]:
                smallest = right_child_index

            if smallest != index:
                # Swap with the smallest child
                self._list[index], self._list[smallest] = self._list[smallest], self._list[index]
                # Update the element map
                self._element_map[self._list[index]._element] = index
                self._element_map[self._list[smallest]._element] = smallest
                index = smallest
            else:
                break

    def add(self, priority, item):
        new_element = Element(priority, item)
        self._list.append(new_element)
        self._element_map[item] = self._length
        self._length += 1
        self._bubble_up(self._length - 1)

    def remove_min(self):
        if self._length == 0:
            raise IndexError("Priority queue is empty")
        min_element = self._list[0]
        del self._element_map[min_element._element]
        last_element = self._list.pop()
        self._length -= 1
        if self._length > 0:
            self._list[0] = last_element
            self._element_map[last_element._element] = 0
            self._bubble_down(0)
        return min_element._element

    def min(self):
        if self._length == 0:
            raise IndexError("Priority queue is empty")
        return self._list[0]._element

    def update_priority(self, item, new_priority):
        if item not in self._element_map:
            raise ValueError("Item not found in priority queue")
        index = self._element_map[item]
        old_priority = self._list[index]._priority
        self._list[index]._priority = new_priority
        if new_priority < old_priority:
            self._bubble_up(index)
        else:
            self._bubble_down(index)

    def remove(self, item):
        if item not in self._element_map:
            raise ValueError("Item not found in priority queue")
        index = self._element_map[item]
        del self._element_map[item]
        last_element = self._list.pop()
        self._length -= 1
        if index < self._length:
            self._list[index] = last_element
            self._element_map[last_element._element] = index
            self._bubble_down(index)
            self._bubble_up(index)

    def length(self):
        return self._length

if __name__ == "__main__":
    myPQ = AdaptablePriorityQueue()
    myPQ.add(4, 'Orangutan')
    print(myPQ.min())  # Output: Orangutan
    myPQ.add(2, 'Gorilla')
    print(myPQ.min())  # Output: Gorilla
    myPQ.add(3, 'Monkey')
    myPQ.add(1, 'Human')
    print(myPQ.min())  # Output: Human
    print(myPQ.length())  # Output: 4
    print(myPQ.remove_min())  # Output: Human
    print(myPQ.length())  # Output: 3

    # Update priority example
    myPQ.update_priority('Monkey', 0)
    print(myPQ.min())  # Output: Monkey

    # Remove example
    myPQ.remove('Gorilla')
    print(myPQ.length())  # Output: 2
