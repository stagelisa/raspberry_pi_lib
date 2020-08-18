class a:
    def __init__(self):
        self._a = 1
    
    def _add(self):
        self._a += 1

b = a()
print(b._a)
b._add()
print(b._a)