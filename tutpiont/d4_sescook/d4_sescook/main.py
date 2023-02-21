from flask import Flask, render_template, make_response, request, session, abort, flash

app = Flask(__name__)
app.secret_key = 'ASDF'


@app.route('/testcookie')
def testcookie():
    context= dict()
    session['login'] = 'yes'
    resp = make_response(render_template('testcookie.html' , context=context))
    resp.set_cookie('user', 'skybhav')
    return resp

@app.route('/checkcookie')
def checkcookie():
    if 'login' not in session :
        abort(401)
    context = dict()
    context['user'] = request.cookies.get('user', 'not set yet')
    context['log_status'] = session['login']
    return render_template('testcookie.html', context=context)


@app.route('/testflashmsg')
def testflashmsg():
    flash('this is test flash message ...')

    return render_template('testflashmsg.html')


if __name__ == '__main__':
    app.debug = True
    app.run()