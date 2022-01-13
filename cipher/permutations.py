# gets permutations from a string or list, returns all possible permutations
# eg 123 - 123,132, 231, 213, 312, 321
class Permutations:
    def __init__(self):
        self.result = []
        
    def permute(self, lst):
        self.backtrack(lst, [])
        return self.result
    
    def backtrack(self, lst, path):
        if not lst:
            self.result.append(path)
        for x in range(len(lst)):
            self.backtrack(lst[:x] + lst[x + 1:], path + [lst[x]])

# gets permutations from a string or list, returns all possible permutations of length n, repeats allowed
# eg 123, n = 2 - 11, 12, 13, 21, 22, 23, 31, 32, 33
# this is also a helper function to create a dictionary of ngrams
class Permutations2:
    def __init__(self, n = 1):
        self.result = []
        self.n = n
    def permute(self, lst):
        self.backtrack(lst, [])
        return self.result
    def backtrack(self, lst, path):
        if len(path) == self.n:
            self.result.append(path)           
        for x in range(len(lst)):
            if len(path) == self.n:
                continue
            self.backtrack(lst, path + [lst[x]])