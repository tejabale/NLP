from transformers import pipeline
from googletrans import Translator
import streamlit as st
import warnings

#pip install googletrans==3.1.0a0

warnings.filterwarnings("ignore")

model_checkpoint = "tejabale/bert-finetuned-squad3"
question_answerer = pipeline("question-answering", model=model_checkpoint)


def predict(Context, Context_Language, Question, Question_Language):
    if Context_Language == "Telugu":
        translator = Translator()
        translated_context = translator.translate(
            Context, src='te', dest='en').text

    elif Context_Language == "Hindi":
        translator = Translator()
        translated_context = translator.translate(
            Context, src='hi', dest='en').text

    else:
        translated_context = Context

    if Question_Language == "Telugu":
        translator = Translator()
        text_to_translate = translator.translate(Question, src='te', dest='en')
        translated = text_to_translate.text
        ans = question_answerer(question=translated, context=translated_context)
        st.write(translated)
        return ans['answer']

    elif Question_Language == "Hindi":
        translator = Translator()
        text_to_translate = translator.translate(Question, src='hi', dest='en')
        translated = text_to_translate.text
        ans = question_answerer(question=translated, context=translated_context)
        st.write(translated)
        return ans['answer']

    else:
        ans = question_answerer(question=Question, context=translated_context)
        st.write("english")
        return ans['answer']


def main():
    st.title("Streamlit Question Answering App")

    context = st.text_area("Enter Context:")
    context_language = st.selectbox("Select Context Language:", ["Telugu", "Hindi", "English"])

    question = st.text_area("Enter Question:")
    question_language = st.selectbox("Select Question Language:", ["Telugu", "Hindi", "English"])

    if st.button("Predict Answer"):
        answer = predict(context, context_language, question, question_language)
        st.success(f"Answer: {answer}")


if __name__ == "__main__":
    main()
