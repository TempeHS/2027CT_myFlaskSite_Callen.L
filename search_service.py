from search_config import (
    DISALLOWED_SEARCH_CHARS,
    MAX_SEARCH_QUERY_LEN,
    SEARCH_PAGES,
)


def sanitize_search_query(raw_query: str) -> str:
    query = (raw_query or "").strip()[:MAX_SEARCH_QUERY_LEN]
    query = DISALLOWED_SEARCH_CHARS.sub("", query)
    return " ".join(query.split())


def find_exact_match_endpoint(query: str) -> str | None:
    q = query.lower()
    for page in SEARCH_PAGES:
        if q == page["title"].lower() or q == page["endpoint"].lower():
            return page["endpoint"]
    return None


def find_partial_matches(query: str) -> list[dict]:
    q = query.lower()
    matches = []
    for page in SEARCH_PAGES:
        searchable_text = " ".join(
            [page["title"], page["description"], " ".join(page["keywords"])]
        ).lower()
        if q in searchable_text:
            matches.append(page)
    return matches


def resolve_endpoint_name(endpoint: str) -> str | None:
    from flask import current_app

    if endpoint in current_app.view_functions:
        return endpoint
    suffix = f".{endpoint}"
    matches = [
        name for name in current_app.view_functions.keys() if name.endswith(suffix)
    ]
    if not matches:
        return None
    return sorted(matches)[0]


# search rankings?
