""" This file stores helper functions """

def query_casualty(accident_id, col_name=None):
    """ 
        query casualty related to an accident from casualty dataset using "accident_id"
    """
    if col_name==None:
        return casualty.query(f"accident_index == '{accident_id}'")
    else:
        return casualty.query(f"accident_index == '{accident_id}'")[col_name]


def lookup_func(col, dataset, attribute="note"):
    """ 
        function to lookup a feature's attribute easily
        ** works only on lookup dataset **
        
    """
    return dataset[dataset["field name"]==col][attribute]