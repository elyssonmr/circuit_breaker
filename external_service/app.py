import os
from flask import Flask, request
from time import sleep

from random import randint


percent_point = int(os.environ.get('PERCENT_POINT', '0'))
app = Flask(__name__)


def should_timeout():
    point = randint(1, 100)
    return percent_point >= point


@app.route('/place_order', methods=['POST'])
def place_order():
    order = request.get_json()
    if should_timeout():
        print("The server is really slow today!")
        sleep(25)

    print(f'Order: {order["number"]} placed')
    return ({'message': f'Order {order["number"]} placed'}, 201)


if __name__ == "__main__":
    print('Starting app')
    app.run()
