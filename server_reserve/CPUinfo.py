import re
import json 
import subprocess







#remote_ip="10.7.190.172"
#remote_user="graham"
#your_ip="10.7.189.88"    
#your_user="austin"
file_config_name="CPU_config_file.txt"
file_input_name="cpuinfo.txt"
file_output_name="cpuinfo.json"

open(file_input_name, 'w').close()

with open(file_config_name) as f:
	contents=f.read()
	match_hosts=re.findall('Host:(\S+)',contents)
	match_ips=re.findall('IP:(\S+)',contents)
	print(match_ips)
	print(match_hosts)

for ip in match_ips:
	subprocess.check_call(["./CPU.sh",ip,"root"])

with open(file_input_name) as f:
	contents =f.read()
	match_mac=re.search('HWaddr (\S+)',contents)
	mac=match_mac.group(1) if match_mac else None 	
	print(mac)
	
content={"mac_address":mac}
json_str=json.dumps(content)
print(json_str)

with open(file_output_name, "w") as fout:
	json.loads((json_str), fout)
	fout.write (json_str)
#with open(file_input_name, "rb") as fin:
#    content = json.load(str(fin))
#with open(file_output_name, "wb") as fout:
#    json.dump(content, fout, indent=1)
#all_variables=["~/PythonPuzzle/CPU.sh", remote_ip, remote_user, your_ip, your_user]
#subprocess.call([ "/home/austin/PythonPuzzle", "./CPU.sh" , remote_ip , remote_user , your_ip , your_user , shell=True ])
#subprocess.run(["/home/austin/PythonPuzzle", "/.CPU.sh"] +[remote_ip] +[remote_user] +[your_ip] +[your_user],shell=True)
##subprocess.Popen(["./CPU.sh",remote_ip,remote_user], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#subprocess.run("./test.sh",shell=True)
