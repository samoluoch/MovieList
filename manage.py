from app import create_app,db
from flask_script import Manager, Shell, Server
from app.models import User,Role,Review
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')
app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """
    Run the unit tests.
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=3).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)


if __name__ == '__main__':
    manager.run()
