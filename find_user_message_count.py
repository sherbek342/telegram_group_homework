from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    lis = []
    count = 0
    p = 0
    ids = find_all_users_id(data)
    for i in range(len(ids)):
        if ids[p] == users_id:
            count +=1
        p +=1 
    return count
users_id = 'user1953599777'
file = 'data/result.json'
print(find_user_message_count(file, users_id))