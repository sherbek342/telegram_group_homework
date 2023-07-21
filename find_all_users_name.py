from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    lis = []
    data = read_data(file)
    for i in data['messages']:
        if i['type']== 'service':
                lis.append(i['actor'])
        if i['type']== 'message':
                lis.append(i['from'])
    return lis
file = 'data/result.json'
print(find_all_users_name(file))
