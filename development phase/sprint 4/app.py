
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


 
    
#businesss--------    

@app.route('/business')
def business():
    bh="https://newsapi.org/v2/top-headlines?category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(bh).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/business.html",us=As)
@app.route('/business/india')
def india1():
    india="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/business/country/india.html",ind=india)

@app.route('/business/ArabEmirates')
def ArabEmirates1():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/business/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/business/Argentina')
def Argentina1():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/business/country/Argentina.html",ae=Ar)
@app.route('/business/Australia')
def Australia1():
    au="https://newsapi.org/v2/top-headlines?country=au&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/business/country/Australia.html",au=Au)
@app.route('/business/Austria')
def Austria1():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Austria.html",ast=As)
@app.route('/business/Brazil')
def  Brazil1():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Brazil.html",ast=As)
@app.route('/business/Belgium')
def Belgium1():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Belgium.html",ast=As)
@app.route('/business/Bulgaria')
def Bulgaria1():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Bulgaria.html",ast=As)
@app.route('/business/Canada')
def Canada1():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Canada.html",ast=As)
@app.route('/business/China')
def China1():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/China.html",ast=As)
@app.route('/business/Colombia')
def Colombia1():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Colombia.html",ast=As)
@app.route('/business/ Cuba')
def  Cuba1():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Cuba.html",ast=As)
@app.route('/business/Czhechia')
def  Czhechia1():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Czhechia.html",ast=As)
@app.route('/business/Denmark')
def  Denmark1():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Denmark.html",ast=As)
@app.route('/business/Egypt')
def  Egypt1():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Egypt.html",ast=As)
@app.route('/business/France')
def  France1():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/France.html",ast=As)
@app.route('/business/Greece')
def  Greece1():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Greece.html",ast=As)
@app.route('/business/HongKong')
def  HongKong1():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/HongKong.html",ast=As)
@app.route('/business/Hungray')
def  Hungray1():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Hungray.html",ast=As)
@app.route('/business/Italy')
def  Italy1():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Italy.html",ast=As)
@app.route('/business/Japan')
def  Japan1():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/Japan.html",ast=As)
@app.route('/business/SwitzerLand')
def  SwitzerLand1():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/SwitzerLand.html",ast=As)
@app.route('/business/UnitedKingdom')
def  UnitedKingdom1():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/UnitedKingdom.html",ast=As)
@app.route('/business/UnitedStates')
def  UnitedStates1():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/business/country/UnitedStates.html",ast=As)

#tech-------
@app.route('/technology')
def technology():
    th="https://newsapi.org/v2/top-headlines?category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(th).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/technology.html",us=As)
@app.route('/technology/india')
def india2():
    india="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/technology/country/india.html",ind=india)

@app.route('/technology/ArabEmirates')
def ArabEmirates2():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/technology/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/technology/Argentina')
def Argentina2():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Argentina.html",ae=Ar)
@app.route('/technology/Australia')
def Australia2():
    au="https://newsapi.org/v2/top-headlines?country=au&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Australia.html",au=Au)
@app.route('/technology/Austria')
def Austria2():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Austria.html",ast=As)
@app.route('/technology/Brazil')
def  Brazil2():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Brazil.html",ast=As)
@app.route('/technology/Belgium')
def Belgium2():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Belgium.html",ast=As)
@app.route('/technology/Bulgaria')
def Bulgaria2():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Bulgaria.html",ast=As)
@app.route('/technology/Canada')
def Canada2():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Canada.html",ast=As)
@app.route('/technology/China')
def China2():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/China.html",ast=As)
@app.route('/technology/Colombia')
def Colombia2():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Colombia.html",ast=As)
@app.route('/technology/ Cuba')
def  Cuba2():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Cuba.html",ast=As)
@app.route('/technology/Czhechia')
def  Czhechia2():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Czhechia.html",ast=As)
@app.route('/technology/Denmark')
def  Denmark2():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Denmark.html",ast=As)
@app.route('/technology/Egypt')
def  Egypt2():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Egypt.html",ast=As)
@app.route('/technology/France')
def  France2():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/France.html",ast=As)
@app.route('/technology/Greece')
def  Greece2():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Greece.html",ast=As)
@app.route('/technology/HongKong')
def  HongKong2():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/HongKong.html",ast=As)
@app.route('/technology/Hungray')
def  Hungray2():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Hungray.html",ast=As)
@app.route('/technology/Italy')
def  Italy2():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Italy.html",ast=As)
@app.route('/technology/Japan')
def  Japan2():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/Japan.html",ast=As)
@app.route('/technology/SwitzerLand')
def  SwitzerLand2():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/SwitzerLand.html",ast=As)
@app.route('/technology/UnitedKingdom')
def  UnitedKingdom2():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/UnitedKingdom.html",ast=As)
@app.route('/technology/UnitedStates')
def  UnitedStates2():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/technology/country/UnitedStates.html",ast=As)


