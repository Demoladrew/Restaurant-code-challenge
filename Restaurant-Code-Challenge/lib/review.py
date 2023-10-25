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
