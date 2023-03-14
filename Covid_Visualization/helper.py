### This file stores the helper functions 
### to be used in the jupyter notebooks

def execute_q(query, cur):
    """ get the result of SQL Query as pandas dataframe """
    import pandas as pd
    import sqlite3

    try:
        # run the query
        result = cur.execute(query) # to get value results as tuple
    except sqlite3.OperationalError as err:
        # if something went wrong
        print(err)
        return 1
    
    # if query success, create of list of col:val pairs
    tmp_list = [dict(row) for row in result]
    # make pandas dataframe
    tmp_df = pd.DataFrame(tmp_list)  
    
    return tmp_df