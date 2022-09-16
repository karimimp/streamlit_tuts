import streamlit as st
import spacy

# caching the model
@st.cache(allow_output_mutation=True)
def load_model(model_name):
    nlp = spacy.load(model_name)
    return (nlp)

nlp = load_model("en_core_web_lg")




def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))

    return (results)

st.title("Tutorial on Forms")

form1 = st.sidebar.form(key="Options" )

form1.header("Parameters")
ent_types = form1.multiselect("Select the entity to extract", ["PERSON", "ORG", "GPE"])
form1.form_submit_button("Click Me")

text = st.text_area("Text Sample", "James enjoys playing basketball in Florida for the Salvation Army.")
hits = extract_entities(ent_types, text)
st.write(hits)