#!/bin/sh

if [ $1 = "help" ]
then
	echo "Arguments required:ip_remote,username_remote"  
fi

#$1=ip
#$2=username
#$3=your ip address don't need anymore
#$4=your username don't need anymore
ssh $2@$1 "echo Kernel: & uname -r" | cat >> cpuinfo.txt
ssh $2@$1 "echo Distribution: & lsb_release -a" | cat >> cpuinfo.txt
ssh $2@$1 "echo Users: & who" | cat >> cpuinfo.txt
ssh $2@$1 "echo Network Interface: & ifconfig" | cat >> cpuinfo.txt
ssh $2@$1 "echo CPU Architecture: & lscpu; " | cat >> cpuinfo.txt
ssh -t $2@$1 "echo Memory: & sudo dmidecode --type=17 | grep -E '(Size|Speed)'">>cpuinfo.txt

#ssh $2@$1 "echo Kernel: & uname -r & echo Distribution: & lsb_release -a & echo Users: & who & echo Network Interface & ifconfig & echo CPU Architecture: & lscpu" | cat >> cpuinfo.txt
#ssh -t $2@$1 "sudo dmidecode --type=17 | grep -E '(Size|Speed)'">>cpuinfo.txt
#ssh -t $2@$1 "sudo rm /tmp/cpuinfo.txt"
 
#ssh -t $2@$1 "sudo rm /tmp/cpuinfo.txt"
 
#echo "[sudo] password for graham" 

#ssh -t $2@$1 'sudo dmidecode --type=17| grep size'|cat >>cpuinfo.json

#echo "[sudo] password for graham" 









#ssh $2@$1  {"lscpu & echo uname -r & who & ifconfig & lsb_release -a ;" } | cat > cpuinfo.json
#ssh -t $2@$1 'sudo dmidecode --type=17'
# | grep size ;" } | cat > cpuinfo.json
#free -h | ssh $3@$4 "cat >> cpuinfo.json"
#who | ssh $3@$4 "cat >> cpuinfo.json"
#ifconfig | ssh $3@$4 "cat >> cpuinfo.json"
