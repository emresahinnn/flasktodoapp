
from flask import Flask,render_template,redirect,url_for
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                                                                  #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emres/OneDrive/Masaüstü/TodoApp/todo.db'   # # bu 3 satır şart
db = SQLAlchemy(app)                                                                                   #



@app.route("/")
def index():
    todos = Todo.query.all()


    return render_template("index.html", todos = todos )

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()

    """if todo.comlete == True :
        todo.comlete = False
    else:
        todo.comlete = True"""

    todo.comlete = not todo.comlete

    db.session.commit()

    return redirect(url_for("index"))








@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title") # title değerini form dan alıcaz
    newTodo = Todo(title = title , comlete = False) #complete de false dan başlatıyoruz / obje oluşturduk

    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))



@app.route("/delete/<string:id>") #siliyor Todo yu
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()

    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model): # orm içindeki türettik

    id = db.Column(db.Integer, primary_key=True) # db.column satır / sütün oluşturmuş ### db.integer / sayı bir değerdir ### otoikrament olarak artsın diyoruz
    title = db.Column(db.String(80))             #title 80 uzunluğunda olacak
    comlete = db.Column(db.Boolean)              # 2 değer alabilecek ya 0 yada 1  -- 1 True 0 ise false dur


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)















