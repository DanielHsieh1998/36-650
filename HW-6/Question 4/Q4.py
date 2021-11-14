def delete_keys(list_key, dictionary):
    for key in list_key:
        dictionary.pop(key)
    return dictionary

my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
print(delete_keys(['First','Second'], my_dict))

dict = {"firstName":"Mohanmed","lastName":"Farag","birthYear":1990,"nationality":"Egyptian"}
print(delete_keys(["lastName","birthYear"],dict))