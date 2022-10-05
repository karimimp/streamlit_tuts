import streamlit as st
import pandas as pd
import json
from io import StringIO

def humble_multiplier(a,b,c):
    return a*b*c

st.title("Multiplier!")

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
    dataframe = pd.read_csv(user_file)
    # st.write(dataframe)
    a = dataframe["num_a"]
    b = a*10
    st.write(f"My number is {b[0]}")


