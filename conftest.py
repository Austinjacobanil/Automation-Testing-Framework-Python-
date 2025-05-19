import pytest
from datetime import datetime
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    # request.cls.driver = webdriver.chrome(ChromeDriverManager.install(), options=chrome_options)
    request.cls.driver = webdriver.Chrome(service=service, options=chrome_options)

#HTML Reports
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("atReports",today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = today.strftime("%Y%m%d%H%M")
    pytest_html = report_dir / f"Report_{timestamp}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Automation Test Report"
