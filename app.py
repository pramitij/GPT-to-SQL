import streamlit as st
import pandas as pd
from sql_db_connection import SqlObject
from gpt_api import GptObject
import time

DB_NAME = 'my_sample_db.db'
sql_obj = SqlObject(DB_NAME)
gpt_obj = GptObject()
gpt_query = None

# Text input from user
user_input = st.text_input('Input User Text', '')
progress_text = ":hourglass:"
my_bar = st.progress(0, text=progress_text)


# Display user input in bold
if user_input:
    st.write('Log -> User Input:', user_input)

    gpt_prompt = sql_obj.create_prompt(user_input)
    gpt_response = gpt_obj.query_to_response(gpt_prompt)
    gpt_query = gpt_obj.get_sql_query(gpt_response)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.code(gpt_query, language="sql", line_numbers=False)

# Button to query SQL
if gpt_query:
    if st.button('Query SQL'):
    # Simulate a database output
        st.write('Database Output:')
        st.table(sql_obj.generate_df_from_query(gpt_query))
