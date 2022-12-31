from PIL import Image, ImageDraw, ImageFont
import textwrap
import board
import busio
import adafruit_ssd1306
from loguru import logger


def setup():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.show()
    logger.info("setup oled display")
    return oled


def show_task(display, name: str):
    if len(name) < 10:
        font_size = 20
    else:
        font_size = 15
    font = ImageFont.truetype("./Helvetica.ttc", font_size)
    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)
    draw.text(
        (0, 0),
        "\n".join(textwrap.wrap(name, width=15)),
        font=font,
        fill=255,
    )
    display.image(image)
    display.show()
