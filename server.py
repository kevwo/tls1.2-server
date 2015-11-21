from flask import Flask
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('dummycert.pem', 'dummycert.key')

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, ssl_context=context)