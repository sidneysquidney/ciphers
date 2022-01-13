

class MinHeapString:
    #  Min Heap of tuples (string, number) to help with (key, score) sorting
    def __init__(self, heap_limit = 10):
        self.count = 0
        self.heap_list = [None]
        self.max = None
        self.heap_limit = heap_limit
        
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def parent_idx(self, idx):
        return idx // 2
    
    def has_children(self, idx):
        return self.left_child_idx(idx) <= self.count
    
    def smaller_child_idx(self, idx):
        if self.has_children(idx):
            if self.right_child_idx(idx) > self.count:
                return self.left_child_idx(idx)
            else:
                left = self.left_child_idx(idx)
                right = self.right_child_idx(idx)
                if self.heap_list[left][1] < self.heap_list[right][1]:
                    return left
                else:
                    return right 
                
    def add(self, value):      
        if (self.count < self.heap_limit) or (value[1] > self.heap_list[1][1]):
            self.heap_list.append(value) 
            self.count += 1
            self.heapify_up(self.count)
            if not self.max:
                self.max = value
            elif value[1] > self.max[1]:
                self.max = value
            if self.count > self.heap_limit:
                self.remove_min()
                
    def remove_min(self):
        smallest = self.heap_list[1]
        temp = self.heap_list[self.count]
        self.heap_list[1] = temp
        self.heap_list[self.count] = smallest
        self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return smallest
    
    def heapify_up(self, idx):
        while self.parent_idx(idx) > 0:
            parent = self.parent_idx(idx)
            if self.heap_list[parent][1] > self.heap_list[idx][1]:
                temp = self.heap_list[parent]
                self.heap_list[parent] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx = self.parent_idx(idx)
            
    def heapify_down(self):
        idx = 1
        while self.has_children(idx):
            new_index = self.smaller_child_idx(idx)
            if self.heap_list[idx][1] > self.heap_list[self.smaller_child_idx(idx)][1]:
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[self.smaller_child_idx(idx)]
                self.heap_list[self.smaller_child_idx(idx)] = temp
            idx = new_index