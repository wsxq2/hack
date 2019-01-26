# get active ip
sed -ne '/.*/{s/^Host: \([0-9.]\+\) .*/\1/p}' a

# get ssh-active ip
sed -ne '/22\/open\/tcp/{s/^Host: \([0-9.]\+\) (.*/\1/p}' a

# get domain-name-haved ip and domain-name
sed -ne '/.*/{s/^Host: \([0-9.]\+ ([^)]\+)\).*/\1/p}' a

# get ssh-active and domain-name-haved ip and domain-name
sed -ne '/22\/open\/tcp/{s/^Host: \([0-9.]\+ ([^)]\+)\).*/\1/p}' a

