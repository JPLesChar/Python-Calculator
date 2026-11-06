import streamlit as st

st.title("🧮 JP's Calculator")

num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number", value=0.0)

operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2

    elif operation == "Divide":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            st.stop()

        result = num1 / num2

    st.success(f"Result: {result}")


    