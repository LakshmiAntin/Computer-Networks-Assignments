Group details:
		USN-1PI12IS045
		Name-Lakshmi Antin

How to execute the program:
			$chmod +x ass1.py
			$./ass1.py -s 2 -u 0.3 -p 0.3 -q 0.85
			The maximum nuber of users that can be supported are 15
			
				
Desription of the program:
			Assignment 1 is question number A1.The program should calculate the maximum number of users that can be supported such that probability that there is no queueing delay is greater than 'q'.This program contains two functions.One function nCr(n,r).It calculates combination nCr i.e combination of 'n' objects taken 'r' at a time.Second Function ass1() which is the important function where the main business logic of the assignment lies.nCr(n,r) is a helper function to calculate combination.Then main logic of this program lies in function ass1() and the logic is
			k   N	
			Σ    C  p^i (1-p)^i 	<  	q
			i=0   i
			where k=Number of users that can be supported without any queue
			      N=k+1 to required N
			      p=probaility of transmission
			the above formula is appiled form N=K+1 to maximum number of users that can be supported such that probability that there is no queueing delay is greater than 'q'.This 'q' is given as input by the user.The moment at which the above probability becomes less than 'q',we stop the process.Then return the value N-1.Because after this N,with probability of transmission being 'p',queueing might start.And we want to be no queue.

		
			Input validation is being done.If a user enters negative value or an undesirable input,appropriate error messages are displayed.If a user enters an undesirable input,the program is terminated there only,and it will not proceed further.So as there are 4 inputs,there are 4 while loops for this input validation.The speed link 'S' is expected to be enterd in "MBPS",and user speed in "MBPS".Probaility values i.e 'q' and 'p' should be greater than 0 and less than or equal to 1.Probaility 0 means event will not happen.This is taken care of.


challenges/Issues faced:
			Deciding the type was an issue.As the probability values are too small,storing them in appropriate type was an issue.Float is used in storing the values.input validation was an issue.using try and except blocks made coding easier and simple.using a variable which is declared outside and using in a function was an issue.so use the global Keyword to use the same N.To extract the whole number part from the number which indicates that users can be supported with no queue,i.e number obtained by s/u.The inbuilt function modf() is used to extract this whole number part, as common sense says that if number is 6.6667,6 users can be supported easily and with no queue.
