# Connect to Oracle DB that exists to pull data
# Show some SQL data manipulation (i.e. aggregate functions, window functions, joins, etc.)
# If there's time, set up Azure SQL Database or Snowflake DB along with varying credentials in .env file
# with varying credentials, create function app to determine which source to pull from

import oracledb
import pandas as pd
import os

test = os.getenv("orcl_username")

# Set up Oracle client configuration (adjust as needed)
# cx_Oracle.init_oracle_client(lib_dir="/path/to/instantclient")  # Uncomment and specify the path if needed

def connect_to_oracle(username, password, hostname, port, service_name):
    """
    Connects to an Oracle database using cx_Oracle.

    :param username: Database username
    :param password: Database password
    :param hostname: Database host
    :param port: Database port (usually 1521 for Oracle)
    :param service_name: Database service name or SID
    :return: Oracle connection object
    """
    try:
        local_dsn = f'{hostname}:{port}/{service_name}'

        connection = oracledb.connect(user=username, password=password, dsn=local_dsn)
        
        print("Successfully connected to the Oracle database")
        return connection
    except:
        print(f"Error connecting to Oracle database: {e}")
        return None

def fetch_data_as_dataframe(connection, query):
    """
    Executes a query and fetches data as a pandas DataFrame.

    :param connection: Oracle database connection object
    :param query: SQL query to execute
    :return: DataFrame containing the query results
    """
    try:
        # Execute the query and read it into a DataFrame
        df = pd.read_sql(query, con=connection)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def main():
    # Connection details
    username = orcl_username
    password = orcl_password
    hostname = orcl_hostname
    port = orcl_port
    service_name = orcl_service_name

    # Connect to the Oracle database
    connection = connect_to_oracle(username, password, hostname, port, service_name)

    # If connection is successful, fetch data
    if connection:
        # SQL query to fetch data from the 'superstore_orders_stg' table
        query = 'SELECT * FROM superstore_orders_stg'

        # Fetch the data and create a DataFrame
        df = fetch_data_as_dataframe(connection, query)

        # Display the first few rows of the DataFrame
        print("Data from the superstore_orders_stg table:")
        print(df.head())

        # Close the database connection
        connection.close()

if __name__ == "__main__":
    main()
