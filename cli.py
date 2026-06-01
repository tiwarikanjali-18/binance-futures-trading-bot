import argparse

from bot.orders import place_order
from bot.validators import validate_order


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_order(
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        print("\n===== ORDER RESPONSE =====")
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])

        if "avgPrice" in response:
            print("Average Price:", response["avgPrice"])

        print("\nSUCCESS")

    except Exception as e:

        print("\nFAILED")
        print(str(e))


if __name__ == "__main__":
    main()