import requests;

print("requests module version:", requests.__version__)

""" Ben Lloyd Pearson, How to Use the Python Requests Module With REST APIs
    2020-07-11, https://www.nylas.com/blog/use-python-requests-module-rest-apis/
    Public Domain
"""
response = requests.get("http://www.google.com")
print(response)

