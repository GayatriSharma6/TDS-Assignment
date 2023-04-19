!pip install streamlit
import streamlit as st

def get_greatest(x1,x2,x3):
     if x1 >= x2 and x1 >= x3:
        return x1
     elif x2 >= x1 and x2 >= x3:
        return x2
     else:
        return x3
st.title("Greatest Num")
x1 = st.number_input("Enter first number")
x2 = st.number_input("Enter second number")
x3 = st.number_input("Enter third number")

if st.button("Greatest Num"):
    greatest = get_greatest(x1,x2,x3)
    st.write("Greatest Number is:", greatest)
    
!streamlit run /usr/local/lib/python3.9/dist-packages/ipykernel_launcher.py    
