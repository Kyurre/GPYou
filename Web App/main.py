from website import create_app


app = create_app()


# only run this if the name is main file\
# debug = true will rerun the server whenever changes are made
if __name__ == '__main__':
    app.run(debug=True)
