from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        multiple_num = int(request.form['multiple_num'])
        text = str(request.form['text'])
        com_num = int(request.form['com_num'])

        seven_list = []
        for num in range (num1 , num2 ):
            if num % multiple_num == 0:
                seven_list.append(num)
        if len(seven_list) > com_num:
            
        
            return render_template('app.html', outputDiv = text)
        else:
     
            return render_template('app.html', outputDiv = str(seven_list))
    
    else:
        return render_template('app.html')  
        

if __name__ == '__main__':
    app.run(debug=True,port=2021)


