import streamlit as st

st.title("Alan Ibo jr Pogi")
st.write(
    """[Verse 1: Daniel Caesar] You don't know babe, when you hold me and kiss me slowly it's the sweetest thing, And it don't change if I had it my way, You would know that you are 
    [Pre-Chorus: Daniel Caesar] You're the coffee that I need in the morning, You're my sunshine in the rain when it's pouring, Won't you give yourself to me, Give it all, oh 
    [Chorus: Daniel Caesar & H.E.R.] I just wanna see, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, oh you're the best part, oh oh oh, You're the best part, oh oh oh, Best part 
    [Verse 2: H.E.R.] It's this sunrise and those brown eyes, yes, You're the one that I desire when we wake up, And then we head out, ooh yeah I just wanna be, just wanna be here with you, oh 
    [Pre-Chorus: H.E.R.] You're my water when I'm stuck in the desert, You're the Tylenol I take when my head hurts, You're the sunshine on my life, Oh, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, then you're the best part, oh oh oh, You're the best part, oh oh oh, Best part"""
)

import math

def calculate():
    try:
        if st.session_state.operation == "=":
            st.session_state.result = eval(st.session_state.equation)
            st.session_state.equation = str(st.session_state.result)
        elif st.session_state.operation == "C":
            st.session_state.equation = ""
            st.session_state.result = 0
        elif st.session_state.operation == "⌫":
            st.session_state.equation = st.session_state.equation[:-1]
        elif st.session_state.operation == "M+":
            st.session_state.memory += eval(st.session_state.equation)
        elif st.session_state.operation == "M-":
            st.session_state.memory -= eval(st.session_state.equation)
        elif st.session_state.operation == "MR":
            st.session_state.equation += str(st.session_state.memory)
        elif st.session_state.operation == "MC":
            st.session_state.memory = 0
        else:
            st.session_state.equation += st.session_state.operation
    except:
        st.session_state.equation = "Error"

# Initialize session state
if "equation" not in st.session_state:
    st.session_state.equation = ""
    st.session_state.result = 0
    st.session_state.memory = 0

# UI Layout
st.title("🔬 Scientific Calculator")
st.write("---")

# Display
st.text_input("", st.session_state.equation, key="display", disabled=True)

# Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=calculate, kwargs={"operation": "7"})
    st.button("4", on_click=calculate, kwargs={"operation": "4"})
    st.button("1", on_click=calculate, kwargs={"operation": "1"})
    st.button("π", on_click=calculate, kwargs={"operation": "math.pi"})
    st.button("sin", on_click=calculate, kwargs={"operation": "math.sin("})

with col2:
    st.button("8", on_click=calculate, kwargs={"operation": "8"})
    st.button("5", on_click=calculate, kwargs={"operation": "5"})
    st.button("2", on_click=calculate, kwargs={"operation": "2"})
    st.button("e", on_click=calculate, kwargs={"operation": "math.e"})
    st.button("cos", on_click=calculate, kwargs={"operation": "math.cos("})

with col3:
    st.button("9", on_click=calculate, kwargs={"operation": "9"})
    st.button("6", on_click=calculate, kwargs={"operation": "6"})
    st.button("3", on_click=calculate, kwargs={"operation": "3"})
    st.button("√", on_click=calculate, kwargs={"operation": "math.sqrt("})
    st.button("tan", on_click=calculate, kwargs={"operation": "math.tan("})

with col4:
    st.button("C", on_click=calculate, kwargs={"operation": "C"})
    st.button("0", on_click=calculate, kwargs={"operation": "0"})
    st.button(".", on_click=calculate, kwargs={"operation": "."})
    st.button("^", on_click=calculate, kwargs={"operation": "**"})
    st.button("log", on_click=calculate, kwargs={"operation": "math.log10("})

# Memory Functions
st.write("---")
st.write("**Memory Functions**")
mcol1, mcol2, mcol3, mcol4 = st.columns(4)
with mcol1:
    st.button("M+", on_click=calculate, kwargs={"operation": "M+"})
with mcol2:
    st.button("M-", on_click=calculate, kwargs={"operation": "M-"})
with mcol3:
    st.button("MR", on_click=calculate, kwargs={"operation": "MR"})
with mcol4:
    st.button("MC", on_click=calculate, kwargs={"operation": "MC"})

st.write(f"Memory: {st.session_state.memory}")