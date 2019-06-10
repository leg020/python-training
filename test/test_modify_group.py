__author__ = 'Alex'
from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(header='test'))
    old_groups = db.get_group_list()
    text = "New group56"
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group.name = text
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modyfy_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)