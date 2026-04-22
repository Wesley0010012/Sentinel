CREATE TABLE schemas_data (
    sch_id INT PRIMARY KEY AUTO_INCREMENT,
    sch_signature VARCHAR(255),
    sch_schema TEXT NOT NULL,
    sch_type TEXT NOT NULL,
    sch_version INTEGER NOT NULL,
    sch_created_at DATETIME NOT NULL
);

CREATE INDEX idx_schema_signature ON schemas_data (sch_signature);