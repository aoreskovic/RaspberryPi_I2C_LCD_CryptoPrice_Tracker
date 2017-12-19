import I2C_LCD_driver
import json
import requests
from time import *


sleep(5)
response = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=14")

mylcd1 = I2C_LCD_driver.lcd(0x27)
mylcd2 = I2C_LCD_driver.lcd(0x26)

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



mylcd1.lcd_clear()
mylcd1.lcd_display_string("BTC " + getPrice("BTC") + " $ " + getChange("BTC") + "%", 1, 0)
mylcd1.lcd_display_string("ETH " + getPrice("ETH") + " $ " + getChange("ETH") + "%", 2, 0)
mylcd1.lcd_display_string("LTC " + getPrice("LTC") + " $ " + getChange("LTC") + "%", 3, 0)
mylcd1.lcd_display_string("ADA " + getPrice("ADA") + " $ " + getChange("ADA") + "%", 4, 0)

mylcd2.lcd_clear()
mylcd2.lcd_display_string("XRP " + getPrice("XRP") + " $ " + getChange("XRP") + "%", 1, 0)
mylcd2.lcd_display_string("IOT " + getPrice("MIOTA") + " $ " + getChange("MIOTA") + "%", 2, 0)
mylcd2.lcd_display_string("NEM " + getPrice("XEM") + " $ " + getChange("XEM") + "%", 3, 0)
mylcd2.lcd_display_string("EOS " + getPrice("EOS") + " $ " + getChange("EOS") + "%", 4, 0)
    


    
    