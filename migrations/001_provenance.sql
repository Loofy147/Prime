-- migrations/001_provenance.sql

CREATE TABLE provenance (
    id UUID PRIMARY KEY,
    request_id UUID NOT NULL,
    source_id VARCHAR(255) NOT NULL,
    type VARCHAR(50),
    cursor VARCHAR(255),
    confidence FLOAT,
    snippet_hash VARCHAR(64)
);

CREATE INDEX idx_request_id ON provenance (request_id);
