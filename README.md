little-zebra
============

This Telegram bot shows how easy it is to decode barcodes.

## Setup
Install ZBar library, it is used for detecting and decoding barcodes of different types.

macOS
```commandline
brew install zbar
```

Ubuntu
```commandline
sudo apt-get install libzbar-dev libzbar0
```

Next install bot dependencies
1. aiogram - asynchronous framework for Telegram Bot API
1. PIL - package to work with images 
1. pyzbar - package to work with ZBar library

```commandline
pip install -r requirements.txt
```