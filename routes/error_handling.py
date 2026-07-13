from flask import Blueprint, render_template, request
from werkzeug.exceptions import NotFound

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(404)
def handle_404(e):
    error_reason = "page_not_found"

    if e.description and not str(e.description).startswith("The requested URL"):
        error_reason = str(e.description).upper().replace(" ", "_")
    else:
        try:
            adapter = (
                request.url_rule and None
            )  # keep linter happy if url_rule is unused
            adapter = request.environ.get("werkzeug.request")
            # Fallback route-check style (same idea as your current code)
        except Exception:
            pass

    return (
        render_template(
            "error_handler/404.html",
            error_code=error_reason,
            site_url=request.url,
        ),
        404,
    )
