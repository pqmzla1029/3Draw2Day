import http.client

conn = http.client.HTTPConnection("api,playment,in")

payload = "{\n  \"reference_id\": \"sample_reference_id\",\n  \"data\": {\n    \"frames\": [\n      {\n        \"frame_id\": \"frame001\",\n        \"src\": \"https://dummyimage.com/600x400/000/fff.jpg&text=Dummy+Image+1\"\n      },\n      {\n        \"frame_id\": \"frame002\",\n        \"src\": \"https://dummyimage.com/600x400/000/fff.jpg&text=Dummy+Image+2\"\n      },\n      {\n        \"frame_id\": \"frame003\",\n        \"src\": \"https://dummyimage.com/600x400/000/fff.jpg&text=Dummy+Image+3\"\n      },\n      {\n        \"frame_id\": \"frame004\",\n        \"src\": \"https://dummyimage.com/600x400/000/fff.jpg&text=Dummy+Image+4\"\n      },\n      {\n        \"frame_id\": \"frame005\",\n        \"src\": \"https://dummyimage.com/600x400/000/fff.jpg&text=Dummy+Image+5\"\n      }\n    ],\n    \n  },\n  \"tag\": \"object_tracking\"\n}"

headers = {
    'x-client-key': "<your x-client-key here>",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }

conn.request("POST", "v1,project,:projectId,feedline", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
