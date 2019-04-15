from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/bio')
def bio():
    return render_template('bio.html.j2')

@app.route('/usernameFun')
def usernameFun():
    name = request.args.get('funName')

    if name:
        if name[-1] == 'y':
            newName = ( name[:-1] + 'iful' )
        else:
            newName = ( name + 'y' )
        return render_template('newName.html.j2', newName=newName)
    return render_template('usernameFun.html.j2')

@app.route('/user/<name>')
def userName(name):
    return render_template('user.html.j2', name=name)

@app.route('/signup')
def signUpForm():
    return render_template('signUp.html.j2')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')

    if first and last:
        return render_template('thankYou.html.j2', first=first, last=last)
    else:
        return render_template('signUp.html.j2')

def checkUserName(userName):
    import string
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    hasLower = False
    hasUpper = False
    endsInNumber = False

    for char in userName[:-1]:
        if char in lower:
            lower = True
        elif char in upper:
            upper = True
    if userName[-1] is int:
        endsInNumber = True

    return ( hasUpper and hasLower and endsInNumber )

@app.route('/report')
def report():
    hasLower = any(c.islower() for c in username)
    hasUpper = any(c.isupper() for c in username)
    endsInNumber = userName[-1].isdigit()

    report = ( hasLower and hasUpper and endsInNumber )

    return render_template('report.html.j2',
                            report = report,
                            hasLower=hasLower,
                            hasUpper=hasUpper,
                            endsInNumber=endsInNumber)

## Custom 404 page_not_found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html.j2')

if __name__ == '__main__':
    app.run(debug = True)
