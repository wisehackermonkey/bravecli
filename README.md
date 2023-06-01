# bravecli
----
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h2 align="center">bravecli</h2>

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
git clone https://github.com/wisehackermonkey/bravecli.git
cd bravecli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 




# Usage
### 
```bash

# Only listing title, description, and url from results
python bravecli.py web_search "adele dazeem" --list

# Basic usage with only the required arguments RAW OUTPUT
python bravecli.py web_search "adele dazeem"


# Saving results to a file
python bravecli.py web_search "adele dazeem" --save output.json

# Turning off safe search
python bravecli.py web_search "xxx" --safesearchoff

# Turning off safe search and saving results to a file
python bravecli.py web_search "adele dazeem" --safesearchoff --save output.json

# Turning off safe search and only listing title, description, and url from results
python bravecli.py web_search "xxx" --safesearchoff --list

# Saving results to a file and only listing title, description, and url from results
python bravecli.py web_search "adele dazeem" --save output.json --list

# All options at once
python bravecli.py web_search "adele dazeem" --safesearchoff --save output.json --list

```





-----------------
# Development
### 
```bash
# Install development dependencies
pip install -r requirements_dev.txt

# Run tests
pytest 

# or run
pytest test_bravecli.py
# how to create exe
pyinstaller --onefile -i favicon.ico bravecli.py

```










 -----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/bravecli)](https://github.com/wisehackermonkey/bravecli/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------


# License

#### MIT © wisehackermonkey
<img src="https://149753425.v2.pressablecdn.com/wp-content/uploads/2009/06/OSI_Standard_Logo_100X130.png" width="80">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20230601
```