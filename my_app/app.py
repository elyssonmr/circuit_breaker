from flask import Flask, request

from http_client import place_order

from exceptions import CircuitBreakerOpen

app = Flask(__name__)


@app.route('/buy_course', methods=['POST'])
def buy_course():
    post_data = request.get_json()
    # TODO: Validate input data

    try:
        # place the order in the external service
        place_order(post_data['username'], post_data['order_id'])
    except CircuitBreakerOpen:
        return (
            {"message": "Can't place order right now..."
                        " Try again in 5 minutes."},
            502
        )
    except Exception:
        return (
            {"message": "There is a problem placing your order. Try again"},
            502
        )

    return ({"message": "You order was placed"}, 200)


if __name__ == "__main__":
    print("Stating app")
    app.run()
