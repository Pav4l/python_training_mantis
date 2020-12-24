def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_loggen_in_as("administrator")