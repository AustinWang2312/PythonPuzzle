#!/bin/sh

if [ $1 = "help" ]
then
	echo "Arguments required:ip_remote,username_remote"  
fi

#$1=ip
#$2=username
#$=your ip address don't need anymore
#$=your username don't need anymore
#$3=the random number appended to the filename

file_prefix=$3
file_suffix="cpuinfo.txt"
file_path="/home/austin/PythonPuzzle/server_reserve/"
file_ping="online.txt"
#echo $file_path$file_prefix$file_suffix
timeout 0.2 ping -c 1 $1 ; echo $? > "$file_path$file_prefix$file_ping"
#nc -vv -z $1 22 > online.txt 2>&1
if  grep -q "0" "$file_path$file_prefix$file_ping" ; then
	ssh $2@$1 "echo Host Name: & hostname" | cat > "$file_path$file_prefix$file_suffix"
	ssh $2@$1 "echo Kernel: & uname -r" | cat >> "$file_path$file_prefix$file_suffix"
	ssh $2@$1 "echo Distribution: & lsb_release -a" | cat >> "$file_path$file_prefix$file_suffix"
	ssh $2@$1 "echo Users: & who" | cat >> "$file_path$file_prefix$file_suffix"
	ssh $2@$1 "echo Network Interface: & ifconfig" | cat >> "$file_path$file_prefix$file_suffix"
	ssh $2@$1 "echo CPU Architecture: & lscpu; " | cat >> "$file_path$file_prefix$file_suffix"
	ssh -t -t $2@$1 "echo Memory Info: & sudo dmidecode --type=17 | grep -E '(Size|Speed)'">>"$file_path$file_prefix$file_suffix"
	ssh -t -t $2@$1 "echo End" |cat >>"$file_path$file_prefix$file_suffix"
else 
	echo Host Name:OFFLINE | cat >"$file_path$file_prefix$file_suffix"
	echo Kernel:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo Distribution:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo Users:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo Network Interface:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo CPU Architecture:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo Memory Info:OFFLINE | cat >>"$file_path$file_prefix$file_suffix"
	echo End | cat >>"$file_path$file_prefix$file_suffix"
fi

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

