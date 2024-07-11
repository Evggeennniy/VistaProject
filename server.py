from app.app import create_app


if __name__ == '__main__':
    # with app.app_context():
    #     database.create_all()
    app = create_app()
    app.run(debug=True)
