import I2C_LCD_driver
import json
import requests
from time import *


sleep(5)
response = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=15")

mylcd = I2C_LCD_driver.lcd()

parsedData = response.json()

def getPrice(coin):
    for name in parsedData:
        if name["symbol"] == coin:
            return (name["price_usd"]+"00")[0:7]
    return 0

def getChange(coin):
    for name in parsedData:
        if name["symbol"] == coin:
            if name["percent_change_1h"][0] == "-":
                return name["percent_change_1h"]
            else:
                return "+" + (name["percent_change_1h"]+"0")[0:3]
    return 0



mylcd.lcd_clear()
mylcd.lcd_display_string("BTC " + getPrice("BTC") + " $ " + getChange("BTC") + "%", 1, 0)
mylcd.lcd_display_string("ETH " + getPrice("ETH") + " $ " + getChange("ETH") + "%", 2, 0)
mylcd.lcd_display_string("LTC " + getPrice("LTC") + " $ " + getChange("LTC") + "%", 3, 0)
mylcd.lcd_display_string("ADA " + getPrice("ADA") + " $ " + getChange("ADA") + "%", 4, 0)
#mylcd.lcd_display_string("XRP " + getPrice("XRP"), 4, 10)
#mylcd.lcd_display_string("IOT " + getPrice("MIOTA"), 3, 0)
    


    
    