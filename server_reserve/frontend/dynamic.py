import subprocess
import re
h = 0
o = 0
s = "Host:"
with open("/var/www/html/index.html","w") as r:
	print("<html>", file = r)	
	print("<style>", file = r)
	print("body{", file = r)
	print("\tcolor:white;", file = r)
	print("\tbackground-color:#0071c5", file = r)
	print("}", file = r)
	print("</style>", file = r)
	print("<title>", file = r)
	print("Intel Server Info", file = r)
	print("</title>", file = r)
	print("<h3>", file = r)
	print("Intel Server Info", file = r)
	print("</h3>", file = r)
	print("<body>", file = r)
	with open("./cpuinfo.json", "r") as f:
		brlist = ["{","}",",","\"","\\n"]
		jsondata = f.read()	


		for i in brlist:
			jsondata = jsondata.replace(i, "<br>" )

		jsondata = jsondata.replace("<br>: <br>", "<br>" )
		jsondata= jsondata.replace("\\t","")

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

	#	jsondata = jsondata.replace("Host:", "<font style=\"background-color: #EF4323\">Host:</font> ")

		print(jsondata, file = r)
		print("<p><a href=\"#\">Jump to Top</a></p>", file = r)
		print("</body>", file = r)
		print("</html>", file = r)

subprocess.check_call("./frontend/cpagec.sh",shell=True)
