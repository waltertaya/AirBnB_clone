import re

def extract_strings(input_string):
    # Define a regular expression pattern to match the function call format
    pattern = re.compile(r'(\w+)\.(\w+)\((?:"([^"]+)"(?:, "([^"]+)"(?:, "([^"]+)")?)?)?\)')


    
    # Use the pattern to find matches in the input string
    matches = re.findall(pattern, input_string)
    
    # If there are matches, return the extracted strings as a list
    if matches:
        return list(filter(None, matches[0]))  # Filter out any empty strings
    else:
        return None

# Example usage:
input_string = 'User.all()'
result = extract_strings(input_string)

if result:
    print(result)
else:
    print("No match found.")

input_string = 'User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")'
result = extract_strings(input_string)

if result:
    print(result)
else:
    print("No match found.")