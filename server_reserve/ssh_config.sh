if [ $1 == "help" ]
then
        echo "Arguments required:ip_remote,username_remote"  
fi
#$1=ip
#$2=username
#ssh -t $2@$1 "sudo chmod 746 /etc/ssh/sshd_config" 
#echo "Change PermitRootLogin to 'yes'"
#ssh -t $2@$1 " vim /etc/ssh/sshd_config & sudo ssh service restart"
if ! grep -q "Host:" "CPU_config_file.txt";
then
	ssh-keygen -t rsa
fi
#echo "Add:'admin ALL=(ALL) NOPASSWD:ALL' to the end of file"
ssh -t $2@$1 "adduser admin_awgs"
ssh -t $2@$1 " echo "admin_awgs:rtp" | chpasswd"
ssh -t $2@$1 "echo 'admin_awgs ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers"
#ssh -t $2@$1 "sudo su admin & sudo visudo"
ssh -t $2@$1 "sudo service ssh restart & sudo chown -R admin_awgs /home/admin_awgs"
echo "password:rtp"

#cat ~/.ssh/id_rsa.pub | ssh admin@$1 "sudo mkdir -p /home/.ssh && cat >>  /home/.ssh/authorized_keys"
ssh-copy-id admin_awgs@$1
echo "test"
ssh-add
if ! grep -q "$1" "CPU_config_file.txt"; 
then
	echo "Host:$2 IP:$1">>CPU_config_file.txt
fi

