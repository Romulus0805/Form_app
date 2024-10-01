from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')
    
@app.route("/response")
def render_page1():
    sel1 = request.args['sellist1']
    sel2 = request.args['sellist2']
    if sel1 == 'in theaters' and sel2 == 'Horror':
        reply = "Speak no evil"
    elif sel1 == 'in theaters' and sel2 == 'Action':
        reply = "Transformers one"
    elif sel1 == 'in theaters' and sel2 == 'Science fiction':
        reply = "Afraid"
    elif sel1 == 'in theaters' and sel2 == 'Romance':
        reply = "Fly me to the moon"
    elif sel1 == 'in theaters' and sel2 == 'Comedy':
        reply = "Wolfs"
    elif sel1 == 'in theaters' and sel2 == 'Drama':
        reply = "Whiplash"
    elif sel1 == 'on streaming' and sel2 == 'Horror':
        reply = "Halloween"
    elif sel1 == 'on streaming' and sel2 == 'Action':
        reply = "John Wick"
    elif sel1 == 'on streaming' and sel2 == 'Science fiction':
        reply = "Dune"
    elif sel1 == 'on streaming' and sel2 == 'Romance':
        reply = "A silent voice"
    elif sel1 == 'on streaming' and sel2 == 'Comedy':
        reply = "the hangover"
    elif sel1 == 'on streaming' and sel2 == 'Drama':
        reply = "joker"
    else: 
        reply = "plese answer the questions"
    return render_template('answer.html', response = reply)


if __name__=="__main__":
    app.run(debug=False)