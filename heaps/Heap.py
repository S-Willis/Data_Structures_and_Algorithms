import math

class Heap:
    def __init__(self,array):
        self.heap = array
        self.maximum = array[0]
        self.heapsize = len(self.heap)

    # def display_heap(self):
    #     layers = floor(log2(self.heapsize))
    #     maxspaces = 5*(2**layers)+(2**layers-1)
    #     heap_read_in = self.heap
    #     for i in range(layers):
    #         num_in_layer = 2**i
    #
    #     return

    def heap_maximum(self):
        return self.maximum

    def update_max(self):
        self.maximum = self.heap[0]

    def max_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if(l<len(self.heap) and self.heap[l] > self.heap[i]):
            largest = l
        if(r<len(self.heap) and self.heap[r] > self.heap[largest]):
            largest = r
        if largest != i:
            hold = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = hold
            self.max_heapify(largest)

        self.update_max()
        return

    def heap_extract_max(self):
        heapmax = self.maximum
        self.heap[0] = self.heap[self.heapsize-1]
        del self.heap[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.max_heapify(0)
        self.update_max()
        return heapmax

    def get_Parent_idx(self,index):

        parent_idx = None

        if(index==0):
            return 0
        if(index%2 == 0):
            parent_idx = int((index-2)/2)
        else:
            parent_idx = int((index-1)/2)

        return parent_idx

    def max_heap_insert(self,k):
        self.heapsize = self.heapsize + 1
        self.heap.append(k)
        j = self.heapsize-1
        while(j!=0 and self.heap[j]>self.heap[self.get_Parent_idx(j)]):
            hold = self.heap[j]
            self.heap[j] = self.heap[self.get_Parent_idx(j)]
            self.heap[self.get_Parent_idx(j)] = hold
            j = self.get_Parent_idx(j)
        return


    def build_max_heap(self):
        for i in range(math.floor(len(self.heap)/2),-1,-1):
            self.max_heapify(i)
        return

    # def getLeft(self,node_index):
    #     return self.heap[2*node_index]
    #
    # def getRight(self,node_index):
    #     return self.heap[2*node_index + 1]
