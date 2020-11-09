import subprocess


def get_netsh_wifis_data():
	return subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')


def get_wifi_names(data):
	return [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]


def get_netsh_password_data(wifi):
	return subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')


def get_wifi_password(data):
	return [line.split(':')[1][1:-1] for line in data if 'Key Content' in line]


def print_wifi_password(wifi):
	data = get_netsh_password_data(wifi)
	wifi_password = get_wifi_password(data)
	try:
		print(f'Wi-fi: {wifi}, Password: {wifi_password[0]}')
	except Exception as e:
		print(f'Wi-fi: {wifi}, Password cannot be read')



def main():
	data = get_netsh_wifis_data()
	wifis = get_wifi_names(data)

	for wifi in wifis:
		print_wifi_password(wifi)


if __name__ == '__main__':
	main()