from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hi')
def hai():
    return render_template('hai.html')

@FAI.route('/balayya')
def image_insert():
    return render_template('image_insert.html')


if __name__=='__main__':
    FAI.run(debug=True)