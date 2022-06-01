class SparseVector:
    def __init__(self, length):
        self.length = length
        self.elements = {}
        self.v1 = []
        self.v = []
        self.j = []
    def __len__(self):
        return self.length
    def set_pos(self, pos, el):
        self.elements[pos] = el
        #print(self.elements.values())
        return self.elements
    def get_pos(self, pos):
        if self.elements == {}:
            return 0
        else:
            for k, v in self.elements.items():
                return v 
            
            
    def __str__(self):
        for k, v in self.elements.items():
            self.v1 = [0] * (self.length - 1)
            self.v1.insert(k, v)        
        return "SparseVector" + str(self.v1)
    
    def concatenate(self, v2):
        #print(v)
        for k, m in self.elements.items():
            self.j = [0] * (self.length - 1)
            self.j.insert(k, m)
        self.v = (self.j + v2)
        return 'SparseVector' + str(self.v)