

def test_singup_new_account(app):
    username = "user1"
    password = "test"
    app.james.insure_user_exists(username, password)
