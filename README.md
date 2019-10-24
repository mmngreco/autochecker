# Auto Checker

Little script to do a check in / check out from in a web page.

Requires:

* python3
* Chrome
* chromedriver

# Installation

1. Fill `config.ini` file with your data.
1. Download [chromedriver](./driver/README.md) if you haven't downloaded yet.
1. First check your chrome version,
1. ["About Chrome Section"](chrome://settings/help). Then goes to driver [downloads
page](https://chromedriver.chromium.org/downloads) and choose a driver
compatible with your version of chrome. Extracts the binary in `drive` folder.
1. Create an isolated environment:
    1. `conda install -n autochecker python=3.6 pip=18`
    1. `conda activate autochecker`
    1. `pip install -r requirements.txt`

# Usage

1. Run the checker:
    1. `python main.py`
1. Alias bash
    1. `echo alias etscheck='~/miniconda3/envs/autochecker/bin/python ~/autochecker/main.py' >> .bash_profile`
    1. then you can just run `etscheck` to turn on/off your tracking time.

