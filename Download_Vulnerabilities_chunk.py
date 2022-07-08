#After running the export vulnerabilites to get the UUID and the Get vulnerabilities export status to get the Chunk IDs, you can run this script to download the results. 
import requests

url = "https://cloud.tenable.com/vulns/export/%3CEnterUUID%3E/chunks/%3CEnter_ChunkID%3E"

headers = {
    "Accept": "application/octet-stream",
    "X-ApiKeys": "accessKey=<insert_key>;secretKey=<insertkey>"
}

response = requests.get(url, headers=headers)

print(response.text)
