-- XML v1
INSERT INTO schemas_data (
    sch_signature,
    sch_schema,
    sch_type,
    sch_version,
    sch_created_at
) VALUES (
    'xml-signature',
    '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="note" type="xs:string"/>
     </xs:schema>',
    'xml',
    1,
    CURRENT_TIMESTAMP
);

-- XML v2
INSERT INTO schemas_data (
    sch_signature,
    sch_schema,
    sch_type,
    sch_version,
    sch_created_at
)VALUES (
    'xml-signature',
    '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="note">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="title" type="xs:string"/>
                    <xs:element name="body" type="xs:string"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
     </xs:schema>',
    'xml',
    2,
    CURRENT_TIMESTAMP
);

-- JSON v1
INSERT INTO schemas_data (
    sch_signature,
    sch_schema,
    sch_type,
    sch_version,
    sch_created_at
)VALUES (
    'json-signature',
    '{
        "type": "object",
        "properties": {
            "name": { "type": "string" }
        },
        "required": ["name"]
    }',
    'json',
    1,
    CURRENT_TIMESTAMP
);

-- JSON v2
INSERT INTO schemas_data (
    sch_signature,
    sch_schema,
    sch_type,
    sch_version,
    sch_created_at
)VALUES (
    'json-signature',
    '{
        "type": "object",
        "properties": {
            "name": { "type": "string" },
            "age": { "type": "number" }
        },
        "required": ["name", "age"]
    }',
    'json',
    2,
    CURRENT_TIMESTAMP
);