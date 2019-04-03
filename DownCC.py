import requests
import json

def check_json(input_data):
    try:
        json.loads(input_data)
        return True
    except:
        return False


# find file_id in http://cc.sjtu.edu.cn/portal/Resource/detail.aspx?id={file_id}
file_id = ''

if (not file_id):
    file_id = input("Please input file id:")

json_url = "http://cc.sjtu.edu.cn/Portal/Ashx/Resource.ashx?action=File_Portal_Get&FileID=" + str(file_id)

json_req = requests.get(json_url)
if(json_req.status_code != 200 or not check_json(json_req.content)):
    print("Failed: unable to get json data")
    exit()
json_data = json.loads(json_req.content)
down_url = json_data["DownURL"]
file_title = json_data["FileTitle"]

file_req = requests.get(down_url)
if(file_req.status_code == 200):
    open(str(file_title),"wb").write(file_req.content)
    print("Success")
else:
    print("Failed: unable to get document file")
