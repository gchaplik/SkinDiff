champDataLocation='champData.txt'
champions_dict = {}
with open(champDataLocation, 'r') as file:
    # Read all lines into a list
    for line in file:
        # Split the line into key (champion) and value
        champion, value = line.strip().split('\t')  # Assuming tab-separated columns, adjust as needed
        # Check if the champion already exists in the dictionary
        if champion in champions_dict:
            # If yes, add the value to the existing key
            champions_dict[champion] += value  # Assuming the value needs to be converted to an integer, adjust as needed
        else:
            # If not, create a new key-value pair
            champions_dict[champion] = value  # Assuming the value needs to be converted to an integer, adjust as needed

# Print the resulting dictionary
print(champions_dict)