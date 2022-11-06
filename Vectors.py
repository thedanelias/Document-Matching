import numpy as np
import math, collections

def relevant_docs(query, docdict, dictdeleter):
    listdeleter = dictdeleter.copy()
    query = query.strip("\n")
    querylist = []
    querylist.append(query.split(" "))
    
    queryword = ""
    for word in querylist:
        for wordw in word:
            queryword = str(wordw)
            queryword = queryword.strip("['']")
            for doc in listdeleter:
                found = False
                sentencelist = docdict[doc].split()
                for wordword in sentencelist:
                        if queryword in wordword:
                            found = True
                            break
                if found == False:
                    listdeleter.remove(doc)
                
    return listdeleter

def find_vector(doclist, docdict, query, all_words):
    query = query.strip("\n")
    querylist = query.split()

    vectors_angle = {}
    queryarraylist = []

    querylistnodupes = []
    seen = set()

    #removes duplicate words from query to create vector
    for queryword in querylist:
        wordw = str(queryword)
        wordw = wordw.strip("['']")
        if wordw not in seen:
            querylistnodupes.append(wordw)
        else:
            seen.add(wordw)

    for ting in all_words:
        for queryword in querylistnodupes:
            count = 0
            if ting == queryword:
                count += 1
                break
            if count > 1:
                count = 1
        queryarraylist.append(count)
    
    queryarray = np.array(queryarraylist)
    for doc in doclist:
        sentencelist = docdict[doc].split()
        docarraylist = []
        for ting in all_words:
            count = 0
            for word in sentencelist:
                if word == ting:
                    count += 1
            docarraylist.append(count)

        docarray = np.array(docarraylist)
        norm_doc = np.linalg.norm(docarray)
        norm_query = np.linalg.norm(queryarray)
        cos_theta = np.dot(queryarray, docarray) / (norm_query * norm_doc)
        theta = math.degrees(math.acos(cos_theta))
        vectors_angle.update({doc: theta})

    sorted_vectors = sorted(vectors_angle.items(), key=lambda kv: kv[1])
    sorted_dict_vectors = collections.OrderedDict(sorted_vectors)
    return sorted_dict_vectors