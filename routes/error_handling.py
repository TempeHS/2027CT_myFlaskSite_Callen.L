from flask import Blueprint, render_template, request

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(404)
def handle_404(e):
    desc = getattr(e, "description", "")

    if desc and not str(desc).startswith("The requested URL"):
        error_code = str(desc).upper().replace(" ", "_")
    else:
        error_code = "PAGE_NOT_FOUND"

    return (
        render_template(
            "error_handler/404.html",
            error_code=error_code,
            site_url=request.url,
        ),
        404,
    )
