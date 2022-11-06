def get_words(document):
    all_words = []
    seen = set()
    doc = open(document, "r")
    for line in doc:
        words = line.split()
        for word in words:
            if word not in seen:
                seen.add(word)
                all_words.append(word)
    doc.close()
    
    return all_words, len(all_words)

def inverted_index(words, document):
    doc = open(document)
    for lines, line in enumerate(doc):
        pass
    doc.close()
    doc_id_dict = {}
    doc_id = ""
    doc = open(document)
    lines += 1
    for i in range(lines):
        doc_id = "ID " + str((i + 1))
        docwords = str(doc.readline())
        docwords = docwords.strip("\n")
        doc_id_dict.update({doc_id: docwords})
    doc.close()
    dictdeleter =  []
    for doc in doc_id_dict:
        dictdeleter.append(doc)
    index = {}
    for word in words:
        doc_id_list = []
        for doc_id in doc_id_dict:
            if word in doc_id_dict[doc_id]:
                doc_id_list.append(doc_id)
        index.update({word: doc_id_list})
    return index, doc_id_dict, dictdeleter