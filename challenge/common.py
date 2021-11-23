import os
from urllib.parse import urlparse

import redis
from flask_caching import Cache

url = urlparse(os.environ.get('REDIS_URL'))
r = redis.Redis(host=url.hostname, port=url.port, username=url.username,
                password=url.password, ssl=os.environ.get('REDIS_SSL', False),
                ssl_cert_reqs=None)

cache = Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': r,
})
