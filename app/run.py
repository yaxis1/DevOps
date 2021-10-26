from flask import Flask, render_template, request

app = Flask(__name__)
 
@app.route('/')
def main():
    
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    # Get the data from the form
    if request.method != 'POST':
        return render_template('app.html')
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    multiple_num = int(request.form['multiple_num'])
    com_num = int(request.form['com_num'])

    seven_list = [num for num in range (num1 , num2 ) if num % multiple_num == 0] 
    if len(seven_list) <= com_num:
        
        return render_template('app.html', outputDiv = str(seven_list)) 

    text = str(request.form['text'])
    return render_template('app.html', outputDiv = text)
        

if __name__ == '__main__':
    
    from waitress import serve
    
    serve(app, host="0.0.0.0", port=2021)
    


