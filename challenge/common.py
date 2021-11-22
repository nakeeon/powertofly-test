import os

from flask_caching import Cache

cache = Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': os.environ.get('REDIS_HOST'),
    'CACHE_REDIS_PORT': os.environ.get('REDIS_PORT'),
})
