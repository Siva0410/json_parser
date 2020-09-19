import json

def write_dockerfile(json_dict):
    
    with open('Dockerfile',mode='w') as f:
        if json_dict["OS_version"] != None:
            f.write('FROM ' + json_dict["OS"] + ':' + json_dict["OS_version"] + '\n')
        else:
            f.write('FROM ' + json_dict["OS"] + '\n')
        f.write('LABEL maintainer="ichi"\n')
        f.write('RUN echo "Now building"\n')
        f.write('RUN apt-get update && apt-get install -y tzdata\n')
        f.write('ENV TZ=Asia/Tokyo\n')
        if json_dict["app_version"] != None:
            f.write('RUN apt-get update && apt-get -y install ' + json_dict["app"] + str(json_dict["app_version"]) + '\n')
        else:
            f.write('RUN apt-get update && apt-get -y install ' + json_dict["app"] +'\n')
        f.write('EXPOSE 80\n')
        f.write('CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]\n')
        
#json -> dictionary type
json_file = open('docker_info.json', 'r')
json_dict = json.load(json_file)

write_dockerfile(json_dict)
