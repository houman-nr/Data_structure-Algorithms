#arr[(k - 1)/2] will return the parent node

#arr[(2*k) + 1] will return left child

#arr[(2*k) + 2] will return right child


#this is where the heap is written which is used to maximize the elements of the queue
class heap:
    heap = []

    def __init__(self, array) -> None:
        if len(array) > 3:
            self.heap = array
            n = int((len(array)//2)-1)
            for k in range(n, -1, -1):
                self.maximize(k)
            print(self.heap)
        else:
            return "tree is not created yet"

    def maximize(self, k):
        largest = self.heap[k]
        l = self.left(k)
        r = self.right(k)
        swap_index = 0

        if l < int(len(self.heap)) and self.heap[l] > largest:
            largest = self.heap[l]
            swap_index = l
        if r < int(len(self.heap)) and self.heap[r] > largest:
            largest = self.heap[r]
            swap_index = r

        if largest != self.heap[k]:
            self.heap[k] ,self.heap[swap_index] = self.heap[swap_index], self.heap[k]
            self.maximize(k)


    #this fucntion was made to find the index of the left leaf of a branch
    def left(self, number):
        print(number * 2 + 1)
        return (number * 2) + 1

    #this fucntion was made to find the index of the right leaf of a branch
    def right(self, number):
        print(number * 2 + 2)
        return (number * 2) + 2

    def addElement(self, number):
        pass

    def popElement(self):
        pass

    def isEmpty(self):
        pass
#this is where the heap is written which is used to maximize the elements of the queue


if __name__ == "__main__":
    test_array = [1, 5, 12, 2, 4, 8]
    heap_object = heap(test_array)