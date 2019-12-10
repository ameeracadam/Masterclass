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
****
##  Task 6B
### Set up a Docker container for Postgres
We will use the same container in **Task 5**

### Set up a Docker container for PostgREST
For Windows:
-   Navigate to the [PostgREST Downloads page](https://github.com/PostgREST/postgrest/releases/tag/v6.0.2)
-   Select **postgrest-v6.0.2-windows-x64.zip** and **Save**
-   Navigate to the downloaded folder and extract out **postgrest.exe**
-   Test **postgrest.exe** in the Terminal by `cd` to folder and typing in the following command line:
    `./postgrest.exe`
The output should print out the PostgREST version number

For Mac:
-   In a Terminal, run the following command line:
    `tar xfJ postgrest-v6.0.2-osx.tar.xz`
The output will be a **postgrest.exe** file
-   Test out **postgrest.exe** in the Terminal by `cd` to folder and typing in the following command line:
    `./postgrest.exe`
The output should print out the PostgREST version number

### Show how the API can be queried to list the first 10 rows of a table
-   We will use Postman for our API testing. Download Postman from this [link](https://www.getpostman.com/downloads/)
-   Launch the Postman setup and install Postman on your local machine
-   To query rows from the API, launch the Docker container. In a Terminal, type in the following command line:
    `docker container start [TASK5A_CONTAINER_NAME]`
-   Create a .conf file for PostgREST. Navigate to the folder containing **postgrest.exe** and create a nee .conf file
-   Open the .conf file in a code editor and type in the following:
    ```
    db-uri = "postgres://authenticator:mysecretpassword@localhost:54320/postgres"
    db-schema = "public"
    db-anon-role = "web_anon"
    ```
-   Save the .conf file and run PostgREST. In a Terminal, `cd` to the location of the .conf file and type in the following command line:
    `./postgrest.exe [FILE_NAME].conf`
The output should be:
    ```
    Listening on port 3000
    Attempting to connect to the database...
    Connection successful
    ```
-   The container is hosted on port 3000. You can open [localhost](localhost:3000) in your browser
-   Launch Postman and Create a New Request. 
-   Since we want to query the first 10 rows of a table, select `GET` under the request and under `Enter Request URL`, type in the following:
    `localhost:3000/actor?limit=10`
In this case, we are requesting the first 10 roes of the table ACTOR


