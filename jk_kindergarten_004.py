import io
import requests
import PIL.Image

response = requests.get("https://www.python.jp/logo.png")
PIL.Image.open(io.BytesIO(response.content))