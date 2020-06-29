import unittest, Heap, math

class HeapTests(unittest.TestCase):

    def setUp(self):
        self.Heap = Heap.Heap([13,2,16,9,4,16,17,30,8,45,17,88])

    def test_buildMaxHeap(self):
        self.Heap.build_max_heap()
        for i in range(math.floor(self.Heap.heapsize/2)-1):
            self.assertTrue(self.Heap.heap[i] >= self.Heap.heap[2*i+1] and self.Heap.heap[i] >= self.Heap.heap[2*i + 2], 'false at ' + str(i))


if __name__ == '__main__':
    unittest.main()
