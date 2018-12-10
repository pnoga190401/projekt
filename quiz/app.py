#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py 
#  
# http://    - protokol
# lo1.sandomierz.pl      - nazwa serwera
#  /    - symbolizuje glowny katalog serwera



from flask import Flask
from flask import render_template

app = Flask(__name__)

#widok domyslny
@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/strona")
def strona():
    return render_template('strona.html')


if __name__ == '__main__':
    app.run(debug=True)
