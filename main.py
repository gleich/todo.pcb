import requests
import microdotphat
import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import textwrap

tasks = requests.get(
    "https://api.mattglei.ch/things/cache", headers={"Authorization": "Bearer 1234"}
).json()

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()


while True:
    for task in tasks["today_todos"]:
        text = task["name"]
        if len(text) < 10:
            font_size = 20
        else:
            font_size = 15
        font = ImageFont.truetype("./Helvetica.ttc", font_size)
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.text(
            (0, 0),
            "\n".join(textwrap.wrap(text, width=15)),
            font=font,
            fill=255,
        )
        oled.image(image)
        oled.show()
        time.sleep(2)

time.sleep(10)
