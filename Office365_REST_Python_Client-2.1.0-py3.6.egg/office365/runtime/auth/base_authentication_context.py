from abc import ABCMeta, abstractmethod


class BaseAuthenticationContext(metaclass=ABCMeta):
    def __init__(self):
        pass

    
    @abstractmethod
    def authenticate_request(self, request_options):
        pass
