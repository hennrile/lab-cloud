import requests

cookies = {
    'user_session': '<YOUR_COOKIE>',
    'pythonsession': '<YOUR_COOKIE>'
}

response = requests.get('https://api.github.com/user', cookies=cookies)

print(response.json())