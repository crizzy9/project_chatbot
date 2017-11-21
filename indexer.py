import os


class Indexer:

    def __init__(self):
        self.files = os.listdir('docs')
        self.index = {}

    def create_index(self):
        for file_name in self.files:
            with open('docs/' + file_name, 'r+') as f:
                data = f.read().split('\n')
                question = data[0].split(' ')
                for word in question:
                    if word not in self.index.keys():
                        self.index[word] = [[file_name, 1]]
                    else:
                        found = False
                        for i in self.index[word]:
                            if i[0] == file_name:
                                i[1] += 1
                                found = True
                                break
                        if not found:
                            self.index[word].append([file_name, 1])

    def get_index(self):
        return self.index


indexer = Indexer()
indexer.create_index()
print(indexer.get_index())
