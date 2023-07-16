import requests
from time import sleep
for i in range(1,5):
	for state in [1,0]:
		r = requests.post("http://192.168.1.32:8001/jagcontrol/post", data={'relay':str(i), 'state':str(state)})
		print(r.text)
		sleep(2)

