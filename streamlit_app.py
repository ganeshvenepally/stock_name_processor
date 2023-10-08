import streamlit as st

def process_stock_names(data):
    lines = data.split("\n")
    stock_names = [line.replace("BSE:", "") + ".BO" for line in lines if "BSE:" in line]
    return ", ".join(stock_names)

st.title('Stock Name Processor')
st.write('Input stock data in the provided format and get processed stock names.')

# User input
data = st.text_area("Enter stock data:")

if st.button('Process Stock Names'):
    processed_names = process_stock_names(data)
    st.write(processed_names)
