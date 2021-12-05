import os
import argparse
from kafka import KafkaConsumer
from json import loads


def create_consumer(brokers, topic, group, offset='end'):
    grp = group
    if group == "-1"or group == "None":
        grp = None
    return KafkaConsumer(
                topic,
                bootstrap_servers=brokers,
                auto_offset_reset=offset,
                enable_auto_commit=True,
                group_id=grp,
                value_deserializer=lambda x: loads(x.decode('utf-8'))
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buy/Sell signal consumer.')
    parser.add_argument('-b', '--brokers', default='127.0.0.1:9092', type=str,
                        help="Kafka brokers to consume from")
    parser.add_argument('-t', '--topic', default='okxexecutor', type=str,
                        help="Kafka trading signal for ETH-USDT-SWAP, okex exchange")

    args = parser.parse_args()

    group = None
    brokers = []
    brokers.append(args.brokers)

    print(brokers, args.topic)

    consumer = create_consumer(brokers, args.topic, group, 'latest')
    try:
        consumer.poll()
        consumer.seek_to_end()
    except: pass

    for message in consumer:
        msg = message.value
        if 'trigger' in msg and msg['trigger'] in ('position','snapshot'):
            continue # skipping message

        print(msg)

        # TODO: use signal here


        
