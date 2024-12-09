# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("test_group", "test_header", "test_footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.session.logout()





