from app import create_app, db
import pymysql
print("pymysql imported")

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)