import requests
import json
import pandas as pd

url = 'http://127.0.0.1:5000/recognition/recognition_images'
path_images = 'recognition/data/test/negative/Copia de TREP 13.jpg'

path = {
"images": path_images
}




n = json.dumps(path)
output = json.loads(n)
df = pd.io.json.json_normalize(output)


r = requests.post(url,json= output)
print(r.json())

