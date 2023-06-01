# braverycli
----
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h2 align="center">BraveryCLI</h2>

<h4 align="center">A command-line interface for the Brave Search API.</h4>

---

# Summary
### -  *[Installation](#Installation)*
### -  *[Usage](#Usage)*
### -  *[Deveopment](#For-developers)*
### -  *[Contributors](#Contributors)*
### -  *[Links](#Links)*
### -  *[License](#License)*

 
# Installation
### 
```bash
cd ~
git clone https://github.com/wisehackermonkey/braverycli.git
cd braverycli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 


 <!-- ----------------- -->
<!-- # Screenshots -->
<!-- - <img src="NNNNNNNNNNNNN" width="400"> -->








-----------------
# Development
### 
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```




# Usage
### 
```bash
# For web search
python brave_search.py web_search 'brave search' -l 

# For saving results to disk 
python brave_search.py web_search 'brave search' -l -s results.json

# For suggest search
python brave_search.py suggest_search 'brave search' -s results.json

# For spell check search
python brave_search.py spell_check_search 'brave search' -s results.json
```









 -----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/braverycli)](https://github.com/wisehackermonkey/braverycli/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------


# License

#### MIT © wisehackermonkey
<img src="osi-logo.png" width="100">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
__DATE___
```
<!-- 

# Docker
### Build
```bash
cd ~
git clone https://github.com/wisehackermonkey/braverycli.git
cd braverycli
docker build -t wisehackermonkey/braverycli:latest .  
```
### Run
```bash
docker run -it --rm --name wisehackermonkey/braverycli:latest  
```
### Docker-compose
```bash
docker-compose build
docker-compose up 
```
# Publish Docker Image
```bash
docker build -t wisehackermonkey/braverycli:latest .
docker login
docker push wisehackermonkey/braverycli:latest
```
# Deploy on netlify
```
npm install netlify-cli -g
netlify login
netlify deploy
netlify deploy --prod
```
-->