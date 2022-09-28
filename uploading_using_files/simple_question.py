import streamlit as st
import pandas as pd
import json

def humble_multiplier(a,b,c):
    return a*b*c

st.title("My Humble Multiplier!!")

a_ = st.number_input("number a:", value = 0.01)
b_ = st.number_input("number b:", value = 0.02)
c_ = st.number_input("number c:", value = 0.03)

df = pd.read_csv('df.csv')

file_type = st.radio("CSV or JSON", ("csv", "json"))

if file_type == "csv":
    if st.button("Calculate"):
        results = humble_multiplier(a_,b_,c_)
        st.metric("Results",value=results)
        data = {"num a": [a_], "num_b":[b_], "num_c":[c_],"results":[results]}
        temp = pd.DataFrame(data)
        st.write(temp)
        df = pd.concat([df,temp], ignore_index=True)
        open('df.csv', 'w').write(df.to_csv())
else:
    if st.button("Calculate"):
        results = humble_multiplier(a_,b_,c_)
        st.metric("Results",value=results)
        data = {"num a": a_, "num_b": b_, "num_c":c_,"results":results}
        json_obj = json.dumps(data, indent=4)
        with open("sample.json", "w") as output:
            output.write(json_obj)


