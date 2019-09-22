#%%
import flask
from flask import Flask,request
from callAPI import Wordpreprocess

preprocess_app=Flask(__name__)
word_process_obj=Wordpreprocess()

@preprocess_app.route('/home')
def test_api():
    return 'API is working'

@preprocess_app.route('/stopwords',methods=['POST']) #endpoint in url
def top_words_api():
    text=json.loads(request.data.decode())['text']
    top_words=word_process_obj.top_words(text)
    return str(top_words)


#%%
if __name__=='__main__':
    preprocess_app.run(host='0.0.0.0',port='8080')

#%%
