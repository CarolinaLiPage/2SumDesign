from collections import defaultdict
class TwoSum:

    def __init__(self):
        # ini: empty list
        self.numbers = []
        # ini: empty defaultdict to count occurrences of each number
        self. count = defaultdict(int)

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # add num to the list called numbers
        self.numbers.append(number)
        # uopn adding, meaning the count of this num ++
        self.count[number] += 1


    # O(n^2)
    def find(self, value):
        # create a list of keys to iterate over
        keys = list(self.count.keys())
        cts = list(self.count.values())
        print(keys)
        print(cts)
        for num in keys:
            diff = value - num
            if num != diff and self.count[diff] > 0:
                return True
            if num == diff and self.count == 2:
                return True
        return False

    # To improve bigO, use hashmap in find()
    # can also sort list first, then find. Consider insertion sort