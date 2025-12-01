import streamlit as st
from calculator import calculate

st.title("Simple Calculator")

expression = st.text_input("Enter an expression", "")

if st.button("Calculate"):
    if expression:
        try:
            result = calculate(expression)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception:
            st.error("An unexpected error occurred.")
    else:
        st.warning("Please enter an expression.")
