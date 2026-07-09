DROP TABLE IF EXISTS search_index;

CREATE TABLE search_index (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    endpoint TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    keywords TEXT NOT NULL DEFAULT '',
    content TEXT NOT NULL DEFAULT '',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_search_index_endpoint ON search_index (endpoint);
CREATE INDEX idx_search_index_title ON search_index (title);