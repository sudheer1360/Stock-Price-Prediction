import streamlit as st 
import pickle

model=pickle.load(open('model.pkl','rb'))

st.title("Stock Price Prediction")

H=st.text_input('Enter the High value:')
L=st.text_input('Enter the Low value: ')
O=st.text_input('Enter the Open value:')
V=st.text_input('Enter the volume values:')


if st.button('Predict'):
    H=float(H)
    L=float(L)
    O=float(O)
    V=float(L)

    data=[[H,L,O,V]]
    result=model.predict(data)
    st.success(result)
    st.write('Closing of Stock Value')