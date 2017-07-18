import subprocess
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
		brlist = ["{","}",",","\""]
		jsondata = f.read()	
		
		for i in brlist:
			jsondata = jsondata.replace(i, "<br>" )
	#	jsondata = jsondata.replace("}", "<br>" )
	#	jsondata = jsondata.replace(",", "<br>" )
	#	jsondata = jsondata.replace("\"", "<br>" )		
		jsondata = jsondata.replace("<br>: <br>", "<br>" )
		
		title = ["Memory Info:","Network Interface:","Distribution:","CPU Architecture:","Kernel:","Users:"]
		for j in title:
			jsondata = jsondata.replace(j, "<font style=\"background-color:ff8e3a\">"+j+"</font>")
		jsondata = jsondata.replace("Host:", "<font style=\"background-color: #EF4323\">Host:</font> ")
	#	jsondata = jsondata.replace("Memory Info:", "<font style=\"background-color: #ff8e3a \">Memory Info:</font> ")
	#	jsondata = jsondata.replace("Network Interface:", "<font style=\"background-color: #ff8e3a\">Network Interface:</font> ")
	#	jsondata = jsondata.replace("Distribution:", "<font style=\"background-color: #ff8e3a\">Distribution:</font> ")
	#	jsondata = jsondata.replace("CPU Architecture:", "<font style=\"background-color: #ff8e3a\">CPU Architecture:</font> ")
	#	jsondata = jsondata.replace("Kernel:", "<font style=\"background-color: #ff8e3a\">Kernel:</font> ")
	#	jsondata = jsondata.replace("Users:", "<font style=\"background-color: #ff8e3a\">Users:</font> ")

		print(jsondata, file = r)
		print("</body>", file = r)
		print("</html>", file = r)

subprocess.check_call("./frontend/cpagec.sh",shell=True)
