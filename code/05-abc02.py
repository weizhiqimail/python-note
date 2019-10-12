# -*- encoding: utf-8 -*-
import abc


class CacheBase(metaclass=abc.ABCMeta):

    # @abc.abstractmethod 表示实例化类的时候就会检查是否实现了该方法，如果没有实现，就会报错
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

    # 这样仅仅是在调用该方法的时候检查是否是实现了该方法，如果没有实现，就会报错
    def remove(self, key):
        raise NotImplementedError


class RedisCache(CacheBase):
    def __init__(self):
        self.caches = {}

    def get(self, key):
        return self.caches[key]

    def set(self, key, value):
        self.caches[key] = value

    def remove(self, key):
        del self.caches[key]


r_cache = RedisCache()
r_cache.set('name', 'mark')
print(r_cache.caches)
r_cache.remove('name')
print(r_cache.caches)
