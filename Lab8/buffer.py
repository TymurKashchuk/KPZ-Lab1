class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *args):
        for x in args:
            if isinstance(x, (int, float)):
                self.data.append(x)
                if len(self.data) >= 5:
                    result = sum(self.data[:5])
                    self.data = self.data[5:]
                    return result
        return None

    def get_current_part(self):
        return self.data[:]