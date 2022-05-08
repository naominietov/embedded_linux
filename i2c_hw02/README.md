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

* The HTTP Server
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



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
https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md