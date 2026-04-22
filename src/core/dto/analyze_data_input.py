class AnalyzeDataInput:
    def __init__(self, signature: str, data_to_test: str):
        self._signature = signature
        self._data_to_test = data_to_test

    @property
    def signature(self) -> str:
        return self._signature

    @signature.setter
    def signature(self, value: str):
        if not value:
            raise ValueError("Signature cannot be empty")
        self._signature = value

    @property
    def data_to_test(self) -> str:
        return self._data_to_test

    @data_to_test.setter
    def data_to_test(self, value: str):
        if not value:
            raise ValueError("Data to test cannot be empty")
        self._data_to_test = value