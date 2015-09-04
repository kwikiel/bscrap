import requests
from requests_jwt import JWTAuth

secret = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJpdGxlbmRpbmdjbHViLmNvbVwvYXBpXC90b2tlbiIsInN1YiI6IjY3MzYiLCJpYXQiOjE0NDEzNzY4MTIsImV4cCI6MTQ0Mzk2ODgxMn0.ihBeEJ9CRGzUBomQTbU4STitCbKCjkGkdlt_4rELyG4'

def post_example():
    url = "https://api.bitlendingclub.com/api/investment"
    params = {'loan_id': 16025, 'amount': 0.001, 'rate':1}
    headers = {
            'Authorization': 'Bearer ' + secret,
            'Accept': 'application/vnd.blc.v1+json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

    resp = requests.post(url,data=params,headers=headers) #, auth=JWTAuth(secret))
    print(resp.text)

post_example()
