class AppRoute:
    def __init__(self, routes, url):
        """Сохраняет значение переданного параметра"""
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """Сам декоратор"""
        self.routes[self.url] = cls()
