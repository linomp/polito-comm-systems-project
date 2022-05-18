## Web Service

- Professor suggested Python.

- From researching a bit the existing frameworks, FastAPI is modern, popular and seems really promising & simple to learn. 

- The best feature IMO is automatic documentation & interactive testing interface generation, that will be so useful when developing the clients.

- You can get up to speed with APIs, automatic documentation and the modern FastAPI framework for developing web services in Python with this 1h video: [Python FastAPI tutorial by TechWithTim](https://www.youtube.com/watch?v=-ykeT6kk4bk)

- I've created a skeleton fastAPI project already, you can already run it, but it's just what gets created by default with PyCharm IDE: a "hello world" endpoint.

### Instructions to run the web service (on PyCharm):
_Good news is this stuff needs to be done only once..._

1. Clone the repo
2. Open the folder 'inventory-backend' as PyCharm project
3. Create a Virtual Environment (venv) and install dependencies: 
    - File -> Settings -> Project: inventory-backend -> Python Interpreter (Click on the Cog Icon & choose "Add")
    - Choose Virtualenv Environment -> New Environment (Make sure that "Base interpreter" is your basic bare-bones Python interpreter)
    - Go to the bottom of the IDE UI to the Python Packages tab, verify the only packages installed at the moment are setuptools, pip and wheel.
    - Open `main.py` and you should get a warning about missing packages that are listed in `requirements.txt`, just click on the provided option to install them all.
4. Create a Configuration and run it:
    - Go to the top-right corner where it says "Add Configuration".
    - Choose FastAPI, give it whatever name you like. 
    - In the "Application File" option, point it to the `main.py` file. 
    - Make sure the "Python interpreter" option is set to the interpreter you just created in the previous steps.
    - Now you should be able to click on "Run <your configuration name>", next to where it previously said "Add Configuration".

    Note: these steps are 100% tested 

### Instructions to run the web service (raw Anaconda interpreter):
1. Clone the repo
2. Open anaconda prompt and navigate to the folder 'inventory-backend'
3. Type this (to automatically install any missing packages that our project requires - [source](https://stackoverflow.com/a/64538393/8522453)): 
  
    ```cat requirements.txt | while read x; do conda install -y "$x" ;done```
 4. Then to start the server, in that same directory run: 
  
    `uvicorn main:app --reload`
 
    Note: these steps are untested :(  (I got rid of anaconda and will never look back)
    