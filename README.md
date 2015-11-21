# tls1.2-server
A simple TLS 1.2 server to test clients

```
pip install flask
python server.py
```

This hosts a simple server on https://localhost:8080 with a /test endpoint which returns 'Hello World!'

```
import requests
requests.get('https://localhost:8080/test', verify=False).text
```