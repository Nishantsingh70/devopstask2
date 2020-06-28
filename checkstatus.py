import os
if(os.system("$(curl -o /dev/null -s -w \"%{http_code}\" 172.17.0.2/index.php)") == "200"):
    pass
else:
    with open("/status","w") as a:
         a.write("Code is not correct")
