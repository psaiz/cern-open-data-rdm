"""Additional views."""

from flask import Blueprint

#
# Registration
#
def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "open_data_rdm",
        __name__,
        template_folder="./templates",
        static_folder="./static",
    )

    # Add URL rules
    return blueprint
