from Crypto.Cipher import AES
import os
IV='1111111122222222'
for i in range(1,11):
	inp=open("./jpgs/"+str(i)+'.jpg','rb').read()
	out=open('./cfb/'+str(i)+'.jpg.enc','w')
	key=os.urandom(16)
	aes=AES.new(key,AES.MODE_CFB,IV)
	out.write(aes.encrypt(inp))

	
