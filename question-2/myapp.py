import streamlit as st

def reverse_string(s):
    if len(s)<=1:
        return s
    else:
        return reverse_string(s[1:])+s[0]
str=input("Enter the String to reverse")
str1=reverse_string(str)
str1.capitalize()
if st.button("Reverse String"):
    if operation == "reverse":
        result = reverse_string(str)