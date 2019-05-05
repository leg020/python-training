__author__ = 'Alex'
from model.group import Group

def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(name="111", header="222", footer="333"))
    app.session.logout()