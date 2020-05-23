from uuid import uuid4

from locust import HttpUser, between, task


class CircuitBreakerTester(HttpUser):
    wait_time = between(0.2, 0.400)

    @task
    def buy_course(self):
        request_data = {
            "username": "elyssonmr",
            "order_id": str(uuid4())
        }
        self.client.post('/buy_course', json=request_data)
