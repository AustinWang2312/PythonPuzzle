import re
import json 
import subprocess
import os






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
#	print(match_ips)
#	print(match_hosts)

d={} 
for ip in match_ips:
	subprocess.check_call(["./CPU.sh",ip,"admin_awgs"])
	with open(file_input_name) as f:
		contents =f.read()
#		match_mac=re.findall('HWaddr (\S+)',contents)
		match_host_name=re.search('Host Name:(.*?)Kernel:',contents,re.S)
		host_name=match_host_name.group(1) if match_host_name else None 	
		host_name=re.sub('\s+',"",host_name)
		
		match_kernel=re.search('\Kernel:(.*?)\Distribution',contents,re.S)
		kernel=match_kernel.group(1) if match_kernel else None 	
#		print(kernel)
		kernel=str.strip(kernel)
	
		match_distribution=re.search('Distribution:(.*?)Users',contents,re.S)
		distribution=match_distribution.group(1) if match_distribution else None 	
			
#		distribution=distribution.rstrip()
#		distribution="".join(distribution.split('\n'))
		distribution=re.sub('\s+'," ",distribution)
#		print(distribution)
		
		match_users=re.search('Users:(.*?)Network Interface:',contents,re.S)
		users=match_users.group(1) if match_users else None 	
#		users=re.sub('\s+'," ",users)
#		print(users)
				
		match_network_interface=re.search('Network Interface:(.*?)CPU Architecture:',contents,re.S)
		network_interface=match_network_interface.group(1) if match_network_interface else None 	
#		network_interface=re.sub('\s+'," ",network_interface)
#		print(network_interface)
		

		match_CPU=re.search('CPU Architecture:(.*?)Memory Info:',contents,re.S)
		CPU=match_CPU.group(1) if match_CPU else None 	
#		CPU=re.sub('\s+'," ",CPU)
#		print(CPU)

		match_memory=re.search('Memory Info:(.*?)End',contents,re.S)
		memory=match_memory.group(1) if match_memory else None 	
#		memory=re.sub('\s+'," ",memory)
#		print(memory)
		d["Host:"+host_name+"@"+ip]={}	
		d["Host:"+host_name+"@"+ip]["Kernel:"]=kernel
		d["Host:"+host_name+"@"+ip]["Distribution:"]=distribution
		d["Host:"+host_name+"@"+ip]["Users:"]=users
		d["Host:"+host_name+"@"+ip]["Network Interface:"]=network_interface
		d["Host:"+host_name+"@"+ip]["CPU Architecture:"]=CPU
		d["Host:"+host_name+"@"+ip]["Memory Info:"]=memory
#		open(file_input_name, 'w').close()
		
#print(d)
#	for i in match_kernel:
#		str.strip(i)
#		print(i)
#	print(match_kernel)
	
#content={"mac_address":mac}
json_str=json.dumps(d,indent=1)
#json_str=json_str.replace('\\n','\n')
#print(json_str)

with open(file_output_name, "w") as fout:
#	json.loads((json_str), fout)
	fout.write (json_str)
#subprocess.check_call("./dynamic.py",shell=True)
os.system("python3 ./frontend/dynamic.py")
#with open(file_input_name, "rb") as fin:
#    content = json.load(str(fin))
#with open(file_output_name, "wb") as fout:
#    json.dump(content, fout, indent=1)
#all_variables=["~/PythonPuzzle/CPU.sh", remote_ip, remote_user, your_ip, your_user]
#subprocess.call([ "/home/austin/PythonPuzzle", "./CPU.sh" , remote_ip , remote_user , your_ip , your_user , shell=True ])
#subprocess.run(["/home/austin/PythonPuzzle", "/.CPU.sh"] +[remote_ip] +[remote_user] +[your_ip] +[your_user],shell=True)
##subprocess.Popen(["./CPU.sh",remote_ip,remote_user], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#subprocess.run("./test.sh",shell=True)
