import streamlit as st

#def reverse_string(s):
 #  if len(s)<=1:
  #  return s
   #else:
    #return reverse_string(s[1:])+s[0]
#str=st.text_input("Enter the String to reverse")
#str1=reverse_string(str)

#if st.button("Reverse String"):
    #if operation == "reverse":
     #  result = reverse_string(str)
      # st.write(result) 

import streamlit as st

# Title of the application
st.title('Simple Task Application')

# List of tasks
tasks = [
    "Task 1: Write a report",
    "Task 2: Review code",
    "Task 3: Prepare presentation"
]

# Display a dropdown to select a task
selected_task = st.selectbox("Select Task", tasks)

# Display the selected task
st.write("You selected:", selected_task)

# Optional: Display additional details based on the selected task
if selected_task == tasks[0]:
    st.write("Details for Task 1: Write a report")
    st.write("Deadline: July 20, 2024")
elif selected_task == tasks[1]:
    st.write("Details for Task 2: Review code")
    st.write("Deadline: July 22, 2024")
elif selected_task == tasks[2]:
    st.write("Details for Task 3: Prepare presentation")
    st.write("Deadline: July 25, 2024")

# Example: Add a checkbox to mark the task as completed
if st.checkbox("Mark task as completed"):
    st.write(f"Great! You have completed {selected_task}")
if st.checkbox("Mark task as in progreess"):
    st.write(f"Working in Progress{selected_task}")

# Add a footer or additional information
st.text("Built with Streamlit")
