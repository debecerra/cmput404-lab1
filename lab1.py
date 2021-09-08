import requests;

print("requests module version:", requests.__version__)
print()

""" Ben Lloyd Pearson, How to Use the Python Requests Module With REST APIs
    2020-07-11, https://www.nylas.com/blog/use-python-requests-module-rest-apis/
    Public Domain
"""
response = requests.get("https://raw.githubusercontent.com/debecerra/cmput404-lab1/main/lab1.py")
print(response.text.replace("\\n", "\n"))
