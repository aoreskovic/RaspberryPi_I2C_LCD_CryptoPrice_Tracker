# Raspberry Pi I2C LCD Tracker of cryptocurrency prices
Small python project for Raspberry Pi that fetches the prices from https://coinmarketcap.com/ and shows them on I2C 20x4 charachter LCD.

It's a small Python script that is run every 5 minutes by Cron (that's how often CoinMarketCap refreshes their public API data).

![Finished project on Rapbery Pi - I2C LCD displaying prices of BTC, ETH, LTC and ADA](https://raw.githubusercontent.com/aoreskovic/RaspberryPi_I2C_LCD_CryptoPrice_Tracker/master/20171217_164318.jpg)

Cron job:

```*/5 * * * * python3 /home/pi/Desktop/I2C_ekran/main.py```

Possible future improvements:
 * Scrolling screen to show more currencies
 * Task scheduling using some python library
 * Find API that refreshes faster
