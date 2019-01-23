import struct

def bytesToFloat(bytes):
	return struct.unpack('>f',bytes)[0]

def bytesToInt(bytes):
	return int.from_bytes(bytes,byteorder='big')

def dataToVectorsI(data,n):
	result = []
	for i in range(0,len(data),n):
		result.append(bytesToInt(data[i:i+n]))
	return result

def dataToVectors(data,n):
	result = []
	for i in range(0,len(data),n):
		result.append(bytesToFloat(data[i:i+n]))
	return result

def variance(vectors):
	m=mean(vectors)
	squared = [(x-m)**2 for x in vectors]
	return sum(squared)/(len(vectors) - 1)
	
def mean(vectors):
	return float(sum(vectors))/len(vectors)

def vectorsFromFile(filename,vec_size):
	data=open(filename,'rb').read()
	return dataToVectors(data,vec_size)
	

def vectorsFromFileI(filename,vec_size):
	data=open(filename,'rb').read()
	return dataToVectorsI(data,vec_size)





