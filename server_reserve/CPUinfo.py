import re
import json 
import subprocess
import os
import sys


#print(sys.argv[1])


file_config_name="/home/austin/server_reserve/CPU_config_file.txt"
file_input_name="/home/austin/server_reserve/"+sys.argv[1]+"cpuinfo.txt"
file_output_name="/home/austin/server_reserve/"+sys.argv[1]+"cpuinfo.json"

open(file_input_name, 'w').close()

with open(file_config_name) as f:
	contents=f.read()
#	match_hosts=re.findall('Host:(\S+)',contents)
	match_ips=re.findall('IP:(\S+)',contents)

d={} 
for ip in match_ips:
	subprocess.check_call(["/home/austin/server_reserve/CPU.sh",ip,"admin_awgs",sys.argv[1]])
	with open(file_input_name) as f:
		contents =f.read()
		match_host_name=re.search('Host Name:(.*?)Kernel:',contents,re.S)
		host_name=match_host_name.group(1) if match_host_name else None 	
		host_name=re.sub('\s+',"",host_name)
		
		match_kernel=re.search('\Kernel:(.*?)\Distribution',contents,re.S)
		kernel=match_kernel.group(1) if match_kernel else None 	
		kernel=str.strip(kernel)
	
		match_distribution=re.search('Distribution:(.*?)Users',contents,re.S)
		distribution=match_distribution.group(1) if match_distribution else None 	
			
		distribution=re.sub('\s+'," ",distribution)
		
		match_users=re.search('Users:(.*)Network Interface:',contents,re.S)
		users=match_users.group(1) if match_users else None 	
		amount=re.split('\\n',users)
		print_amount="Total:"+str(len(amount)-2)		
		match_network_interface=re.search('Network Interface:(.*?)CPU Architecture:',contents,re.S)
		network_interface=match_network_interface.group(1) if match_network_interface else None 	
		

		match_CPU=re.search('CPU Architecture:(.*?)Memory Info:',contents,re.S)
		CPU=match_CPU.group(1) if match_CPU else None 	

		match_memory=re.search('Memory Info:(.*?)End',contents,re.S)
		memory=match_memory.group(1) if match_memory else None 	
		d["Host:"+host_name+"@"+ip]={}	
		d["Host:"+host_name+"@"+ip]["Kernel:"]=kernel
		d["Host:"+host_name+"@"+ip]["Distribution:"]=distribution
		d["Host:"+host_name+"@"+ip]["Users:"]=users+str(print_amount)
		d["Host:"+host_name+"@"+ip]["Network Interface:"]=network_interface
		d["Host:"+host_name+"@"+ip]["CPU Architecture:"]=CPU
		d["Host:"+host_name+"@"+ip]["Memory Info:"]=memory
		
json_str=json.dumps(d,indent=1)

with open(file_output_name, "w") as fout:
	fout.write (json_str)
python_execute_dynamic_string="python3 /home/austin/server_reserve/frontend/dynamic.py "+str(sys.argv[1])

os.system(python_execute_dynamic_string)
#with open(file_input_name, "rb") as fin:
#    content = json.load(str(fin))
#with open(file_output_name, "wb") as fout:
#    json.dump(content, fout, indent=1)
#all_variables=["~/PythonPuzzle/CPU.sh", remote_ip, remote_user, your_ip, your_user]
#subprocess.call([ "/home/austin/PythonPuzzle", "./CPU.sh" , remote_ip , remote_user , your_ip , your_user , shell=True ])
#subprocess.run(["/home/austin/PythonPuzzle", "/.CPU.sh"] +[remote_ip] +[remote_user] +[your_ip] +[your_user],shell=True)
##subprocess.Popen(["./CPU.sh",remote_ip,remote_user], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#subprocess.run("./test.sh",shell=True)
