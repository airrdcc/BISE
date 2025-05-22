def get_data():
    from pyhive import hive
    import pandas as pd

    # Hive connection parameters
    host = 'your_hive_host'
    port = 10000
    username = 'your_username'
    database = 'your_database'

    # Establish connection to Hive
    conn = hive.Connection(host=host, port=port, username=username, database=database)

    # Define your query to fetch e-commerce data
    query = "SELECT * FROM your_ecommerce_table"

    # Execute the query and fetch data into a DataFrame
    df = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    return df