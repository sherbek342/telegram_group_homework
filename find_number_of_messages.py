from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    counter = 0
    data = read_data(file)
    for i in data['messages']:
        counter +=1
    return counter
file = 'data/result.json'
print(find_number_of_messages(file))