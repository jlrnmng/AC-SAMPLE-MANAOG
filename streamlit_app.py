import streamlit as st

st.title("Alan Ibo jr Pogi")
st.write(
    """[Verse 1: Daniel Caesar] You don't know babe, when you hold me and kiss me slowly it's the sweetest thing, And it don't change if I had it my way, You would know that you are 
    [Pre-Chorus: Daniel Caesar] You're the coffee that I need in the morning, You're my sunshine in the rain when it's pouring, Won't you give yourself to me, Give it all, oh 
    [Chorus: Daniel Caesar & H.E.R.] I just wanna see, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, oh you're the best part, oh oh oh, You're the best part, oh oh oh, Best part 
    [Verse 2: H.E.R.] It's this sunrise and those brown eyes, yes, You're the one that I desire when we wake up, And then we head out, ooh yeah I just wanna be, just wanna be here with you, oh 
    [Pre-Chorus: H.E.R.] You're my water when I'm stuck in the desert, You're the Tylenol I take when my head hurts, You're the sunshine on my life, Oh, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, then you're the best part, oh oh oh, You're the best part, oh oh oh, Best part"""
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