def has_duplicates(id_list):
    unique_id_list = list(set(id_list))
    if len(unique_id_list) != len(id_list):
        return True
    else:
        return False
