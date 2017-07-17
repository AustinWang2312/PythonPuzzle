if [ $1 == "help" ]
then
        echo "Arguments required:ip_remote,username_remote"  
fi
#$1=ip
#$2=username
ssh -t $2@$1 "sudo chmod 746 /etc/ssh/sshd_config" 
echo "Change PermitRootLogin to 'yes'"
ssh -t $2@$1 " vim /etc/ssh/sshd_config"
ssh-keygen -t rsa
ssh-copy-id root@$1
ssh-add
if ! grep -q "$1" "CPU_config_file.txt"; 
then
	echo "Host:$2 IP:$1">>CPU_config_file.txt
fi

