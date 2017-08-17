import subprocess
import re
import sys
from datetime import datetime
h = 0
o = 0
s = "Host:"
time=str(datetime.now())
time=time[:-10]
with open("/var/www/html/"+sys.argv[1]+"index.html","w") as r:
	print("<html>", file = r)	
	print("<style>", file = r)
	print("body{", file = r)
	print("\tcolor:white;", file = r)
	print("\tbackground-color:#0071c5", file = r)
	print("\tbackground: -webkit-linear-gradient(left, #001a2d, #0082e6);", file = r)
	print("\tbackground: -o-linear-gradient(right, #001a2d, #0082e6);", file = r)
	print("\tbackground: -moz-linear-gradient(right, #001a2d, #0082e6);", file = r)
	print("\tbackground: linear-gradient(to right, #001a2d, #0082e6);", file = r)
	print("}", file = r)
	print("</style>", file = r)
	print("<IMG SRC=\"/IntelLogo-300x150.png\" alt = \"Intel Logo\" width = \"300px\" height = \"150px\" align = \"right\" ></IMG>",file = r)
	print("<title>", file = r)
	print("Intel Server Info", file = r)
	print("</title>", file = r)
	print("<h3>", file = r)
	print("Intel Server Info", file = r)
	print("</h3>", file = r)
	print("<body>", file = r)
	print("<p><a href=\"/refresh_long\"><font color=\"FF0000\">Refresh Information (This may take a while)</font></a></p>", file = r)
	print("<p><a href=\"/\"><font color=\"FF0000\">Condensed List</font></a></p>", file = r)
	print("<p>Last Updated:</p>",file = r)
	print("<p>"+str(time)+"</p>", file = r)
	with open("/home/austin/server_reserve/"+sys.argv[1]+"cpuinfo.json", "r") as f:
		brlist = ["{","}",",","\"","\\n",]
		jsondata = f.read()	


		for i in brlist:
			jsondata = jsondata.replace(i, "<br>" )

		jsondata = jsondata.replace("<br>: <br>", "<br>" )
		jsondata= jsondata.replace("\\t","")
		jsondata= jsondata.replace("\r","")

		h = jsondata.count(s)
		
		hosts = re.findall('Host:(\S+)',jsondata)
#		print(hosts)
		for t in hosts:
#			o = o + 1
#			q = str(o)
			abbreviate=t[:-1]
			print("<p><a href=\"#h"+abbreviate+"\"><font color=\"FF0000\">Jump to Host "+t+"</font></a></p>", file = r)
			jsondata = jsondata.replace("Host:"+t+"","<p><a href=\"#""\"><font color=\"FF0000\">Jump to Top</font></a></p><font style=\"background-color: #EF4323\" id= h"+t+">Host: "+t+"</font>",1)

	
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
		print("<p><a href=\"#\"><font color=\"FF0000\">Jump to Top</font></a></p>", file = r)
		print("</body>", file = r)
		print("</html>", file = r)

subprocess.check_call("/home/austin/server_reserve/frontend/clean_up.sh "+str(sys.argv[1]),shell=True)
