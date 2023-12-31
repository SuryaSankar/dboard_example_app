from flask import Blueprint, render_template, url_for, request, current_app
from toolspy import set_query_params, subdict, transform_dict
import json
from dboard import render_table_layout as _render_table_layout

pages_bp = Blueprint('pages_bp', __name__)

def render_table_layout(
        api_endpoint,
        table_heading,
        table_filters,
        table_filters_form_id="filters",
        template_path="dboard/default_theme/table_layout.html",
        **kwargs):

    return _render_table_layout(
        api_url=set_query_params(
            url_for(api_endpoint),
            transform_dict(
                request.args,
                keys_to_retain=['target_db', table_filters_form_id],
                keys_to_rename={table_filters_form_id: "filter_params"}
            )
        ),
        table_heading=table_heading, table_filters=table_filters,
        table_filters_form_id=table_filters_form_id,
        template_path=template_path, **kwargs
    )


@pages_bp.route("/")
def index():
    return render_template("index.html", heading="Table of Contents")

@pages_bp.route("/rentals")
def rentals():
    return render_table_layout(
        api_endpoint='api_bp.rentals',
        table_heading="Rentals List",
        table_filters=[
            {"name": "start_date", "type": "date"},
            {"name": "end_date", "type": "date"},
        ]
    )

@pages_bp.route("/payments")
def payments():
    return render_table_layout(
        api_endpoint='api_bp.payments',
        table_heading="Payments List",
        table_filters=[
            {"name": "start_date", "type": "date"},
            {"name": "end_date", "type": "date"},
        ]
    )

@pages_bp.route("/dummy")
def dummy():
    return render_table_layout(
        template_path="pages/dummy.html",
        api_endpoint='api_bp.dummy',
        table_heading="Monthly Jobs",
        table_filters=[
            {"name": "start_date", "type": "date"},
            {"name": "end_date", "type": "date"}
        ]
    )
