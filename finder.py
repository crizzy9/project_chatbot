
class Finder:

    def __init__(self, index):
        self.index = index

    def search(self, query):
        keywords = query.split(' ')
        docs = []
        for keyword in keywords:
            if keyword in self.index.keys():
                for entry in self.index[keyword]:
                    if entry[0] not in docs:
                        docs.append(entry[0])
        # maintain count to get best match
        print(docs)
