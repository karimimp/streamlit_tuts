import streamlit as st

st.title("Streamlit First App")
st.write("This is my app!")

# button
st.header("Button")
button1 = st.button("Click")
if button1:
    st.write("You clicked the button.")

# input data
## checkboxes
st.header("Checkbox")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    #st.write(like)
    if like:
        st.write("Thanks!")
    else:
        st.write("That's OK!")

## radio button
st.header("Radio button")
animal =  st.radio("Favorite animal", ("Lion", "Tiger", "Bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")

## select box
st.header("Select Box")
animal2 = st.selectbox("Favorite animal", ("Lion", "Tiger", "Bear"))
button4 = st.button("Submit 2nd Animal")
if button4:
    st.write(animal2)

## multiselect box
st.header("Multiselect Box")
options = st.multiselect("Favorite food?", ["Kebab", "Rice", "Pizza", "Banana"])

button5 = st.button("Print foods")
if button5:
    st.write(options)

## numerical data
st.header("Slider")
ep = st.slider("How many epochs?", 1, 100)
if st.button("Slider Button"):
    st.write(ep)

## text input
st.header("Text Input ")
user_text = st.text_input("Favorite movie?", "Forest Gump")
if st.button("Text Button"):
    st.write(user_text)

## input numerical using number input
user_num = st.number_input("Favorite number?")
if st.button("User Number"):
    st.write(user_num)


def run_sentiment_analysis(txt):
    st.write(f"Analysis Done! {txt}")

txt = st.text_area('Text to analyze', 'If this is the first time Streamlit has seen these four components with these exact values and in this exact combination and order, it runs the function and stores the result in a local cache. Then, next time the cached function is called, if none of these components changed, Streamlit will skip executing the function altogether and, instead, return the output previously stored in the cache.')
st.write('Sentiment:', run_sentiment_analysis(txt))








