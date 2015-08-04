import requests
from requests_jwt import JWTAuth
from urllib import urlencode

secret = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJpdGxlbmRpbmdjbHViLmNvbVwvYXBpXC90b2tlbiIsInN1YiI6IjY3MzYiLCJpYXQiOjE0Mzg2Nzg2NTEsImV4cCI6MTQ0MTI3MDY1MX0.I4nVxq94COixxnh6U1U9gcmkjkCZutxwJOYMKXzCsF8'

def post_example():
    url = "https://api.bitlendingclub.com/api/investment"
    params = {'loan_id': 15044, 'amount': 0.001, 'rate':1}
    headers = {
            'Authorization': 'Bearer ' + secret,
            'Accept': 'application/vnd.blc.v1+json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

    resp = requests.post(url,data=urlencode(params),headers=headers) #, auth=JWTAuth(secret))
    print(resp.text)

post_example()
