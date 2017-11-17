from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from views import app
from models import db, User, Post, Role

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Role=Role)


if __name__ == '__main__':
    manager.run()