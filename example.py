import pickle
from topicModel import TopicModel
from documentSummaries import DocumentSummaries

def getFederalDockets():
    dockets = ['APHIS-2006-0044','CPSC-2012-0050', 
               'APHIS-2006-0085', 'APHIS-2009-0017']
    return dockets

def getComments():
    regulations = dict()
    comments = list()
    dockets = getFederalDockets()
    for docket in dockets:
        file_name = 'example_data/' + docket + '.pickle'
        cmts = pickle.load(open(file_name, 'rb'))
        regulations[docket] = cmts
        comments.extend(cmts)
    return regulations, comments


num_topics = 15

if __name__ == "__main__":
    print("Loading regulations and comments..")
    
    regulations, comments = getComments()

    print("Done")
 
    #print(regulations)
    
    print("Building TopicModel")
    topicModel = TopicModel(num_topics)
    topicModel.fit(comments)
    print("Done")


    print("Summarizing documents")
    for docket_id, document in regulations.items():
        docSummaries = DocumentSummaries(topicModel, num_dominant_topics=3, number_of_sentences=4)
        docSummaries.summarize(document)
        print(docket_id)
        docSummaries.display()


    print("Done")
