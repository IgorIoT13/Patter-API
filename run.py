from app import create_app, db
from app.dao import UserDao, DeviceDataDao, BrockerDao

app = create_app()

# with app.app_context():
#     u = User(username='test_user')
#     db.session.add(u)
#     db.session.commit()

#     p1 = Post(title='First post', author=u)
#     p2 = Post(title='Second post', author=u)

#     db.session.add_all([p1, p2])
#     db.session.commit()
#     print("Data added successfully.")

if __name__ == '__main__':
    app.run(debug=True)