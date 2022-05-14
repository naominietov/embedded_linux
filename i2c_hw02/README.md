# 📚 Assignment 2. Show messages on LCD via I2C remotely

<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]

* TE2003B. System Design on Chip 
* Embedded Linux

<!-- TABLE OF CONTENTS -->
## 📌 Table of Contents
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 🔍 About The Project

This assignment seeks to enable the I2C ports on the Raspberry in order to write to the LCD using I2C module remotely. 

<!-- GETTING STARTED -->
## 🚀 Getting Started

### ✅ Prerequisites and Installation

In order to run this project, some software prerequisites that need to be installed (in case they are not already installed):

* Pip
  ```shell
  sudo apt install python3-pip -y
  ```

* I2C Tools
  ```shell
  sudo apt-get install i2c-tools
  ```

  To verify the I2C tools installation run 
  ```shell
  sudo i2cdetect -y 1 
  ```

* CircuitPython I2C library
[CircuitPython](https://github.com/dhalbert/CircuitPython_LCD) library for HD77480 LCD character displays with an I2C backpack which supports I2C model PCF8574. 
For other models such as I2C MC2300XXX the [Adafruit](https://github.com/adafruit/Adafruit_CircuitPython_CharLCD) library is supported. 

* FastAPI and HTTP Server
In order to run the web app using Python we used [FastAPI](https://fastapi.tiangolo.com/#installation).
  ```shell
  pip install fastapi
  pip install "uvicorn[standard]"
  ```
  
* Node Red
  ```shell
  bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)![image](https://user-images.githubusercontent.com/64105772/167316004-0f5ab937-eea4-45a5-8d87-fba480a384a2.png)
  ```

<!-- USAGE EXAMPLES -->
## 💻 Usage example

1. Make the physical connections.
2. Download main.py file
3. To run the project, open a new bash and run the following command to connect to the server
    ```shell
    python -m uvicorn main:app --reload
    ```
2. Connect to [HiveMQ MQTT Broker Client](http://www.hivemq.com/demos/websocket-client/)
3. Then, to open NodeRED run:
    ```shell
    node-red-start
    ```
    and upload the flows.json file.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## 📩 Contact

* Name: Naomi Estefanía Nieto Vega
* ID: A01706095
* Email: a01706095@tec.mx

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## 🎉 Acknowledgments

* Porfessor Ing. Jesús Antonio Pérez Reyes [contact](mailto:antonio.perez@tec.mx)

<p align="right">(<a href="#top">back to top</a>)</p>

## 📎 References

* Adafruit not compatible
https://stackoverflow.com/questions/59482708/can-i-set-the-address-of-an-i2c-lcd-in-circuitpython-for-something-other-than-20
* https://github.com/dhalbert/CircuitPython_LCD
* https://github.com/dbrgn/RPLCD
* https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md
* https://pinout.xyz/pinout/i2c
* https://fastapi.tiangolo.com/tutorial/first-steps/

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/naominietov/
