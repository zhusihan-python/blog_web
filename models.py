from main import db


roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    roles = db.relationship(
        'Role',
        secondary=roles,
        backref=db.backref('users', lazy='dynamic')
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    rolename = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, rolename):
        self.rolename = rolename

    def __repr__(self):
        return "<Role '{}'>".format(self.rolename)


# class Privilege(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     privname = db.Column(db.String(255))
#     descript = db.Column(db.String(255))
#
#     def __init__(self, privname):
#         self.rolename = privname
#
#     def __repr__(self):
#         return "<Privilege '{}'>".format(self.privname)
#
#
# class RolePriv(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     role_id = db.Column(db.Integer())
#     priv_id = db.Column(db.Integer())