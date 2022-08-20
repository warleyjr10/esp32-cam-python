from PIL import Image
import requests
from io import BytesIO
import os, sys
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)
d1 = str(datetime_object)
output = d1.replace(":","")
output = output.replace(" ","_")
output = output[0:17]+".jpg"
print(output)
# url da camera
url = "http://192.168.0.117/1280x1024.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

try:
    img.save('imagens/'+output)
except IOError:
    print("não foi possivel converter")