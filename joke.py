import requests

# defining the API endpoint
endpoint = "https://official-joke-api.appspot.com/random_joke"

# make a request
response = requests.get(endpoint)

# check if request worked
if response.status_code == 200:
   # load JSON data from the response
   joke = response.json()
   count = 0
   #only print setup and punchline values in dictionary
   for value in joke.values():
   	if count == 1 or count == 2:
   		print(value)
   	count = count + 1
   	
else:
   # if the request unsuccessful, print an error message
   print("error", response.status_code)
