from typing import Union

from flask import Blueprint, render_template, Response
from flask_login import login_required

from english_lab.forms import BugReportForm


__all__ = ["report"]


report = Blueprint('report', import_name=__name__, url_prefix='/report')


@report.get('/report_bug')
@login_required
def report_bug_get() -> Union[str, Response]:
    """View for reporting different bugs."""
    form = BugReportForm()
    return render_template("report/report_bug.html", form=form)
