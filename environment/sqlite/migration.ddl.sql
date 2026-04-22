CREATE TABLE schema (
    sch_id TEXT PRIMARY KEY,
    sch_signature TEXT NOT NULL,
    sch_schema TEXT NOT NULL,
    sch_type TEXT NOT NULL,
    sch_version INTEGER NOT NULL,
    sch_created_at DATETIME NOT NULL
);

CREATE INDEX idx_schema_signature ON schema (sch_signature);