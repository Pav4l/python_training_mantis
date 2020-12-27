def test_add_project(app, db, json_project):
    app.session.login("administrator", "root")
    app.project.create_new_project(json_project)
    new_project = db.get_project_list()
    assert len(app.soap.get_list_projects("administrator", "root")) == len(new_project)