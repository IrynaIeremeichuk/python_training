from fixtures.application import Application
from pytest import fixture


@fixture(scope="session")
def app(request):
    fixture_app = Application()
    request.addfinalizer(fixture_app.quit_browser())
    return fixture_app
