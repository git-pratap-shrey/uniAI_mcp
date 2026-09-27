CREATE TABLE subjects (
    id        INTEGER PRIMARY KEY,
    year      INTEGER NOT NULL,
    name      TEXT NOT NULL,
    code      TEXT NOT NULL,
    UNIQUE(code),
    UNIQUE(year, name)
);

CREATE TABLE sources (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL UNIQUE       -- "Source A", "Handwritten", "Source XYZ"
);

CREATE TABLE resources (
    id            INTEGER PRIMARY KEY,
    subject_id    INTEGER NOT NULL REFERENCES subjects(id),
    resource_type TEXT NOT NULL CHECK (resource_type IN ('syllabus','notes','pyq')),
    source_id     INTEGER NOT NULL REFERENCES sources(id),
    label         TEXT NOT NULL DEFAULT '',   -- 'Unit 1', 'Unit 2', '' if not split
    file_path     TEXT NOT NULL,
    UNIQUE(subject_id, resource_type, source_id, label)
);

CREATE INDEX idx_subjects_lookup ON subjects(year);