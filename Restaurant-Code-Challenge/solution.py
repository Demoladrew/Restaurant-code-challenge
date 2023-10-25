from lib.review import *


class Customer:
    _all = []

    def __init__(self, name):
        Customer._all.append(self)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add_review(restaurant, content):
        Review(restaurant, self, content)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_all_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name]

    @classmethod
    def find_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name][0]


class Restaurant:
    _all = []

    def __init__(self, name):
        Restaurant._all.append(self)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    @property
    def customers(self):
        return [review.customer for review in self.reviews]

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_all_by_name(cls, name):
        return [restaurant for restaurant in cls.all() if restaurant.name == name]

    @classmethod
    def find_by_name(cls, name):
        return [restaurant for restaurant in cls.all() if restaurant.name == name][0]


class Review:
    _all = []

    def __init__(self, restaurant, customer, content):
        self._content = content
        Review._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def customer(self):
        return self._customer

    @property
    def content(self):
        return self._content

    @property
    def restaurant(self):
        return self._restaurant
