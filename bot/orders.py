from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Order Request: {symbol} {side} {order_type} {quantity}"
        )

        if order_type.upper() == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )

        else:

            response = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:

        logger.error(str(e))
        raise