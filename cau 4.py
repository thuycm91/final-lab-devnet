import requests
import json
requests.packages.urllib3.disable_warnings()
baseUrl = "https://api.meraki.com/api/v1"
API_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "681155"
def get_org():
    url = baseUrl + f"/organizations/{org_id}/inventory/devices"
    header = {
        "X-Cisco-Meraki-API-Key" : API_key
    }
    response= requests.get(url,headers=header,verify=False)
    data=response.json()
    parse_data=json.dumps(data,indent=4)
    print(f"câu B:/n{parse_data}")
    # print(data)
    # print(type(data))
    device_null=[]
    for i in data:
        if i['networkId']==None:
            device_null.append(i)
    parse_data=json.dumps(device_null,indent=4)     
    print(f"Cau C: /n{json.dumps(device_null, indent=4)}")   
    
if __name__ == "__main__":
    get_org()