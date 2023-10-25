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
