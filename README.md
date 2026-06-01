# Binance Futures Testnet Trading Bot

## Overview

This project is a simple trading bot developed in Python for Binance Futures Testnet. It allows users to place MARKET and LIMIT orders through a command-line interface while maintaining proper validation, logging, and error handling.

The project was created as part of the PrimetradeAI Python Developer application task.

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- Command-line interface using argparse
- Input validation
- Logging of requests and responses
- Error handling for invalid inputs and API issues

## Project Structure

trading_bot/
│
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

git clone <repository-url>
cd trading_bot

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file and add your Binance Futures Testnet API credentials:

API_KEY=your_api_key
API_SECRET=your_api_secret

## Usage

MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000

## Logging

All order requests, responses, and errors are recorded in:

logs/trading.log

## Assumptions

- Binance Futures Testnet account is active.
- API credentials are valid.
- Quantity and price values are provided according to Binance Futures requirements.

## Sample Results

Successfully tested:
- MARKET BUY order on BTCUSDT
- LIMIT SELL order on BTCUSDT
- Request and response logging

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- Binance Futures Testnet API

## Author
Anjali Tiwari