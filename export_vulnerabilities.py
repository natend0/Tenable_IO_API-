#Creates an export UUID High and critical vulnerabilites from Tenable in the open status from 6/8/2022 to today
#will need to run Download_vulnerabilities_chunk.py to download the export. 
import requests

url = "https://cloud.tenable.com/vulns/export"

payload = {"filters": {
        "severity": ["critical,high"],
        "state": ["open"],
        "first_found": 1654733304
    }}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-ApiKeys": "accessKey=<insert_key>;secretKey=<insertkey>"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
