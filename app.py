import streamlit as st
from transformers import TranslationPipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("divyanshu-finetuned-hi-en/checkpoint-11644")
model = AutoModelForSeq2SeqLM.from_pretrained("divyanshu-finetuned-hi-en/checkpoint-11644")

st.title("English to Hindi Translation")
en_hi_translator = TranslationPipeline(
    model,
    tokenizer,
)

str = st.text_input("Input String to translate")

if str:
    st.write(en_hi_translator(str)[0]['translation_text'])