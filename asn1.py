#!/usr/bin/env python
import math,sys,argparse

_parser = argparse.ArgumentParser();
_parser.add_argument("-s","-speed",help = "Speed of link in MBPS",required = True)
_parser.add_argument("-u","-Userspeed",help = "User speed link in MBPS",required = True)
_parser.add_argument("-p","-probability_transmission",help = "probability of transmission",required = True)
_parser.add_argument("-q","-probability_queue_delay",help = "probability of no queue delay",required = True)
_args = _parser.parse_args()
s=_args.s
u=_args.u
p=_args.p
q=_args.q



try:
	s = float(s)
	if(s<0):
		print('Link speed cant be negative')
		sys.exit()
except ValueError:
	print('Oops!  Link speed was not valid number.')
	sys.exit()



try:
	u = float(u)
	if(u<0):
		print('user speed cant be negative')
		sys.exit()
	if(u>s):
		print('user speed cant be greater than link speed')
		sys.exit()
except ValueError:
	print('Oops!  user speed  not valid number.')
	sys.exit()


try:
	p = float(p)
	if(p<=0 or p>1):
		print('Oops! Probability of transmission should be greater than 0 or less than 1')
		sys.exit()
except ValueError:
	print('Oops!  Probability of transmission  was not valid number.  Try again')
	sys.exit()



try:
	q = float(q)
	if(q<=0 or q>1):
		print('Oops ! Probability of no queueing delay should be greater than 0 or less than 1')
		sys.exit()
except ValueError:
	print('Oops!  Probability of no queueing delay was not valid number.')
	sys.exit()


no_queue=0.0
N=0
no_queue=s/u
_,no_queue = math.modf(no_queue)
N=no_queue+1
i=0






def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def ass1():
	while True:
		i=0
		sum1=0
		while(i<=no_queue):
			global N
			ncr=nCr(N,i)
			product=ncr*math.pow(p,i)*math.pow(1-p,N-i)
			sum1=sum1+product
			i=i+1
		if(sum1<q):
			return N-1
		else:
			N=N+1




ans=ass1()
print('The maximum number of users that can be supported are',ans)
