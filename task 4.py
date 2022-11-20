import requests
url = "https://www.netflix.com" # takes in url
page = requests.get(url)
if page.status_code == 200 #200 means url is functioning
    print("This URL is working")
else:
    print("This URL is not working")

