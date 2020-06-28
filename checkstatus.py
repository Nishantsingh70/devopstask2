import os
if(os.system("$(curl -o /dev/null -s -w \"%{http_code}\" 192.168.99.106:3333/index.html)") == "200"):
    pass
else:
    with open("/status","w") as a:
         a.write("Code is not correct")
