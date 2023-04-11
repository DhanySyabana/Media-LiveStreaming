import json

class TypeDataConverter:

    def __init__(self, data) -> None:
        self.data = data
        super().__init__()

    def dict_to_binary(self):
        jsn = json.dumps(self.data)
        bin = ' '.join(format(ord(x), 'b') for x in jsn)
        return bin.encode("utf-8")
    
    def binary_to_dict(self):
        jsn = ''.join(chr(int(x, 2)) for x in self.data.split(' '))
        return json.loads(jsn)