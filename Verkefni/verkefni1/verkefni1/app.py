#Halló heimur með innbyggðum flask server
# import Flask class in Python
from flask import Flask,render_template

# Create app, that hosts the application
app = Flask(__name__)

frettir = [
    ['0','21 lát­inn eft­ir eld­gosið á Nýja-Sjálandi','Alls er 21 lát­inn eft­ir að eld­fjall á Hvítu­eyju á Nýja-Sjálandi gaus í des­em­ber.'],
    ['1','Lög­reglumaður ákærður fyr­ir morð',' Lög­reglumaður í Mary­land-ríki hef­ur verið ákærður fyr­ir morð en hann skaut mann til bana á mánu­dags­kvöldið. Maður­inn var í járn­um inni í lög­reglu­bíl þegar Michael Owen skaut hann sjö sinn­um.'],
    ['2','Ekk­ert smit inn­an­lands í gær',' Ekk­ert kór­ónu­veiru­smit greind­ist inn­an­lands í gær. Þetta kem­ur fram á Covid.is. 19 eru á sjúkra­húsi, sem er fjölg­un um einn frá því í gær. 89 eru í ein­angr­un, sem er fækk­un um 17 á milli daga. '],
]
# route that calls a Python function. A route maps what you type in the browser (the url) to a Python function.
@app.route('/')
def index():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return render_template("default.html")


@app.route('/frettir')
def frettasida():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return render_template("frettir.html", frettir=frettir)

@app.route('/frett/<int:id>')
def frett(id):
    return render_template('frett.html', frett=frettir[id], nr=id)



@app.route('/kt-sida/<kt>')
def ktsida(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('kt-sum.html', kt = kt, summa = summa)

# This starts the web app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)   
     # debug=True. This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.
     # use_reloader. use_reloader=True þýðir að þú þarft ekki að endurkeyra python skrá stöðugt þegar þú gerir kóðabreytingar. 
     

