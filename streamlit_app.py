import streamlit as st

st.title("Alan Ibo jr Pogi")
st.write(
    "Adobo Recipe: Marinate meat (chicken/pork) in soy sauce, vinegar, garlic, bay leaves, and pepper for 30+ mins, then simmer in the marinade until tender (~30-45 mins). Optional: brown meat first for crispiness, add water if too salty, and serve with rice."
)
import streamlit as st

def calculate(num1, num2, operation):
    """Perform the calculation based on the operation"""
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

def main():
    st.title("Simple Calculator")
    st.write("Perform basic arithmetic operations")
    
    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)
    
    # Operation selection
    operation = st.radio(
        "Select operation",
        ["Add", "Subtract", "Multiply", "Divide"],
        horizontal=True
    )
    
    # Calculate button
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()