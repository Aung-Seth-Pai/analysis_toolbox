""" This file stores helper functions """

def query_casualty(accident_id, col_name=None):
    """ 
        query casualty related to an accident from casualty dataset using "accident_id"
    """
    if col_name==None:
        return casualty.query(f"accident_index == '{accident_id}'")
    else:
        return casualty.query(f"accident_index == '{accident_id}'")[col_name]


def name_lookup(lookup_df, col_name):
    """ For a given column, get dict containing numerical label and their meaning 
        
        Args:
            lookup_df : dataframe containing column label meanings
            col_name  : name of column to lookup
            
        Returns:
            A dictionary with { label code : text meaning }
    """
    label = lookup_df[lookup_df['field name']==col_name]["label"]
    code = lookup_df[lookup_df['field name']==col_name]["code/format"].astype(int)
    return dict(zip(code, label))