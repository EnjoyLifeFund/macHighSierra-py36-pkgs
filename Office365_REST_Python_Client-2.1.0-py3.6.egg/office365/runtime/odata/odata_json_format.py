from abc import ABCMeta, abstractmethod


class ODataJsonFormat(object, metaclass=ABCMeta):
    """OData JSON format"""

    def __init__(self, metadata=None):
        self.metadata = metadata
        self.payload_root_entry = None
        self.payload_root_entry_collection = None

    
    @abstractmethod
    def build_http_headers(self):
        pass
