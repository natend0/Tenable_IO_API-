#This will need to be run after running the Export vulnerabilities.py script. 
# You will need the UID generated in the response after running the Export_vulnerabilities.py for this script. 
import requests

url = "https://cloud.tenable.com/vulns/export/%3CENTER_UUID%3E/status"

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=<insert_key>;secretKey=<insertkey>"
}

response = requests.get(url, headers=headers)

print(response.text)
