#Cipher Program Designed to take any code and cipher a message
from Tkinter import *

chr_list = [' ','-']
num_list = ['0','1','2','3','4','5','6','7','8','9']
let_list =[]
code_set = []
cipher_set = []

for i in range(65,91):
    let_list.append(chr(i))
	
class Cipher(object):
	
	def __init__(self):
		pass
		
	def start_text(self):
		print "----------------------------"
		print "WELCOME TO CIPHER PROGRAM V2"
		print "----------------------------"
		raw_input('> ')
		print ''
		
	def code_text(self):
		print "PLEASE INPUT ANY TEXT BELOW "
		print "THAT YOU WISH TO CIPHER     "
		
	def cipher_text(self):
		print "PLEASE INPUT ANY NUMERIC    "
		print "CODE YOU WISH TO BECOME YOUR"
		print "CIPHER"
		
	def code_test(self):
		code_pass = False
		while code_pass == False:
			code_attempt = raw_input('> ')
			if code_attempt == '':
				print "YOU NEED TO ENTER A CODE"
			else:
				code_pass = True
		return code_attempt
		
	def cipher_test(self):
		cipher_pass = False
		while cipher_pass == False:
			cipher_attempt = raw_input('> ')
			if cipher_attempt == '':
				print "YOU NEED TO ENTER A CODE"
			else:
				num_only = True
				for entry in cipher_attempt:
					if entry not in num_list:
						num_only = False
				if num_only == False:
					print "YOUR CIPHER SHOULD ONLY"
					print "CONTAIN NUMBERS"
				else:
					cipher_pass = True
		return cipher_attempt
					
	def merge_code(self, code, cipher):
		counter = 0
		for char in code:
			if char in chr_list:
				pairing = [char, 0]
				code_set.append(pairing)
			else:
				pairing = [char.upper(), cipher[counter]]
				code_set.append(pairing)
				if counter == len(cipher) - 1:
					counter = 0
				else:
					counter = counter + 1
		return code_set
	
	def up_or_down(self):
		print "CIPHER THE CODE UP OR DOWN"
		move_pass = False
		while move_pass == False:
			move_attempt = raw_input('> ').upper()
			if move_attempt != 'UP' and move_attempt != 'DOWN':
				print "YOU MUST ENTER UP OR DOWN"
			else:
				move_pass = True
				return move_attempt
				
	def move_code(self, code_set, move):		
		cipher_set = []
		for pairs in code_set:
			move_factor = int(pairs[1])
			if move == 'UP':
				if pairs[0] in num_list:
					pre_char = int(pairs[0])
					post_char = (pre_char + move_factor)%10
					post_char = num_list[post_char]
				elif pairs[0] in chr_list:
					post_char = pairs[0]
				else:
					pre_char = let_list.index(pairs[0])
					post_char = (pre_char + move_factor)%26
					post_char = let_list[post_char]
			elif move == 'DOWN':
				if pairs[0] in num_list:
					pre_char = int(pairs[0])
					post_char = (pre_char - move_factor)%10
					post_char = num_list[post_char]
				elif pairs[0] in chr_list:
					post_char = pairs[0]
				else:
					pre_char = let_list.index(pairs[0])
					post_char = (pre_char - move_factor)%26
					post_char = let_list[post_char]				
			cipher_set.append(post_char)
		cipher_string = ''.join(cipher_set)
		return cipher_string
			
	def end_cipher(self, cipher_string):
		print 'YOUR CIPHER CODE IS: ' + cipher_string
		print 'IT IS NOW APPENDED TO YOU CLIPBOARD'

		r = Tk()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(cipher_string)
		r.destroy()        

run_cipher = Cipher()
run_cipher.start_text()
run_cipher.code_text()
code = run_cipher.code_test()
run_cipher.cipher_text()
cipher = run_cipher.cipher_test()
final = run_cipher.merge_code(code, cipher)
movement = run_cipher.up_or_down()
string = run_cipher.move_code(final, movement)
run_cipher.end_cipher(string)

			
		
						
	