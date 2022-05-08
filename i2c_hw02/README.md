# Assignment 2. Show messages on LCD via I2C remotely

<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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
  pip install "uvicorn[standard]"
  ```
* Node Red
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)![image](https://user-images.githubusercontent.com/64105772/167316004-0f5ab937-eea4-45a5-8d87-fba480a384a2.png)
```

<!-- USAGE EXAMPLES -->
## Usage

To run the project, connect 
```
python -m uvicorn main:app --reload
```
Open NodeRED
```
node-red-start

```

_For more examples, please refer to the [Documentation](https://example.com)_

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


## Useful Links

*

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/naominietov/embedded_linux.svg?style=for-the-badge
[contributors-url]: https://github.com/naominietov/embedded_linux/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/naominietov/embedded_linux.svg?style=for-the-badge
[forks-url]: https://github.com/naominietov/embedded_linux/network/members
[stars-shield]: https://img.shields.io/github/stars/naominietov/embedded_linux.svg?style=for-the-badge
[stars-url]: https://github.com/naominietov/embedded_linux/stargazers
[issues-shield]: https://img.shields.io/github/issues/naominietov/embedded_linux.svg?style=for-the-badge
[issues-url]: https://github.com/naominietov/embedded_linux/issues
[license-shield]: https://img.shields.io/github/license/naominietov/embedded_linux.svg?style=for-the-badge
[license-url]: https://github.com/naominietov/embedded_linux/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/naominietov/
[product-screenshot]: images/screenshot.png

To run the 
```
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```


Useful links:
Adafruit not compatible
https://stackoverflow.com/questions/59482708/can-i-set-the-address-of-an-i2c-lcd-in-circuitpython-for-something-other-than-20

https://github.com/dhalbert/CircuitPython_LCD
https://github.com/dbrgn/RPLCD
https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md
