## Flask Application Design

### HTML Files

- **home.html**: The front page of the application, where the user can view or manipulate information.
- **about.html**: A static page containing information about the application or its creators.
- **error.html**: A page displayed when an error occurs in the application.

### Routes

- **@app.route('/')**: The root route, which displays the home page.
- **@app.route('/about')**: A route that displays the about page.
- **@app.route('/process-data', methods=['POST'])**: A route that handles data submission and performs necessary actions.
- **@app.route('/display-results')**: A route that displays the results of the data processing.
- **@app.route('/error')**: A route that handles application errors and displays the error page.