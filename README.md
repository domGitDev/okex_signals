# AI generated Long/Short position signals for ETH-USDT-SWAP (Okex exchange)

### INSTALL packages

pip install kafka-python==2.0.2 argparse==1.1 json==2.0.9

### How to run in command line

python signal_consumer.py -b 94.202.126.117 -t okxexecutor

### Signal sample (side 1 == BUY and -1 == SHORT)

{'epoch': 1638724064, 'trigger': 'new', 'orders': [{'symbol': 'ETH-USDT-SWAP', 'date': 1211205, 'time': 2107, 'side': -1, 'price': 4122.85, 'stopPrice': -1, 'amount': 1, 'position': -1, 'timestamp': 1638724064}]}


