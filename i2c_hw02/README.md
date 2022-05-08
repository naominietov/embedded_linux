# Assignment 2. Show messages on LCD via I2C remotely

<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This assignment seeks to enable the I2C ports on the Raspberry in order to write to the LCD using I2C module remotely. 

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

In order to run this project, some software prerequisites that need to be installed (in case they are not already installed):

* Pip
```sh
sudo apt install python3-pip -y
```
* I2C Tools
```sh
 sudo apt-get install i2c-tools
  ```
 To verify the I2C tools installation run 
 ```sh 
 sudo i2cdetect -y 1 
 ```
* CircuitPython I2C library
CircuitPython(https://github.com/dhalbert/CircuitPython_LCD) library for HD77480 LCD character displays with an I2C backpack which supports I2C model PCF8574. For other models such as I2C MC2300XXX the Adafruit(https://github.com/adafruit/Adafruit_CircuitPython_CharLCD) library is supported. 
* HTTP Server
In order to run the web app using Python we used FastAPI[https://fastapi.tiangolo.com/#installation].
```sh
  pip install fastapi
  ```
  ```sh
  pip install "uvicorn[standard]"
  ```
* Node Red
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)![image](https://user-images.githubusercontent.com/64105772/167316004-0f5ab937-eea4-45a5-8d87-fba480a384a2.png)
```

<!-- USAGE EXAMPLES -->
## Usage

To run the project, run the following command to connect to the server
```sh
python -m uvicorn main:app --reload
```
Then, to open NodeRED run:
```sh
node-red-start
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Naomi Nieto Vega - a01706095@tec.mx

Project Link: [https://github.com/naominietov/embedded_linux](https://github.com/naominietov/embedded_linux)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Ing. Jesús Antonio Pérez Reyes](antonio.perez@tec.mx)

<p align="right">(<a href="#top">back to top</a>)</p>


## References

* Adafruit not compatible
https://stackoverflow.com/questions/59482708/can-i-set-the-address-of-an-i2c-lcd-in-circuitpython-for-something-other-than-20
* https://github.com/dhalbert/CircuitPython_LCD
* https://github.com/dbrgn/RPLCD
* https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md

<!-- MARKDOWN LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/naominietov/embedded_linux.svg?style=for-the-badge
[stars-url]: https://github.com/naominietov/embedded_linux/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/naominietov/
