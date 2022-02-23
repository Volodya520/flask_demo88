from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>hello vova,this is my first flask site!</h1>"


# 博客
@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number %d' % post_id
# 游客
@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'Hello{guest} as Guest'

if __name__ == '__main__':
    app.run(debug=True)

