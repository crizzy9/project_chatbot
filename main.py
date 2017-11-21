from indexer import Indexer
from finder import Finder

indexer = Indexer()
indexer.create_index()
# print("Index:\n" + str(indexer.get_index()))
print("Indexing done...")

finder = Finder(indexer.get_index())


query = input("Enter the search keyword:")
finder.search(query)