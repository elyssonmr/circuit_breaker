import os
from exceptions import CircuitBreakerOpen

from redis import StrictRedis

cache = StrictRedis.from_url(os.environ['REDIS_URI'])


class CircuitBreaker:
    def __init__(self, name, threshold, open_time, prefix="cb_"):
        self.cb_key = prefix + name
        self.err_count_key = prefix + name + '_error_counter'
        self.threshold = threshold
        self.open_time = open_time

    @property
    def is_open(self):
        return bool(cache.get(self.cb_key))

    def increment_errors(self):
        cache.incr(self.err_count_key, 1)

    def check_cb(self):
        err_count = int(cache.get(self.err_count_key))
        if err_count >= self.threshold:
            print('CB Tripped')
            cache.setex(
                name=self.cb_key,
                time=self.open_time,
                value=1
            )
            cache.set(self.err_count_key, 0)


def circuit_breaker_function(name, threshold, open_time, errors):
    cb = CircuitBreaker(name, threshold, open_time)

    def decorator(func):
        def wrapper(*args, **kwargs):
            if cb.is_open:
                raise CircuitBreakerOpen()

            try:
                func(*args, **kwargs)
            except Exception as ex:
                if isinstance(ex, errors):
                    cb.increment_errors()
                    cb.check_cb()
                raise ex

        return wrapper

    return decorator
