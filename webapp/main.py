from web import create_app
from flask import Flask

app=create_app()



if __name__=='__main__':
    app.run(port=5001,debug=True)