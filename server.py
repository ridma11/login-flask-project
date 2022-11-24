from flask import Flask, render_template
import test
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')



@app.route('/my-link1/',methods=['GET'])
def my_link3():
  return my_link(),my_link2()
def my_link():
  return 'Genarated original sample rate 44.1 kHz .'
def my_link2():
  return test.sound2()


@app.route('/my-link2/',methods=['GET'])
def my_link31():
  return my_link1(),my_link21()
def my_link1():
  return 'Genarated wav[0] is L channel, wav[1] is R.'
def my_link21():
  return test.sound3()


@app.route('/my-link3/',methods=['GET'])
def my_link32():
  return my_link2(),my_link22()
def my_link2():
  return 'Genarated sound amplitude halved; wav[1] amplitude remains the same'
def my_link22():
  return test.sound4()
  
@app.route('/my-link4/',methods=['GET'])
def my_link33():
  return my_link3(),my_link23()
def my_link3():
  return 'Genarated sound amplitude halved; wav[1] amplitude remains the same'
def my_link23():
  return test.sound5()

@app.route('/my-link5/',methods=['GET'])
def my_link34():
  return my_link4(),my_link24()
def my_link4():
  return 'Genarated since 5e3 is float'
def my_link24():
  return test.sound6()

@app.route('/my-link6/',methods=['GET'])
def my_link35():
  return my_link5(),my_link25()
def my_link5():
  return 'Genarated 5 seconds onwards, R channel only'
def my_link25():
  return test.sound7()

@app.route('/my-link7/',methods=['GET'])
def my_link36():
  return my_link5(),my_link26()
def my_link6():
  return 'Mix a 440Hz (middle A) sine wave to the L channel'
def my_link26():
  return test.sound10()
  
if __name__ == '__main__':
  app.run(debug=True)