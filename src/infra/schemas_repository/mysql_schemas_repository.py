import mysql.connector
from typing import Optional
from datetime import datetime

from ...core.protocols.schemas_repository import SchemasRepository
from ...core.entities.schema import Schema
from ...core.enums.schema_type import SchemaType
from ...core.entities.schema_version import SchemaVersion


class MySQLSchemasRepository(SchemasRepository):
    def __init__(self, config: dict):
        self._conn = mysql.connector.connect(**config)

    def findLatestBySignature(self, signature: str) -> Optional[Schema]:
        cursor = self._conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM schemas_data
            WHERE sch_signature = %s
            ORDER BY sch_version DESC
            LIMIT 1
        """, (signature,))

        row = cursor.fetchone()

        if not row:
            return None

        return self._map(row)

    def _map(self, row) -> Schema:
        return Schema(
            id=row["sch_id"],
            signature=row["sch_signature"],
            schema=row["sch_schema"],
            type=SchemaType(row["sch_type"]),
            version=SchemaVersion(
                row["sch_version"],
                row["sch_created_at"]  # MySQL já retorna datetime
            )
        )