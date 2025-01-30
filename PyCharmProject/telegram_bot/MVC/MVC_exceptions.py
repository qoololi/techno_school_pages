class MVC_exceptions(Exception):
    def __init__(self, message="db_exception"):
        self.message = message
        super().__init__(self.message)