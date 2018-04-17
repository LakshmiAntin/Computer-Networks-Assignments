#!/usr/bin/env python3
import sys
import argparse
import math
try:
	_parser = argparse.ArgumentParser()
	_parser.add_argument('-r1',help = "File containing router table of router1",required = True)
	_parser.add_argument('-i1',help = "address list of interfaces of router1",required = True)
	_parser.add_argument('-r2',help = "File containing router table of router2",required = True)
	_parser.add_argument('-i2',help = "address list of interfaces of router2",required = True)
	args = _parser.parse_args()
except:
	sys.exit()


def main():
	try:
		f1 = open(args.r1,'r')
		f2 = open(args.r2,'r')
		interface_1=args.i1
		interface_2=args.i2
	except:
		print('File can\'t be opened.')
		sys.exit()
	data1 =f1.readlines()
	data2 =f2.readlines()
	loop_network=[]
	for line1 in data1:			
		new_line1=line1.split(";")
		
		f2.seek(0,0)
		for line2 in data2:
			new_line2=line2.split(";")
			flag=0
			if_list=interface_2.split(',')
			for s in if_list:
				if s==new_line1[-2]:
					flag=1
					break
			if flag==1:
				inner_flag=0
				if_list2=interface_1.split(',')
				for j in if_list2:
					if j==new_line2[-2]:
						inner_flag=1
						break
                
				if inner_flag==1:
					ip1=new_line1[0]
					ip2=new_line2[0]
					mask1=new_line1[1]
					mask2=new_line2[1]

					list1=[]
					list2=[]
					list3=[]
					list4=[]
					str_1=""
					str_2=""
					list1=ip1.split('.')
					list2=ip2.split('.')

					for x in list1:
						x=int(x)
						x=bin(x)
						y=x[2:]
						y=y.zfill(8)
						str_1=str_1+y
					
					for z in list2:
						z=int(z)
						z=bin(z)
						t=z[2:]
						t=t.zfill(8)
						str_2=str_2+t
					
					str_3=""
					str_4=""
					mask1=int(mask1)
					mask2=int(mask2)
					if(mask1==mask2):
						if(str_1==str_2):
							print("loop occurs for ip",ip1,ip2)
							new_ip=ip1+'/'+str(mask1)
							loop_network.append(new_ip)
							
					if(mask1<mask2):
						count=0
						for x in str_2:
							if(count<mask1):
								str_3=str_3 + x
								count=count+1
							else:
								if(count!=32):
									str_3=str_3+'0'	
									count=count+1
						if(str_1==str_3):
							print("loop occurs for destination",ip1,ip2)
							new_ip=ip2+'/'+str(mask2)
							loop_network.append(new_ip)
							
					if(mask1>mask2):
						count=0
						for x in str_1:
							if(count<mask2):
								str_4=str_4 + x
								count=count+1
							else:
								if(count!=32):
									str_4=str_4+'0'	
									count=count+1		
						if(str_2==str_4):
							print("loop occurs for destination network",ip1,ip2)
							new_ip=ip1+'/'+str(mask1)
							loop_network.append(new_ip)
							
	print(loop_network)

def validate():
	f1=open(args.r1,'r')
	f2=open(args.r2,'r')
	data1 =f1.readlines()
	data2 =f2.readlines()
	list1=[]
	list2=[]
	flag=0
	for line1 in data1:
		new_list1=line1.split(';')
		for i in range(0,len(new_list1)):
			if(i%2==0):
				count=0
				str1=new_list1[i].split('.')
				if(len(str1)==4):
					for w in range(len(str1)):
						if str1[w].isdigit():
							if (int(str1[w])>=0 and int(str1[w])<256):
		         					count=count+1
						else:
							print("Invalid ip address present in r1.txt\nExiting...")
							sys.exit()

					if(count==len(str1)):
						pass
					else:
						print("Invalid ip address present in r1.txt\nExiting...")
						sys.exit()
				else:
					print("Invalid ip address present in r1.txt\nExiting...")
					sys.exit()
					
			elif(i==1):
				flag=0
				if(int(new_list1[i])<32 and int(new_list1[i])>=0):
            				flag=flag+1
            				pass
				else:
					print("invalid mask.exiting...")
					sys.exit()
			else:
				continue
	flag=0
	for line in data2:
		new_list2=line.split(';')
		for i in range(0,len(new_list2)):
			if(i%2==0):
				count=0
				str2=new_list2[i].split('.')
				if(len(str2)==4):
					for w in range(len(str1)):
						if str2[w].isdigit():
							if (int(str2[w])>=0 and int(str2[w])<256):
		         					count=count+1
						else:
							print("Invalid ip address present in r2.txt\nExiting...")
							sys.exit()

					if(count==len(str2)):
						pass
					else:
						print("Invalid ip address present in r2.txt\nExiting...")
						sys.exit()
				else:
					print("Invalid ip address present in r2.txt\nExiting...")
					sys.exit()
					
			elif(i==1):
				flag=0
				if(int(new_list2[i])<32 and int(new_list2[i])>=0):
            				flag=flag+1
            				pass
				else:
					print("invalid mask.exiting...")
					sys.exit()
			else:
				continue

	interface_val1=args.i1.split(',')
	for m in interface_val1:
		str_10=m.split('.')
		if(len(str_10)==4):
				count=0
				for w in range(len(str_10)):
					if str_10[w].isdigit():
						if (int(str_10[w])>=0 and int(str_10[w])<256):
		         				count=count+1
					else:
						print("Invalid ip address present in address list of r2\nExiting...")
						sys.exit()

				if(count==len(str_10)):
					pass
				else:
					print("Invalid ip address present in address list of r2\nExiting...")
					sys.exit()
		else:
			print("Invalid ip address present in address list of r2\n exiting... ")
			sys.exit()
			
	interface_val2=args.i2.split(',')
	for m in interface_val2:
		str_1=m.split('.')
		if(len(str_1)==4):
				count=0
				for w in range(len(str_1)):
					if str_1[w].isdigit():
						if (int(str_1[w])>=0 and int(str_1[w])<256):
		         				count=count+1
					else:
						print("Invalid ip address present in address list of r1\nExiting...")
						sys.exit()

				if(count==len(str_1)):
					pass
				else:
					print("Invalid ip address present in address list of r1\nExiting...")
					sys.exit()
		else:
			print("Invalid ip address present in address list of r1\n exiting... ")
			sys.exit()
			
validate()		            
main()

