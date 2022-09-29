import streamlit as st
import pandas as pd
import json
from io import StringIO

def humble_multiplier(a,b,c):
    return a*b*c

st.title("My Humble Multiplier!!")

a_ = st.number_input("number a:", value = 0.01)
b_ = st.number_input("number b:", value = 0.02)
c_ = st.number_input("number c:", value = 0.03)

# df = pd.read_csv('df.csv')

file_type = st.radio("CSV or JSON", ("csv", "json"))

if file_type == "csv":
    if st.button("Calculate"):
        results = humble_multiplier(a_,b_,c_)
        st.metric("Results",value=results)
        data = {"num_a": [a_], "num_b":[b_], "num_c":[c_],"results":[results]}
        temp = pd.DataFrame(data)
        st.write(temp)
        # df = pd.concat([df,temp], ignore_index=True)
        open('temp.csv', 'w').write(temp.to_csv())
else:
    if st.button("Calculate"):
        results = humble_multiplier(a_,b_,c_)
        st.metric("Results",value=results)
        data = {"num a": a_, "num_b": b_, "num_c":c_,"results":results}
        json_obj = json.dumps(data, indent=4)
        with open("sample.json", "w") as output:
            output.write(json_obj)

user_file = st.file_uploader("Upload Your JSON file", type=["json","csv"])

if user_file is not None:
    # To read file as bytes:
    # bytes_data = user_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(user_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)
    # st.write(string_data[0:10])

    dataframe = pd.read_csv(user_file)
    st.write(dataframe)


