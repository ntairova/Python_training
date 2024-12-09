# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Nelya", "middle_test", "Tairova", "NT", "test_title", "Starpoint",
                            "home_address_for_testing 30-1-32", "1234567890", "9876543210", "123654987", "123",
                            "test1@test.com", "test2@test.com", "test3@test.com", "www.kvakva.com", "1", "February",
                            "1900", "1", "February", "2001", ""))
    app.logout()










