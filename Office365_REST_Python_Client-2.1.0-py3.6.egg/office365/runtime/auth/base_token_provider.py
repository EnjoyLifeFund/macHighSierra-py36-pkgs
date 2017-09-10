from abc import abstractmethod, ABCMeta


class BaseTokenProvider(object, metaclass=ABCMeta):
    """ Base Token provide"""

    @abstractmethod
    def acquire_token(self):
        pass
