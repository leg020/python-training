# -*- coding: utf-8 -*-
from model.group import Group


def test_group(app):
    app.group.create(Group(name="ddc", header="ddc", footer="dcdc"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
