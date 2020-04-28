def len_int(a):
	i=0
	while(a!=0) :
		a=a//10
		i=i+1
	return i


def cesar_encode(u,k):
	C=[]
	for i in range(len(u)):
		if(u[i]==" ") :
			return C
		num=ord(u[i])
		if(  ( num >= ord("a") ) and ( num <= ord("z") )  ) :
			num=num+k
			if(num > ord("z")) :
				dif=num-ord("z")
				num=ord("a")-1+dif
			C.append(chr(num))

		elif (  ( num >= ord("A") ) and ( num <= ord("Z") )  ) :
			num=num+k
			if(num > ord("Z")) :
				dif=num-ord("Z")
				num=ord("a")-1+dif
			C.append(chr(num))
		else:
			return False
	return C


def cesar_decode(u,k):
	D=[]
	for i in range(len(u)):
		if(u[i]==" ") :
			return D
		num1=ord(u[i])
		if(  ( num1 >= ord("a") ) and ( num1 <= ord("z") )  ) :
			num1=num1-k
			if(num1 < ord("a")) :
				dif=ord("a")-num1
				num1=ord("z")+1-dif
			D.append(chr(num1))

		elif (  ( num1 >= ord("A") ) and ( num1 <= ord("Z") )  ) :
			num1=num1-k
			if(num1 < ord("A")) :
				dif=ord("A")-num1
				num1=ord("Z")+1-dif
			D.append(chr(num1))
		else:
			return False
	return D

def vigenere_encode(u,k,key):

	def vigenere_bloc1(u,k,key):
		V=[]
		for i in range(k-1,-1,-1):
			r=key%10
			key=key//10
			V.append("".join(cesar_encode(u[i],r)))
		V=V[::-1]
		return V

	V=""
	while(len(u)%k!=0) :
		u=u+" "
	for i in range(0,len(u)+1-k,k):
		V=V+"".join(vigenere_bloc1(u[i:i+k],k,key))
	return V

def vigenere_decode(u,k,key):
	
	def vigenere_bloc2(u,k,key):
		N=[]
		for i in range(k-1,-1,-1):
			r=key%10
			key=key//10
			N.append("".join(cesar_decode(u[i],r)))
		N=N[::-1]
		return N
	N=""
	while(len(u)%k!=0) :
		u=u+" "
	for i in range(0,len(u)+1-k,k):
		N=N+"".join(vigenere_bloc2(u[i:i+k],k,key))
	return N
		

u=str(input("entrez une chaine de character a chiffree avec le Chiffrement de Vignere:  "))
k=int(input("entrez la longueur des blocs:  "))
key=int(input("entrez la cle de Chiffrement:  "))
while(len_int(key)!=k) :
	key=int(input("entrez la cle de Chiffrement:  "))
u=u.replace(" ", "")
v=vigenere_encode(u,k,key)
print(v)
u=str(input("entrez une chaine de character a dechiffree avec le Chiffrement de Vignere:  "))
key=int(input("entrez la cle de Dechiffrement:  "))
k=len_int(key)
n=vigenere_decode(u,k,key)
print(n)