#general----
@app.route('/general')
def general():
    gh="https://newsapi.org/v2/top-headlines?category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(gh).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/general.html",us=As)
@app.route('/general/india')
def india3():
    india="https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/general/country/india.html",ind=india)

@app.route('/general/ArabEmirates')
def ArabEmirates3():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/general/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/general/Argentina')
def Argentina3():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/general/country/Argentina.html",ae=Ar)
@app.route('/general/Australia')
def Australia3():
    au="https://newsapi.org/v2/top-headlines?country=au&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/general/country/Australia.html",au=Au)
@app.route('/general/Austria')
def Austria3():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Austria.html",ast=As)
@app.route('/general/Brazil')
def  Brazil3():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Brazil.html",ast=As)
@app.route('/general/Belgium')
def Belgium3():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Belgium.html",ast=As)
@app.route('/general/Bulgaria')
def Bulgaria3():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Bulgaria.html",ast=As)
@app.route('/general/Canada')
def Canada3():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Canada.html",ast=As)
@app.route('/general/China')
def China3():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/China.html",ast=As)
@app.route('/general/Colombia')
def Colombia3():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Colombia.html",ast=As)
@app.route('/general/ Cuba')
def  Cuba3():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Cuba.html",ast=As)
@app.route('/general/Czhechia')
def  Czhechia3():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Czhechia.html",ast=As)
@app.route('/general/Denmark')
def  Denmark3():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Denmark.html",ast=As)
@app.route('/general/Egypt')
def  Egypt3():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Egypt.html",ast=As)
@app.route('/general/France')
def  France3():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/France.html",ast=As)
@app.route('/general/Greece')
def  Greece3():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Greece.html",ast=As)
@app.route('/general/HongKong')
def  HongKong3():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/HongKong.html",ast=As)
@app.route('/general/Hungray')
def  Hungray3():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Hungray.html",ast=As)
@app.route('/general/Italy')
def  Italy3():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Italy.html",ast=As)
@app.route('/general/Japan')
def  Japan3():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/Japan.html",ast=As)
@app.route('/general/SwitzerLand')
def  SwitzerLand3():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/SwitzerLand.html",ast=As)
@app.route('/general/UnitedKingdom')
def  UnitedKingdom3():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/UnitedKingdom.html",ast=As)
@app.route('/general/UnitedStates')
def  UnitedStates3():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/general/country/UnitedStates.html",ast=As)
@app.route('/health')
def health():
    hh="https://newsapi.org/v2/top-headlines?category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(hh).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/health.html",us=As)
@app.route('/health/india')
def india4():
    india="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/health/country/india.html",ind=india)

@app.route('/health/ArabEmirates')
def ArabEmirates4():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/health/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/health/Argentina')
def Argentina4():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/health/country/Argentina.html",ae=Ar)
@app.route('/health/Australia')
def Australia4():
    au="https://newsapi.org/v2/top-headlines?country=au&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/health/country/Australia.html",au=Au)
