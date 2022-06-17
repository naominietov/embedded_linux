
## Commands I2C Assignment
* To start the HTTP server
```
python -m uvicorn main:app --reload
```
* Open NodeRED
```
node-red-start
```
* Install i2c tools
```
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

### Useful links:
* Adafruit not compatible
* https://stackoverflow.com/questions/59482708/can-i-set-the-address-of-an-i2c-lcd-in-circuitpython-for-something-other-than-20
* https://github.com/dhalbert/CircuitPython_LCD
* https://github.com/dbrgn/RPLCD

## Commands Midterm Project

* Start n8n
```
sudo docker run -it --rm \
    --name n8n \
    -p 5678:5678 \
    -v ~/.n8n:/home/node/.n8n \
    n8nio/n8n
```
### Buen comando
```
sudo docker run -it --rm \
    --name n8n \
    -p 5678:5678 \
    -v ~/.n8n:/home/node/.n8n \
    -v ~/workspace/data:/data \
    n8nio/n8n
``` 
##-------------------------------------------------
* Start grafana docker
```
sudo docker run -d --name=grafana -p 3000:3000 grafana/grafana
```
* Test docker installation
```
sudo docker run hello-world
```
## Midterm project ======================+++++++++++++++++ 
Run n8n in background
```
sudo docker run -it --rm --detach --name n8n -p 5678:5678 -v ~/workspace/data:/data -v ~/.n8n:/home/node/.n8n n8nio/n8n
```
## Start Midterm
node-red-start
python -m uvicorn main:app --reload --app-dir=~/workspace

nano ~/.zprofile

Start a tunnel to node-red
/snap/bin/ngrok http 1880

## Modo Kiosko
sudo nano /etc/xdg/openbox/autostart
chromium-browser --disable-infobars --kiosk 'http://169.254.186.53:1880/'
sudo reboot

https://dashboard.ngrok.com/tunnels/agents

https://2e05-2001-1260-203-8d44-353b-a3f0-cd2e-817e.ngrok.io
/ui/#!/0?socketid=5aJe6ic32Vbg6nOMAAAS

## Docker
Stop and remove the background container
sudo docker rm -f n8n
Run an interactive shell
sudo docker exec -it n8n /bin/sh
List all containers
sudo docker ps -a




## References

# https://www.geeksforgeeks.org/python-vlc-mediaplayer-checking-if-it-is-playing-or-not/
https://stackoverflow.com/questions/35989666/convert-milliseconds-to-hours-min-and-seconds-python