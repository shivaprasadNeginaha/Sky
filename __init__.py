from app import create_app
'''
Entry point of the project
'''

app = create_app()

if __name__ == "__main__":
    app.run()