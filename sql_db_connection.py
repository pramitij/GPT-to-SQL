from sqlalchemy import create_engine
import sqlite3
import pandas as pd

SYSTEM_PROMPT = '''
Given the following SQL tables, your job is to write queries given a user’s request.
Also, wrap the column names, table names in double quotes.
CREATE TABLE "Categories" (
ID int,
Product Types str,
PRIMARY KEY (ID)
);

CREATE TABLE "Customers" (
ID int,
First Name str,
Last Name str,
Street Address str,
State str,
Zip Code str,
Email str,
Phone Number str,
City str,
Add to Mailing List? str,
Other Notes str,
PRIMARY KEY (ID)
);

CREATE TABLE "Menu Items" (
ID int,
Product ID int,
Sales Unit ID int,
Price Decimal,
PRIMARY KEY (ID)
);

CREATE TABLE "Order Items" (
ID int,
Order ID int,
Menu Item ID int,
Quantity str,
PRIMARY KEY (ID)
);

CREATE TABLE "Orders Table" (
ID int,
Customer ID int,
Paid bool,
Pre Order bool,
Notes str,
Pickup Date datetime,
PRIMARY KEY (ID)
);

CREATE TABLE "Orders: December" (
Product Types str,
Product Name str,
Sales Unit str,
# of Sales Unit Sold float,
Value of Sales Unit int,
Actual # Sold float,

);

CREATE TABLE "Products Table" (
ID int,
Category ID int,
Product Name str,
Description str,
PRIMARY KEY (ID)
);

CREATE TABLE "Sales Unit" (
ID int,
Product Name str,
SalesUnit Val int,
PRIMARY KEY (ID)
);
'''

class SqlObject:
    def __init__(self, db_name):
        self.db_name = db_name
        self.sql_con = sqlite3.connect(self.db_name)

    def generate_df_from_query(self, query):
        return pd.read_sql(query, self.sql_con)

    def create_prompt(self, user_input):

        return {"messages": [
        {"role": "system",
        "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}]}

