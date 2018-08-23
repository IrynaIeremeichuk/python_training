from pages.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group 1", header="Header 1", footer="Footer 1"))
    app.session.logout()
