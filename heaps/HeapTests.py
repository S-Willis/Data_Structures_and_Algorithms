import unittest, Heap, math

class HeapTests(unittest.TestCase):

    def setUp(self):
        self.Heap = Heap.Heap([13,2,16,9,4,16,17,30,8,45,17,88])

    def test_buildMaxHeap(self):
        self.Heap.build_max_heap()
        for i in range(math.floor(self.Heap.heapsize/2)-1):
            self.assertTrue(self.Heap.heap[i] >= self.Heap.heap[2*i+1] and
                            self.Heap.heap[i] >= self.Heap.heap[2*i + 2], 'false at ' + str(i))

    def test_heap_maximum(self):
        self.Heap.build_max_heap()
        self.assertEqual(self.Heap.heap_maximum(), 88)


    def test_heap_extract_max(self):
        self.Heap.build_max_heap()
        result = self.Heap.heap_extract_max()
        self.assertTrue(result == 88, 'returned ' + str(result))
        self.assertTrue(self.Heap.heap_maximum() == 45)

    def test_get_parent_index(self):
        self.Heap.build_max_heap()
        self.assertTrue(self.Heap.get_Parent_idx(1)==0, '1= ' + str(self.Heap.get_Parent_idx(1)))
        self.assertTrue(self.Heap.get_Parent_idx(4)==1, '4= ' + str(self.Heap.get_Parent_idx(4)))
        self.assertTrue(self.Heap.get_Parent_idx(8)==3, '8= ' + str(self.Heap.get_Parent_idx(8)))


if __name__ == '__main__':
    unittest.main()
