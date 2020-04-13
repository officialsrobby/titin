import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random
sandi = input('Masukan password : ')
if sandi == 'firman12':
	print('Welcome Bosku\nUdah Makan Belum?')
else:
    ws.close()
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()


rscode=0
while rscode!=1:
	#nomor = "06802143801"
	###nomor="081310972323"
	nomor = input("masukkan nomor telepon : ")
	###password="rahasia123@"
	password = input("masukkan password : ")
	headers={"User-Agent":"Mozilla/5.0"}
	response=requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers,json={"sns_type":"phone","sns_id":nomor,"password":password})
	#print(response.json())
	rscode = response.json()['results'][0]['result_code']
	if rscode !=1:
		print("nomor atau password salah , ulangi lagi")
print("berhasil login")
tirublock=response.json()['results'][0]['tag']
#time.sleep(100)
tokenl=response.json()['results'][0]['token']
print(response.json()['results'][0]['nickname'])
print("Token Anda Di Bawah")
print(tokenl)
