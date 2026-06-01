# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for Binance Futures Testnet. It supports placing MARKET and LIMIT orders through a command-line interface. The bot includes input validation, logging, and error handling to ensure smooth execution of orders.

The project was built as part of a Python Developer assignment and focuses on creating a simple but structured trading application.

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL operations
* Command-line interface using argparse
* Input validation
* Logging of order requests and responses
* Error handling for invalid inputs and API-related issues

## Project Structure

trading_bot/

├── bot/

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

│

├── logs/

├── cli.py

├── requirements.txt

├── README.md

└── .env.example

## Installation

1. Clone the repository:

git clone https://github.com/tiwarikanjali-18/binance-futures-trading-bot.git

cd binance-futures-trading-bot

2. Install the required packages:

pip install -r requirements.txt

3. Create a `.env` file and add your Binance Futures Testnet credentials:

API_KEY=your_api_key

API_SECRET=your_api_secret

## Usage

MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000

## Logging

All order requests, responses, and errors are stored in:

logs/trading.log

## Assumptions

* Binance Futures Testnet account is active.
* API credentials are valid.
* Symbol, quantity, and price values follow Binance Futures requirements.

## Testing

The following scenarios were tested successfully:

* MARKET BUY order on BTCUSDT
* LIMIT SELL order on BTCUSDT
* Logging of order requests and responses
* Input validation and exception handling

## Technologies Used

* Python 3
* python-binance
* python-dotenv
* Binance Futures Testnet API

## Author

Anjali Tiwari
