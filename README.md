# TextSummarization
Latent Dirichlet Allocation

Scores:

| ROUGE | Precision | Recall | F-Measure |
| ------------- | ------------- | ------------- | ------------- |
| ROUGE-2 | 0.48919 | 0.11052 | 0.18030 |
| ROUGE-L | 0.93560 | 0.21138 | 0.34485 |

# Data
Sample data can be found in ./example_data

# Installation
Python 3.8 was tested.
It is recommended to create the virtual environment and install dependencies in it:

    python3.8 -m vevn venv
    source venv/bin/activate
    pip install -r requirements.txt

# Running
The main script is example.py. You can run it simply by typing:

    python example.py
   
It should print the following:

    TopicModel::Init
    Done
    Loading regulations and comments..
    Done
    Building TopicModel
    
    number of low frequency tokens pruned = 11,980
    min_word_count = 20, top_most_common_words = 10
    number of high frequency tokens pruned = 10
    tokens = 3,400 rows
    text pre-processing is complete
    
    computing LDA...
    computing dominant topics...
    Done

And after this, the trained model will be used to summarize documents.
Here is one example:

I love Sea World, my wife a 3 kids love seeing sea animals up close.
I would love to continue going to sea world and watch them change the sea.
We should continue to support them and their efforts to preserve and protect marine mammals.
Please have the regulations based on science so future generations can love and learn about our world as we did.

    Topic 0
    The top 10 terms and corresponding weights are:
     * dolphin (0.0269)
     * trainer (0.0159)
     * time (0.0095)
     * facility (0.0087)
     * wa (0.0083)
     * one (0.0078)
     * many (0.0075)
     * environment (0.0072)
     * life (0.0066)
     * experience (0.0065)

Default number of topics is 15, you can change this in the `example.py`
by modifying the following variable:

    num_topics = 15
