from typing import List, Optional
from datetime import datetime

from ...core.protocols.schemas_repository import SchemasRepository
from ...core.entities.schema import Schema
from ...core.enums.schema_type import SchemaType
from ...core.entities.schema_version import SchemaVersion


class InMemorySchemasRepository(SchemasRepository):
    def __init__(self, schemas: List[Schema] | None = None):
        self._schemas = schemas or []
        self._seed()

    def _seed(self) -> None:
        xml_signature = "xml-signature"
        json_signature = "json-signature"

        xsd_v1 = """<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
            <xs:element name="note" type="xs:string"/>
        </xs:schema>"""

        xsd_v2 = """<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
            <xs:element name="note">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="title" type="xs:string"/>
                        <xs:element name="body" type="xs:string"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:schema>"""

        self.add(Schema(
            id="xml-1",
            signature=xml_signature,
            schema=xsd_v1,
            type=SchemaType.XML,
            version=SchemaVersion(1, datetime.now())
        ))

        self.add(Schema(
            id="xml-2",
            signature=xml_signature,
            schema=xsd_v2,
            type=SchemaType.XML,
            version=SchemaVersion(2, datetime.now())
        ))

        json_v1 = """
        {
            "type": "object",
            "properties": {
                "name": { "type": "string" }
            },
            "required": ["name"]
        }
        """

        json_v2 = """
        {
            "type": "object",
            "properties": {
                "name": { "type": "string" },
                "age": { "type": "number" }
            },
            "required": ["name", "age"]
        }
        """

        self.add(Schema(
            id="json-1",
            signature=json_signature,
            schema=json_v1,
            type=SchemaType.JSON,
            version=SchemaVersion(1, datetime.now())
        ))

        self.add(Schema(
            id="json-2",
            signature=json_signature,
            schema=json_v2,
            type=SchemaType.JSON,
            version=SchemaVersion(2, datetime.now())
        ))

    def add(self, schema: Schema) -> None:
        self._schemas.append(schema)

    def findLatestBySignature(self, signature: str) -> Optional[Schema]:
        filtered = [s for s in self._schemas if s.signature == signature]

        if not filtered:
            return None

        return max(filtered, key=lambda s: s.version.signature)