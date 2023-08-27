# Import the requests package.
# Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The Social Network. The query string should have two arguments: apikey=72bc447a and t=the+social+network. You can combine them as follows: apikey=72bc447a&t=the+social+network.
# Print the text of the response object r by using its text attribute and passing the result to the print() function.

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com?t=the+social+network&apikey=72bc447a'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
