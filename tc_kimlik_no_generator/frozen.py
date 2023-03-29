import flask_frozen

from tc_kimlik_generator import my_form

if __name__ == '__main__':
    app = my_form()
    freezer = flask_frozen.Freezer(app)

    freezer.freeze()