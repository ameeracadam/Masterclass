#   Task 6
****
##  Task 6A
### Write a function that reverses the sequence for characters in input data
-   Create a Python file and open in a code editor
-   Enter the following into the Python file
    ```
    # Argument parser
    import argparse
    
    parser = argparse.ArgumentParser()
    # Include argyment to accept string of characters
    parser.add_argument("--text", type = str)
    args = parser.parse_args()
    
    text = args.text
    processed_text = ""
    #reverse string of characters
    for i in text:
        processed_text = i + processed_text
    
    #prints reversed string
    print(processed_text)
    ```
-   Save the Python file and test in Terminal
    `python [FILE_NAME].py --text "Hello World!"`
-   The output will be **!dlroW olleH**

### Package the function into a Flask app that accepts user-imput characters
####    Create a HTML template for the app
-   In the same directory, create a new folder named **templates** and `cd` into the folder
-   Create a new HTML file and open in a code editor
-   Enter in the following:
    ```
    <form method="POST">
        <input name="text">
        <input type="submit">
    </form>
    ```
-   Save and exit out of the folder
####    Edit Python script
-   Open the Python script previously created and edit as follows:
    ```
    # Import Flask Python web framework
    from flask import Flask, request, render_template
    app = Flask(__name__)
    
    @app.route('/')
    def my_form():
        return render_template('form.html')
    
    @app.route('/', methods=['POST'])
    def my_form_post():
    # Takes in input from user
            text = request.form['text']
            processed_text = ""
            # Reverses input
            for i in text:
                processed_text = i + processed_text
                # Returns reversed sequence
            return processed_text
    
    if __name__ == '__main__':
        app.run()
    ```
-   Save and exit the editor.

### Test the Flask App. Open the browser to load the app. Key in a sequence of characters and Submit. The app should return the sequence of characters in reverse.
-   In a Terminal, enter in the following command line:
    `python [APP_FILE_NAME].py`
-   The Terminal should return a series of messages:
```
        * Serving Flask app "app" (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: off
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

-   Open browser and enter [localhost:5000](localhost:5000)
-   Enter a string of characters in the query box (e.g Hello World!) and click on **Submir Query** or press ENTER
-   You will be directed to a page that returns the string in reverse (e.g. !dlroW olleH)
-   To send another query, click on the BACK botton of the Browser and enter in a new string
-   To exit out of the Flask App, return to the Terminal the App id running in and CTRL+C