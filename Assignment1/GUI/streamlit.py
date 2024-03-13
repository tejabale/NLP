import streamlit as st
import pickle
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from transphone import read_tokenizer


@st.cache_data
def load_data():
    with open('rbf_SVM_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model


def remove_last_vowel(text):
    return re.sub(r'[aeiouAEIOU]$', '', text)

def extract_last_three(lst):
    if len(lst) >= 3:
        return lst[-3:]
    else:
        return [None, None, None]

model = load_data()
stemmer = SnowballStemmer('english')
eng = read_tokenizer('eng')

with open('label_encoder.pkl', 'rb') as file:
        label_encoder = pickle.load(file)



def predict_inhabitant_name(city):
    city_stemmed = stemmer.stem(city)
    city_stemmed_ro = remove_last_vowel(city_stemmed)
    phoneme_list = eng.tokenize(city)
    phoneme_ids = eng.convert_tokens_to_ids(phoneme_list)
    last3_ = (extract_last_three(phoneme_ids))
    predicted_label = model.predict([last3_])[0]
    predicted_suffix = label_encoder.inverse_transform([predicted_label])[0]
    predicted_inhabitant = city_stemmed_ro + predicted_suffix
    return predicted_inhabitant

st.title("Inhabitants of cities 🏙")
input = st.text_area('Enter the name of the city', '')

if st.button("Predict"):
    if input:
        prediction = predict_inhabitant_name(input)
        st.write(f"## Predicted Inhabitant name: {prediction}")
    else:
        st.warning("## Please enter the city name for prediction")



