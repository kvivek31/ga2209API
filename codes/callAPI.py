#%%
import flask
import json
from nltk import word_tokenize
import pandas as pd
from flask import request,Flask

app=Flask(__name__)

class Wordpreprocess:
    def __init__(self):
        self.num_of_words=2
    def top_words(self,text):
        word_tokens=word_tokenize(text)
        word_tokens=[word for word in word_tokens if len(word>2)]
        text_df=pd.DataFrame({'words':word_tokens})
        count_dict=dict(text_df.words.value_counts())
        top_words=list(count_dict.values())[:self.num_of_words]
        return top_words
#%%
if __name__=='__main__':
    word_process_obj=Wordpreprocess()
    word_process_obj.num_of_words=3
    text="""The ‘Howdy Modi’ mega event in Houston is the culmination of Prime Minister Narendra Modi’s efforts to cultivate the Indian diaspora. Modi has been wooing the diaspora all over the world and more so in the US. As the Indian-Americans have become more powerful, it is only natural for the prime minister to make use of them and market himself and India.

In fact, it was this secret weapon that Modi has been using successfully to create a positive impact in whichever country he has visited in the past five years. The diaspora, on the other hand, is delighted with Modi for giving them facilities such as relaxation in visa norms, ease of doing business and merging the OCI and PIO cards. Hence, they are looking forward to Modi standing by the side of US President Donald Trump when the two share the dais."""
    top_words=word_process_obj.top_words(text)
    print(top_words)



#%%
