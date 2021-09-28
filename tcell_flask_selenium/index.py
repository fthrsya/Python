from flask import Flask,render_template,request
from datetime import datetime
from tcell_v2 import *
app = Flask(__name__,static_url_path='/static')



@app.route("/")
def anaSayfa():
    return "Merhaba Admin Blog ziyaretçileri!"

@app.route('/ajax')
def ajax():
   return render_template("ajax.html")

@app.route("/tarih", methods=['POST','GET'])
def tarih():
    if request.method == 'POST':
#         sayi = request.form.get('sayi')
#         sonuc = int(sayi)**2
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S %d/%m/%Y ")
        return (str(dt_string))
        #return str(sonuc)
    else:
        return "Bu sayfayı görmeye yetkiniz yok!"


@app.route("/tcell", methods=['POST','GET'])
def tcell():
    if request.method == 'POST':
#         sayi = request.form.get('sayi')
#         sonuc = int(sayi)**2
        #turkcell()
#tcell_2_sample()
        return (turkcell())
        #return str(sonuc)
    else:
        return "Bu sayfayı görmeye yetkiniz yok!"

if __name__ == "__main__":
    app.run(debug=True)
