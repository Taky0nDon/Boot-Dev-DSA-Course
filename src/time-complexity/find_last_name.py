def find_last_name(names_dict, first_name):
    # Improve this code. right now it is O(n). Can we get it to O(1)?
#    for current_first_name, last_name in names_dict.items():
#        if current_first_name == first_name:
#            return last_name
# Looks like we can!
    return names_dict.get(first_name)
