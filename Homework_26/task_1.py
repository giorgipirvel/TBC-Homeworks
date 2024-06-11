class Inset:
    def __init__(self):
        self.elements = []
    
    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)
    
    def member(self, element):
        return element in self.elements
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("ვერ ვიპოვნე")
    
    def __str__(self):
        return ', '.join(map(str, sorted(self.elements)))

inset = Inset()
inset.insert(23)
inset.insert(32)
inset.insert(43)

print(inset)
print(inset.member(23))
print(inset.member(29))

try:
    inset.remove(29)
except ValueError:
    print("ვერ ვიპოვნე")
