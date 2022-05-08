Needed:
```
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

To start the HTTP server
```
python -m uvicorn main:app --reload
```
Open NodeRED
```
node-red-start

```

Useful links:
Adafruit not compatible
https://stackoverflow.com/questions/59482708/can-i-set-the-address-of-an-i2c-lcd-in-circuitpython-for-something-other-than-20

https://github.com/dhalbert/CircuitPython_LCD
https://github.com/dbrgn/RPLCD
