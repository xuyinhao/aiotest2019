
import pytest
from py._xmlgen import html
from datetime import datetime
testuser = "徐银浩"
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("测试人: %s"%(testuser))])
#
# @pytest.mark.optionalhook
# def pytest_html_result_header(cells):
#     cells.insert(2,html.th('描述'))
#     cells.insert(3,html.th('Time',class_='storable time',col='time'))
#     cells.pop()
#
# @pytest.mark.optionalhook
# def pytest_html_result_table_row(report,cells):
#     cells.insert(2,html.td(report.description))
#     cells.insert(3, html.td(datetime.utcnow(),class_="col-time"))
#     cells.pop()
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function__doc__)
#     report.nodeid = report.nodeid.encode("utf=8").decode("unicode_escape")
