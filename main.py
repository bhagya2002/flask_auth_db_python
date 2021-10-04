from website import create_app

# run the function create_app() to make the web app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # run the web app and update on every save
