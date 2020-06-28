import os
for root,dirs,files in os.walk('/root/task2'):
    print(files)
    for file in files:
        if file.endswith('.php'):
           os.system("docker container run -dit -p 3333:80 --name phpcontainer -v /root/task2:/usr/local/apache2/htdocs phpweb:v1")
           
