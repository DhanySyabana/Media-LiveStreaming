import json

class TypeDataConverter:

    def __init__(self, data) -> None:
        self.data = data
        super().__init__()

    def dict_to_binary(self):
        str = json.dumps(self.data)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary
    
    def binary_to_dict(self):
        jsn = ''.join(chr(int(x, 2)) for x in self.data.split())
        d = json.loads(jsn)  
        return d