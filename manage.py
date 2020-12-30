#!/usr/bin/env python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from carbery import create_app, db


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all(app=create_app())
    db.session.commit()


if __name__ == '__main__':
    manager.run()
