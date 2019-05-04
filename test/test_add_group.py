# -*- coding: utf-8 -*-
from model.group import Group


def test_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ddc", header="ddc", footer="dcdc"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
