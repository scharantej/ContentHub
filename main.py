
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/process-data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        # Extract data from the form
        data = request.form.to_dict()

        # Perform necessary actions with the data
        processed_data = process(data)

        # Redirect to the display results page
        return redirect(url_for('display_results', processed_data=processed_data))

@app.route('/display-results')
def display_results():
    processed_data = request.args.get('processed_data')
    return render_template('display_results.html', processed_data=processed_data)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
