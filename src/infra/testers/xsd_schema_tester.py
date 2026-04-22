import xmlschema
from ...core.protocols.schema_tester import SchemaTester
from ...core.entities.schema import Schema

class XsdSchemaTester(SchemaTester):
    def test(self, schema: Schema) -> bool:
        try:
            xsd = xmlschema.XMLSchema(schema.schema)
            xsd.validate(schema.data_to_test)
            return True
        except Exception:
            return False