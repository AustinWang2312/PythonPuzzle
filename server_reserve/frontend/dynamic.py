import subprocess
import re
import sys

h = 0
o = 0
s = "Host:"
with open("/var/www/html/"+sys.argv[1]+"index.html","w") as r:
	print("<html>", file = r)	
	print("<style>", file = r)
	print("body{", file = r)
	print("\tcolor:white;", file = r)
	print("\tbackground-color:#0071c5", file = r)
	print("}", file = r)
	print("</style>", file = r)
#	print("<IMG SRC=\"https://cdn.drawception.com/images/panels/2012/4-4/rrqqf3zZXh-6.png\" alt = \"Intel Logo\" width = \"300px\" height = \"250px\" align = \"right\" ></IMG>",file = r)
	print("<title>", file = r)
	print("Intel Server Info", file = r)
	print("</title>", file = r)
	print("<h3>", file = r)
	print("Intel Server Info", file = r)
	print("</h3>", file = r)
	print("<body>", file = r)
	print("<p><a href=\"/refresh\">Refresh Page</a></p>", file = r)
	with open("/home/austin/PythonPuzzle/server_reserve/"+sys.argv[1]+"cpuinfo.json", "r") as f:
		brlist = ["{","}",",","\"","\\n",]
		jsondata = f.read()	


		for i in brlist:
			jsondata = jsondata.replace(i, "<br>" )

		jsondata = jsondata.replace("<br>: <br>", "<br>" )
		jsondata= jsondata.replace("\\t","")
		jsondata= jsondata.replace("\r","")

		h = jsondata.count(s)
		
		hosts = re.findall('Host:(\S+)',jsondata,re.S)
#		print(hosts)
		for t in hosts:
			o = o + 1
			q = str(o)
			print("<p><a href=\"#h"+q+"\">Jump to Host "+t+"</a></p>", file = r)
			jsondata = jsondata.replace("Host:"+t+"","<p><a href=\"#\">Jump to Top</a></p><font style=\"background-color: #EF4323\" id= h"+q+">Host: "+t+"</font>",1)

	
#		for i in brlist:
#			jsondata = jsondata.replace(i, "<br>" )
#			
#		jsondata = jsondata.replace("<br>: <br>", "<br>" )
#		jsondata= jsondata.replace("\\t","")	
		
		jsondata = jsondata.replace(">>",">")
		title = ["Memory Info:","Network Interface:","Distribution:","CPU Architecture:","Kernel:","Users:"]

		for j in title:
			jsondata = jsondata.replace(j, "<font style=\"background-color:ff8e3a\">"+j+"</font>")
		
		num = 0
		numh = re.findall("Host:", jsondata)
		while num < len(numh):
			for k in numh:
				num = num + 1
				jsondata = jsondata.replace(k, "Host " + str(num) + ":", 1)
#               num = 0
#               numu = re.findall("Users:", jsondata)
#               while num < len(numu):
#                       for l in numu:
#                               num = num + 1
#                               jsondata = jsondata.replace(l,"Users " + str(num)+ ":", 1)
		numt = re.findall("Total:",jsondata)
		num = 0
		while num < len(numt):
			for tot in numt:
				num = num + 1
				jsondata = jsondata.replace(tot,"Total<!--" + str(num)+ "-->:", 1)
		num = 0
		while num < len(numt):
			num = num + 1
                        #use = re.findall("Users "+str(num)+".*Total "+str(num)+":[\d]",jsondata,re.S|re.M)
			use = re.findall("Total<!--"+str(num)+"-->:[\d]",jsondata,re.S|re.M)
                        #use = re.findall(":[\d]",use)  
			us = str(use)
			on = int(us[-3])
			if on < 2:
				jsondata = jsondata.replace("\"background-color: #EF4323\" id= h"+str(num)+">Host "+str(num)+":","\"background-color: #9ACD32\" id= h"+str(num)+">Host "+str(num)+":")

	#	jsondata = jsondata.replace("Host:", "<font style=\"background-color: #EF4323\">Host:</font> ")

		print(jsondata, file = r)
		print("<p><a href=\"#\">Jump to Top</a></p>", file = r)
		print("</body>", file = r)
		print("</html>", file = r)

subprocess.check_call("/home/austin/PythonPuzzle/server_reserve/frontend/clean_up.sh "+str(sys.argv[1]),shell=True)
