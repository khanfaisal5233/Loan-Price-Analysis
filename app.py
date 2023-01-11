import streamlit as st
import pickle
import  numpy as np
import joblib
import sklearn
import pandas as pd

#gender
gender = st.selectbox(
    'Gender',
     ['Male','Female'])
if gender=='Male':
    gender=1
else:
    gender=0
#married
married = st.selectbox(
    'Are you married?',
     ['Yes','No'])
if married=='Yes':
    married=1
else:
    married=0

#education
education = st.selectbox(
    'Are you graduated',
     ['Yes','No'])
if education=='Yes':
    education=1
else:
    education=0

#self_employed
self_employed = st.selectbox(
    'Are you self-employed?',
     ['Yes','No'])
if self_employed=='Yes':
    self_employed=1
else:
    self_employed=0

#income
income = st.number_input('Enter your income.')

#coincome
coincome = st.number_input('Enter co-applicant income.\n (in dollar)')

#loan_amount
loan_amount = st.number_input('How much loan amount do you want?\n (in dollar)')

#loan_amount
loan_term = st.number_input('Enter loan term\n (months)')

#credit_history
credit_history = st.selectbox(
    'Do have any current loan?',
     ['Yes','No'])
if credit_history=='Yes':
    credit_history=1
else:
    credit_history=0

#property
property = st.selectbox(
    'Are you self-employed?',
     ['Urban', 'Semi-urban', 'Rural'])
if property=='Urban':
    property=2
elif property=='Semi-urban':
    property=1
else:
    property=0



# print loan status
input=np.array([[gender, married, education, self_employed, income, coincome, loan_amount, loan_term, credit_history, property]])
model =joblib.load('model.pkl')
loan_status=model.predict(input)
st.write(loan_status[0])
