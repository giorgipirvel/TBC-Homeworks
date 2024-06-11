class Extended(list):
    def __init__(self, *args):
        super().__init__(*args)

    def min(self):
        if not self:
            raise ValueError("List is empty")
        return min(self)
    
    def max(self):
        if not self:
            raise ValueError("List is mepty")
        return max(self)
    
list1 = Extended([22, 334, 321, 4, 54])
print(list1)
print("Min:", list1.min())
print("Max:", list1.max())