@app.route('/health/Austria')
def Austria4():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Austria.html",ast=As)
@app.route('/health/Brazil')
def  Brazil4():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Brazil.html",ast=As)
@app.route('/health/Belgium')
def Belgium4():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Belgium.html",ast=As)
@app.route('/health/Bulgaria')
def Bulgaria4():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Bulgaria.html",ast=As)
@app.route('/health/Canada')
def Canada4():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Canada.html",ast=As)
@app.route('/health/China')
def China4():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/China.html",ast=As)
@app.route('/health/Colombia')
def Colombia4():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Colombia.html",ast=As)
@app.route('/health/ Cuba')
def  Cuba4():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Cuba.html",ast=As)
@app.route('/health/Czhechia')
def  Czhechia4():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Czhechia.html",ast=As)
@app.route('/health/Denmark')
def  Denmark4():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Denmark.html",ast=As)
@app.route('/health/Egypt')
def  Egypt4():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Egypt.html",ast=As)
@app.route('/health/France')
def  France4():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/France.html",ast=As)
@app.route('/health/Greece')
def  Greece4():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Greece.html",ast=As)
@app.route('/health/HongKong')
def  HongKong4():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/HongKong.html",ast=As)
@app.route('/health/Hungray')
def  Hungray4():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Hungray.html",ast=As)
@app.route('/health/Italy')
def  Italy4():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Italy.html",ast=As)
@app.route('/health/Japan')
def  Japan4():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/Japan.html",ast=As)
@app.route('/health/SwitzerLand')
def  SwitzerLand4():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/SwitzerLand.html",ast=As)
@app.route('/health/UnitedKingdom')
def  UnitedKingdom4():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/UnitedKingdom.html",ast=As)
@app.route('/health/UnitedStates')
def  UnitedStates4():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/health/country/UnitedStates.html",ast=As)

@app.route('/science')
def science():
    sh="https://newsapi.org/v2/top-headlines?category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(sh).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/science.html",us=As)
    #------
@app.route('/science/india')
def india5():
    india="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/science/country/india.html",ind=india)

@app.route('/science/ArabEmirates')
def ArabEmirates5():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/science/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/science/Argentina')
def Argentina5():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/science/country/Argentina.html",ae=Ar)
@app.route('/science/Australia')
def Australia5():
    au="https://newsapi.org/v2/top-headlines?country=au&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/science/country/Australia.html",au=Au)
@app.route('/science/Austria')
def Austria5():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Austria.html",ast=As)
@app.route('/science/Brazil')
def  Brazil5():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Brazil.html",ast=As)
@app.route('/science/Belgium')
def Belgium5():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Belgium.html",ast=As)
@app.route('/science/Bulgaria')
def Bulgaria5():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Bulgaria.html",ast=As)
@app.route('/science/Canada')
def Canada5():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Canada.html",ast=As)
@app.route('/science/China')
def China5():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/China.html",ast=As)
@app.route('/science/Colombia')
def Colombia5():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Colombia.html",ast=As)
@app.route('/science/ Cuba')
def  Cuba5():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Cuba.html",ast=As)
@app.route('/science/Czhechia')
def  Czhechia5():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Czhechia.html",ast=As)
@app.route('/science/Denmark')
def  Denmark5():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Denmark.html",ast=As)
@app.route('/science/Egypt')
def  Egypt5():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Egypt.html",ast=As)
@app.route('/science/France')
def  France5():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/France.html",ast=As)
@app.route('/science/Greece')
def  Greece5():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Greece.html",ast=As)
@app.route('/science/HongKong')
def  HongKong5():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/HongKong.html",ast=As)
@app.route('/science/Hungray')
def  Hungray5():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Hungray.html",ast=As)
@app.route('/science/Italy')
def  Italy5():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Italy.html",ast=As)
@app.route('/science/Japan')
def  Japan5():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/Japan.html",ast=As)
@app.route('/science/SwitzerLand')
def  SwitzerLand5():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/SwitzerLand.html",ast=As)
@app.route('/science/UnitedKingdom')
def  UnitedKingdom5():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/UnitedKingdom.html",ast=As)
@app.route('/science/UnitedStates')
def  UnitedStates5():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/science/country/UnitedStates.html",ast=As)
@app.route('/sports')
def sports():
    ssh="https://newsapi.org/v2/top-headlines?category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ssh).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/sports.html",us=As)
    #--------
@app.route('/sports/india')
def india6():
    india="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(india).json()
    india={
        'articles' : a['articles']
    }
    return render_template("/sports/country/india.html",ind=india)

