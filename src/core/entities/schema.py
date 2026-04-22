from .schema_version import SchemaVersion
from ..enums.schema_type import SchemaType

class Schema:
    def __init__(
        self,
        id: str,
        signature: str,
        schema: str,
        type: SchemaType,
        version: SchemaVersion
    ):
        self._id = id
        self._signature = signature
        self._schema = schema
        self._type = type
        self._data_to_test: str
        self._version = version

    @property
    def id(self) -> str:
        return self._id

    @property
    def signature(self) -> str:
        return self._signature

    @property
    def schema(self) -> str:
        return self._schema

    @property
    def type(self) -> SchemaType:
        return self._type

    @property
    def data_to_test(self) -> str:
        return self._data_to_test

    @property
    def version(self) -> SchemaVersion:
        return self._version