import requests
# from requests_jwt import JWTAuth
secret = 'uhmm secret? xD'

def post_example():
    url = "https://api.bitlendingclub.com/api/investment"
    params = {'loan_id': 18152, 'amount': 0.001, 'rate': 1}
    headers = {
        'Authorization': 'Bearer ' + secret,
        'Accept': 'application/vnd.blc.v1+json',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    resp = requests.post(url, data=params, headers=headers)
    # auth=JWTAuth(secret))
    print(resp.text)
post_example()
