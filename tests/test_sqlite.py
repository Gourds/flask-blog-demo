

import app
from app import Role,User

db = app.db

admin_role = Role(name='Admin')
user_role = Role(name='User')

user_gourds = User(username='Gourds', email='gourds@tom.com', password_hash='123456', role=admin_role.id)
user_arvon = User(username='Arvon', role=user_role.id)
user_tom = User(username='Tom', role=user_role.id)

db.session.add(admin_role)
db.session.add(user_role)
# db.session.commit()

db.session.add_all([user_arvon,user_gourds,user_tom])
db.session.commit()
db.session.close()

