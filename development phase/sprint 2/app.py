
from flask import Flask, render_template,request,flash,redirect,url_for,session
from newsapi import NewsApiClient
import requests
import sqlite3
app = Flask(__name__)
app.secret_key="123"



@app.route('/')
def home():
    head="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a = requests.get(head).json()
    h={
        'articles' : a['articles']
     }
    return render_template("index.html",head=h)




@app.route('/articles')
def art():
    h1="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a = requests.get(h1).json()
    h={
        'articles' : a['articles']
     }
    return render_template("articles.html",h2=h)



@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        
        try:
            name=request.form['name']
            mail=request.form['mail']
            password=request.form['password']
            con=sqlite3.connect("user.db")
            cur=con.cursor()
            cur.execute("insert into user(name,mail,password)values(?,?,?)",(name,mail,password))
            
            con.commit()
            
             
            
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:

                
             return redirect(url_for("login"))
             con.close()

    return render_template('login.html')

  


            

@app.route('/login')
def login():
    return render_template("log.html")
@app.route('/logs',methods=["GET","POST"])
def log():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']
        con=sqlite3.connect("user.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from user where name=? and password=?",(name,password))
        data=cur.fetchone()

        if data:
            session["name"]=data["name"]
            flash("sucessfully!!","primary")
            return redirect(url_for("art"))
        else:
            flash("Username and Password Mismatch","danger")
    return redirect(url_for("login"))

@app.route('/headlines')
def headlines():
     india="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e11724bf3102412c999b1fb3c9dd2035"
     a = requests.get(india).json()
     india={
        'articles' : a['articles']
     }
     return render_template('/headlines/headlines.html',us=india)
#healines integrates---
@app.route('/headlines/india')
def india():
    india="https://newsapi.org/v2/top-headlines?country=in&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/india.html",ind=india)

@app.route('/headlines/ArabEmirates')
def ArabEmirates():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/headlines/Argentina')
def Argentina():
    ar="https://newsapi.org/v2/top-headlines?country=ar&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Argentina.html",ae=Ar)
@app.route('/headlines/Australia')
def Australia():
    au="https://newsapi.org/v2/top-headlines?country=au&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Australia.html",au=Au)
@app.route('/headlines/Austria')
def Austria():
    ast="https://newsapi.org/v2/top-headlines?country=as&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Austria.html",ast=As)
@app.route('/headlines/Brazil')
def  Brazil():
    ast="https://newsapi.org/v2/top-headlines?country=br&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Brazil.html",ast=As)
@app.route('/headlines/Belgium')
def Belgium():
    ast="https://newsapi.org/v2/top-headlines?country=be&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Belgium.html",ast=As)
@app.route('/headlines/Bulgaria')
def Bulgaria():
    ast="https://newsapi.org/v2/top-headlines?country=bg&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Bulgaria.html",ast=As)
@app.route('/headlines/Canada')
def Canada():
    ast="https://newsapi.org/v2/top-headlines?country=ca&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Canada.html",ast=As)
@app.route('/headlines/China')
def China():
    ast="https://newsapi.org/v2/top-headlines?country=cn&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/China.html",ast=As)
@app.route('/headlines/Colombia')
def Colombia():
    ast="https://newsapi.org/v2/top-headlines?country=co&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Colombia.html",ast=As)
@app.route('/headlines/ Cuba')
def  Cuba():
    ast="https://newsapi.org/v2/top-headlines?country=cu&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Cuba.html",ast=As)
@app.route('/headlines/Czhechia')
def  Czhechia():
    ast="https://newsapi.org/v2/top-headlines?country=cz&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Czhechia.html",ast=As)
@app.route('/headlines/Denmark')
def  Denmark():
    ast="https://newsapi.org/v2/top-headlines?country=de&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Denmark.html",ast=As)
@app.route('/headlines/Egypt')
def  Egypt():
    ast="https://newsapi.org/v2/top-headlines?country=eg&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Egypt.html",ast=As)
@app.route('/headlines/France')
def  France():
    ast="https://newsapi.org/v2/top-headlines?country=fr&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/France.html",ast=As)
@app.route('/headlines/Greece')
def  Greece():
    ast="https://newsapi.org/v2/top-headlines?country=gr&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Greece.html",ast=As)
@app.route('/headlines/HongKong')
def  HongKong():
    ast="https://newsapi.org/v2/top-headlines?country=hk&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/HongKong.html",ast=As)
@app.route('/headlines/Hungray')
def  Hungray():
    ast="https://newsapi.org/v2/top-headlines?country=hu&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Hungray.html",ast=As)
@app.route('/headlines/Italy')
def  Italy():
    ast="https://newsapi.org/v2/top-headlines?country=it&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Italy.html",ast=As)
@app.route('/headlines/Japan')
def  Japan():
    ast="https://newsapi.org/v2/top-headlines?country=jp&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/Japan.html",ast=As)
@app.route('/headlines/SwitzerLand')
def  SwitzerLand():
    ast="https://newsapi.org/v2/top-headlines?country=ch&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/SwitzerLand.html",ast=As)
@app.route('/headlines/UnitedKingdom')
def  UnitedKingdom():
    ast="https://newsapi.org/v2/top-headlines?country=gb&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/UnitedKingdom.html",ast=As)
@app.route('/headlines/UnitedStates')
def  UnitedStates():
    ast="https://newsapi.org/v2/top-headlines?country=us&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/headlines/country/UnitedStates.html",ast=As)


 
 



if __name__ == "__main__":
    app.run(port=24, debug=True)
