import json
from jsonschema import validate
from ...core.protocols.schema_tester import SchemaTester
from ...core.entities.schema import Schema

class JsonSchemaTester(SchemaTester):
    def test(self, schema: Schema) -> bool:
        try:
            schema_dict = json.loads(schema.schema)
            data_dict = json.loads(schema.data_to_test)

            validate(instance=data_dict, schema=schema_dict)
            return True
        except Exception:
            return False