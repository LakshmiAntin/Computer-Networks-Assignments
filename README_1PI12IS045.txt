GROUP DETAILS :
 		1PI12IS026-Bilwa
		1PI12IS045-Lakshmi Antin
		1PI12IS052-Manasa H G

HOW TO EXECUTE THE PROGRAM WITH AN EXAMPLE :
	
		The program is compiled  as chmod +x asn2.9.py.Then it is run as ./asn2.9.py -r1 <file having R1 routing table> -i1 <address list of R1> -r2 <file having R2 routing table> -i2 <address list of R2>

		Then program prints the destination addresses  for which routing loop occurs.
	
		Example:
			Consider the routing table R1
			Destination address         mask length        next hop address     interface
   			12.1.1.0                      24                  11.3.1.0               e1
                        15.2.3.0                      16                  11.2.1.0               e2
                        10.1.1.1                      18                  11.1.1.0               e3
                        109.10.12.0                   24                  11.4.1.0               e3


			interface list of r1 as a paramaeter -i1
			20.2.3.1,20.1.2.3,20.3.1.2

			
			Destination address         mask length        next hop address     interface
   			12.1.1.128                    26                  20.2.3.1               e3
                        15.10.1.0                     28                  20.1.2.3               e1
                        12.10.1.0                     14                  20.1.2.3               e2
                        109.1.1.0                     8                   20.3.1.2               e4


			interface list of r2 as a paramaeter -i2
			11.1.1.0,11.2.1.0,11.3.1.0,11.4.1.0

		
			when the program is invoked as : ./asn2.9.py -r1 r1.txt -i1 20.2.3.1,20.1.2.3,20.3.1.2 -r2 r2.txt -i2 							11.1.1.0,11.2.1.0,11.3.1.0,11.4.1.0
			where r1 and r2 are the files containing the routing tables

			r1.txt:
				12.1.1.0;24;11.3.1.0;e1
				15.2.3.0;16;11.2.1.0;e2
				10.1.1.1;18;11.1.1.0;e3
				109.10.12.0;24;11.4.1.0;e3

			r2.txt:
				12.1.1.128;26;20.2.3.1;e3
				15.10.1.0;28;20.1.2.3;e1
				12.10.1.0;14;20.1.2.3;e2
				109.1.1.0;8;20.3.1.2;e4
		
			The output will be :
						loop occurs for destination 12.1.1.0 12.1.1.128
						['12.1.1.128/26']
			Thus there is loop for destination address 12.1.1.128/26
			
			
DESCRIPTION OF HOW THE PROGRAM WORKS:
		The program expects 4 arguments as mentioned above."argparse" is used to extract the parameter values.If any of them is missing then appropriate message is displayed,as argparse is used.If file can't be opened then also appropriate message is displayed.File containing the routing tables of two router is assumed to be in following format-destination address,mask length,next hop router address,interface.Each of these separated by a ';'.The paramaters -i1 and -i2 i.e address list of router's interface are only IP address,that is there mask values are not specified at the time of the input.

		The next hop address for each entry in router 1's routing table is checked with each entry in address list of router 2.If it is found a flag variable is set to true.And then next hop address for each entry in router 2's routing table is checked with each entry in address list of router 1.If it is found then an variable inner flag is set to true.Two for loops for each of these checking is used.If inner flag is set, the destination addresses for both the entries in there respective tables are checked.If they are same then routing loop occurs and these destination addresses are stored in a list and displayed at end of the program.

		For checking the destination addresses,the mask length of those are also compared.If the two masks are same then directly they are compared.If one mask is smaller than the other,then smaller mask is applied to destination address which has larger mask.The address obtained after applying the mask is checked with the destination address with smaller mask.If the two are same then routing loop occurs and those are stored in list.The destination address with larger mask is printed as shown in above example.

		Input validation is done.If in the file there is an invalid IP address then appropriate message is displayed and program is terminated.The mask values are checked to lie in range 0-32,if not so message is displayed and program is terminated.IP address in Address list of r1 and r2 are also checked and same method is followed for them also.

CHALLENGES/ISSUES FACED:
                     Understanding the concept of routing loop was difficult.Understanding how the router works was difficult.Input validation took a lot of time.Comparing destination address's considering their mask value was challenging task for coding.Like destination address which donot look same but are same was little hard to digest and code for it. But when we approached sir personally,we understood the concepts.
			
			
