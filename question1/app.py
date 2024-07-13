import streamlit as st
import mysql.connector
import pandas as pd

# Function to create a connection to the MySQL database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        st.success("Connection to MySQL DB successful")
    except mysql.connector.Error as err:
        st.error(f"Error: '{err}'")
    return connection

# Function to execute a query and fetch data
def run_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        st.error(f"Failed to run the query - {err}")
        return None

# Function to fetch data from the selected table
def fetch_data(connection, table_choice):
    sql_query = f'SELECT * FROM {table_choice};'
    tbl_data = run_query(connection, query=sql_query)
    if tbl_data:
        df = pd.DataFrame(tbl_data)
        st.table(df)
    else:
        st.write("No data found or query failed.")

# Streamlit interface
st.title('MySQL Database Connector')

# Database connection parameters
st.sidebar.header('Database Connection Parameters')
host = st.sidebar.text_input('Host', 'localhost')
user = st.sidebar.text_input('User', 'root')
password = st.sidebar.text_input('Password', type='password')
database = st.sidebar.text_input('Database')

if 'connection' not in st.session_state:
    st.session_state.connection = None

if st.sidebar.button('Connect'):
    st.session_state.connection = create_connection(host, user, password, database)

if st.session_state.connection:
    table_lst_data = run_query(st.session_state.connection, query='SHOW TABLES;')
    if table_lst_data:
        df_lst_tbl = pd.DataFrame(table_lst_data)
        options = ['Select an option'] + df_lst_tbl[df_lst_tbl.columns[0]].tolist()
        table_choice = st.selectbox(label='Select Table from the below list', options=options)

        if table_choice and table_choice != 'Select an option':
            fetch_data(st.session_state.connection, table_choice)
    else:
        st.write("Failed to retrieve tables from the database.")