@app.route('/sports/ArabEmirates')
def ArabEmirates6():
    ArabEmirates="https://newsapi.org/v2/top-headlines?country=ae&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ArabEmirates).json()
    ArabEmirates={
        'articles' : a['articles']
    }
    return render_template("/sports/country/ArabEmirates.html",ae=ArabEmirates)
@app.route('/sports/Argentina')
def Argentina6():
    ar="https://newsapi.org/v2/top-headlines?country=ar&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ar).json()
    Ar={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Argentina.html",ae=Ar)
@app.route('/sports/Australia')
def Australia6():
    au="https://newsapi.org/v2/top-headlines?country=au&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(au).json()
    Au={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Australia.html",au=Au)
@app.route('/sports/Austria')
def Austria6():
    ast="https://newsapi.org/v2/top-headlines?country=as&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Austria.html",ast=As)
@app.route('/sports/Brazil')
def  Brazil6():
    ast="https://newsapi.org/v2/top-headlines?country=br&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Brazil.html",ast=As)
@app.route('/sports/Belgium')
def Belgium6():
    ast="https://newsapi.org/v2/top-headlines?country=be&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Belgium.html",ast=As)
@app.route('/sports/Bulgaria')
def Bulgaria6():
    ast="https://newsapi.org/v2/top-headlines?country=bg&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Bulgaria.html",ast=As)
@app.route('/sports/Canada')
def Canada6():
    ast="https://newsapi.org/v2/top-headlines?country=ca&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Canada.html",ast=As)
@app.route('/sports/China')
def China6():
    ast="https://newsapi.org/v2/top-headlines?country=cn&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/China.html",ast=As)
@app.route('/sports/Colombia')
def Colombia6():
    ast="https://newsapi.org/v2/top-headlines?country=co&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Colombia.html",ast=As)
@app.route('/sports/ Cuba')
def  Cuba6():
    ast="https://newsapi.org/v2/top-headlines?country=cu&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Cuba.html",ast=As)
@app.route('/sports/Czhechia')
def  Czhechia6():
    ast="https://newsapi.org/v2/top-headlines?country=cz&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Czhechia.html",ast=As)
@app.route('/sports/Denmark')
def  Denmark6():
    ast="https://newsapi.org/v2/top-headlines?country=de&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Denmark.html",ast=As)
@app.route('/sports/Egypt')
def  Egypt6():
    ast="https://newsapi.org/v2/top-headlines?country=eg&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Egypt.html",ast=As)
@app.route('/sports/France')
def  France6():
    ast="https://newsapi.org/v2/top-headlines?country=fr&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/France.html",ast=As)
@app.route('/sports/Greece')
def  Greece6():
    ast="https://newsapi.org/v2/top-headlines?country=gr&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Greece.html",ast=As)
@app.route('/sports/HongKong')
def  HongKong6():
    ast="https://newsapi.org/v2/top-headlines?country=hk&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/HongKong.html",ast=As)
@app.route('/sports/Hungray')
def  Hungray6():
    ast="https://newsapi.org/v2/top-headlines?country=hu&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Hungray.html",ast=As)
@app.route('/sports/Italy')
def  Italy6():
    ast="https://newsapi.org/v2/top-headlines?country=it&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Italy.html",ast=As)
@app.route('/sports/Japan')
def  Japan6():
    ast="https://newsapi.org/v2/top-headlines?country=jp&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/Japan.html",ast=As)
@app.route('/sports/SwitzerLand')
def  SwitzerLand6():
    ast="https://newsapi.org/v2/top-headlines?country=ch&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/SwitzerLand.html",ast=As)
@app.route('/sports/UnitedKingdom')
def  UnitedKingdom6():
    ast="https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/UnitedKingdom.html",ast=As)
@app.route('/sports/UnitedStates')
def  UnitedStates6():
    ast="https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=e11724bf3102412c999b1fb3c9dd2035"
    a=requests.get(ast).json()
    As={
        'articles' : a['articles']
    }
    return render_template("/sports/country/UnitedStates.html",ast=As)


    



if __name__ == "__main__":
    app.run(port=24, debug=True)
