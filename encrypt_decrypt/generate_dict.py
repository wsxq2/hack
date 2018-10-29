import string

# passwdchar=string.digits+string.lowercase
passwdchar=string.digits
passwdlen=6
passwdchar_len=len(passwdchar)
i=0
imax=passwdchar_len**passwdlen
while i < imax:
    temp=i
    passwd=''
    j=0
    while j<passwdlen:
        ch=temp%passwdchar_len
        passwd=passwd+passwdchar[ch]
        temp=temp//passwdchar_len
        j+=1
    print passwd[::-1]
    i+=1
