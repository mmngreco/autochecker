# Auto Checker

Little script to do a check in / check out from in a web page.

Requires:

* python3
* Chrome
* chromedriver

## Installation

1. Fill `config.ini` file with your data.
1. Download [chromedriver](./driver/README.md) if you haven't downloaded yet.
    1. Check your chrome version, writting: `chrome://settings/help`.
    1. Download the driver [here](https://chromedriver.chromium.org/downloads) compatible with your version of chrome.
    1. Extracts the zip and put the binary file on the `drive` folder.
1. Create an isolated environment:
    1. `conda install -n autochecker python=3.6 pip=18`
    1. `conda activate autochecker`
    1. `pip install -r requirements.txt`

## Usage

1. Run the checker:
    1. `python main.py`
1. Alias bash (you should replace the first path with yours)
    1. `echo alias etscheck='~/miniconda3/envs/autochecker/bin/python ~/autochecker/main.py' >> .bash_profile`
    1. Reload your shell.
    1. then you can just run `etscheck` to turn on/off your tracking time.


