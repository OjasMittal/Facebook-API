import requests
import json

url ="https://graph.facebook.com/v13.0/1638456813180268?fields=link%2Cimages&access_token=EAAIVqJpuRJ4BAGZCuZByoZAOgJD2r3J6JVFnGHxhvmj0ncBVVBnWkugpy1U1J3nZCZApBt989vDai1FVdb6ZAfkWOuKa1hZBntXPZB2DUlP669NOZC1VsfmZAwPZBbZB4BvTG7LYfB9Py0tEYafyzjS0XfU0zVV5vPAihEEw9qJQY0ZC0JZB0haMW2Dup6nWIv0skBmde0j597B8ObYiBG9lv4lH4D0ZBo08RKfHs7pXPULWHV7hS0wddOzITKW"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
  file.write(image_bytes)
  