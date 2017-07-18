import json
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
		jsondata = json.load(f)
		
		print(jsondata, file = r)
		print("</body>", file = r)
		print("</html>", file = r)

subprocess.check_call("./frontend/cpagec.sh",shell=True)	
