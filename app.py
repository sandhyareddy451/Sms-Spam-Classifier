import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def text_transformation(text):

    text = text.lower()  # converts text to lowercase
    text = nltk.word_tokenize(text)  # converts lower case text into list of words

    y = []
    for i in text:
        if i.isalnum():  # Removing special characters
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:  # removing stopwords and punctuations
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


vector = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS- Spam Classifier")
input_sms = st.text_area("Enter the message")

st.button('predict')

#data Processing
transformed_sms = text_transformation(input_sms)
#vectorize
vector_input = tfidf.transform([transformed_sms])
#predicting model
result = model.predict(vector_input)[0]
#display
if result == 1:
    st.header('Spam')
else:
    st.header('Not Spam')
