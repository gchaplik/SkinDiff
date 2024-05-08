import pandas as pd
champDataLocation='champData.txt'
champions_dict = {}
with open(champDataLocation, 'r') as file:
    # Read all lines into a list
   for line in file:
        # Split the line into key (champion) and value
        champion, value_str = line.strip().split('\t')  # Assuming tab-separated columns, adjust as needed
        
        # Remove commas from the value string
        value_str = value_str.replace(',', '')
        
        try:
            # Attempt to convert the value to an integer
            value = int(value_str)
        except ValueError:
            # Handle the case where the value cannot be converted to an integer
            print(f"Error: Invalid value '{value_str}' for champion '{champion}'. Skipping this entry.")
            continue
        
        # Check if the champion already exists in the dictionary
        if champion in champions_dict:
            # If yes, add the value to the existing key
            champions_dict[champion] += value
        else:
            # If not, create a new key-value pair
            champions_dict[champion] = value
# Print the resulting dictionary
df = pd.DataFrame(data=champions_dict, index=[0])

df = (df.T)
df.to_excel('champData.xlsx')
print(champions_dict)