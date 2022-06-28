import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("My First Streamlit Web App")

df = pd.DataFrame({
  "one": [1, 2, 3], 
  "two": [4, 5, 6], 
  "three": [7, 8, 9], 
  "four": [10, 11, None],
})
st.write(df)

st.title("Connect to Google Sheets")
# gsheet_url = "https://docs.google.com/spreadsheets/d/1ixMrhGV1TPn14_oTyEIFjszuwuwO9xkbsc1WEBJH3N0/"

gsheet_url = 'https://docs.google.com/spreadsheets/d/1VJjPLds4agbLijYEDup3nsYMcKK57w9YAp0qR5hYixo/edit#gid=613469656'
#url = 'https://docs.google.com/spreadsheets/d/1jmRQJC4wQtSny-JTA3KLJ4BeVFdYU3qQanZerh_5IEU'
st.markdown("""
  Check original Google Sheet data at this [URL](https://docs.google.com/spreadsheets/d/1ixMrhGV1TPn14_oTyEIFjszuwuwO9xkbsc1WEBJH3N0/)
""")
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)
