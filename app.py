import streamlit as st

st.title("Find the Largest Number")

# Input fields for three numbers
num1 = st.number_input("Number 1:")
num2 = st.number_input("Number 2:")
num3 = st.number_input("Number 3:")

# Find the largest number
max_num = max(num1, num2, num3)

# Display the result
if st.button("Find Largest"):
    st.write(f"The largest number is: {max_num}")
