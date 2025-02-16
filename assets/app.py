import requests

url = 'https://onlinebanking.zicb.co.zm/retailbanking-auth/login'

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer 20E38214tC181205'
}

payload = {
    'username': 'kk',
    'password': 'll',
    'requestId': 'LOGIN'

}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
