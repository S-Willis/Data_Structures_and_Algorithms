from Heap import *

def main():
    # print('Hello!')
    #
    array = [13,2,16,9,4,16,17,30,8,45,17,88]
    #
    # ex_heap = [88,17,45,16,17,30,8,13,2,16,9,4]
    #
    heap1 = Heap(array)
    # print(heap1.heap)
    # print(heap1.heap_maximum())
    heap1.build_max_heap()
    # print(heap1.heap)
    # print(ex_heap)

    heap1.max_heap_insert(48)
    print(heap1.heap)





if __name__ == '__main__':
    main()
