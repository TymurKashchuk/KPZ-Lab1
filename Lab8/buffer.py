from config import BUFFER_SIZE

class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *args):
        for x in args:
            if isinstance(x, (int, float)):
                self.data.append(x)
                if len(self.data) >= BUFFER_SIZE:
                    result = sum(self.data[:BUFFER_SIZE])
                    self.data = self.data[BUFFER_SIZE:]
                    return result
        return None

    def get_current_part(self):
        return self.data[:]