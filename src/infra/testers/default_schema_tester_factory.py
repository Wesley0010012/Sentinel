from ...core.protocols.schema_tester_factory import SchemaTesterFactory
from ...core.protocols.schema_tester import SchemaTester
from ...core.entities.schema import Schema
from ...core.enums.schema_type import SchemaType

from .xsd_schema_tester import XsdSchemaTester
from .json_schema_tester import JsonSchemaTester


class DefaultSchemaTesterFactory(SchemaTesterFactory):
    def build(self, schema: Schema) -> SchemaTester:
        if schema.type == SchemaType.XML:
            return XsdSchemaTester()

        if schema.type == SchemaType.JSON:
            return JsonSchemaTester()

        raise ValueError(f"Unsupported schema type: {schema.type}")