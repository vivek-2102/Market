from market import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)






# @app.route('/')
# def hello_world():
#     return '<h1>Hello, World</h1>'

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}</h1>'

# @app.route('/')
# @app.route('/home')
# def home_page():
#     return render_template('home.html')

# @app.route('/market')
# def market_page():
#     return render_template('market.html',item_name='Phone')

# @app.route('/market')
# def market_page():
#     items=Item.query.all()
#     return render_template('market.html',items=items)
