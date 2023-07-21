from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    lis = []
    file = 'data/result.json'
    data = read_data(file)
    for i in data['messages']:
        if i['type']== 'service':
            if i['actor_id'].startswith('user'):
                lis.append(i['actor_id'])
        if i['type']== 'message':
            if i['from_id'].startswith('user'):
                lis.append(i['from_id'])
    return lis