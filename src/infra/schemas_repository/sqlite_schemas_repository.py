import sqlite3
from typing import Optional
from datetime import datetime

from ...core.protocols.schemas_repository import SchemasRepository
from ...core.entities.schema import Schema
from ...core.enums.schema_type import SchemaType
from ...core.entities.schema_version import SchemaVersion


class SqliteSchemasRepository(SchemasRepository):
    def __init__(self, db_path: str = "schemas.db"):
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row

    def findLatestBySignature(self, signature: str) -> Optional[Schema]:
        cursor = self._conn.cursor()

        cursor.execute("""
            SELECT *
            FROM schemas_data
            WHERE sch_signature = ?
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
                datetime.fromisoformat(row["sch_created_at"])
            )
        )