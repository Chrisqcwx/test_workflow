import http.client

conn = http.client.HTTPSConnection("localhost", 2531)
payload = ''
headers = {}
conn.request("POST", "/tools/getTokenId", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))