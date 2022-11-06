import DocRead, Vectors

every_word, dictlength = DocRead.get_words("docs.txt")

print("Words in dictionary:", dictlength)
invertedindex, doclist, doclistid = DocRead.inverted_index(every_word, "docs.txt")
queriesdoc = open("queries.txt", "r")
for lines, line in enumerate(queriesdoc):
        pass
queriesdoc.close
queriesdoc = open("queries.txt", "r")
querieslist = []
lines += 1
for i in range(lines):
    queriestext = str(queriesdoc.readline())
    queriestext = queriestext.strip("\n")
    querieslist.append(queriestext)

for query in querieslist:
    print("Query:", query)
    list_of_document_ids = Vectors.relevant_docs(query, doclist, doclistid)
    if len(list_of_document_ids) == 0:
        print("Relevant documents:")
    else:
        print("Relevant documents:", ' '.join(list_of_document_ids))
    vectorslist = Vectors.find_vector(list_of_document_ids, doclist, query, every_word)
    
    for vector in vectorslist:
        print(vector, "angle is:", vectorslist[vector])