from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my first CI/CD Pipeline from scratch.' \
    'The pipeline is fully Automated!' \
    'Finally Everything is working fine!'

if __name__ == '__main__':
    # Listens on all network interfaces, essential for Docker
    app.run(host='0.0.0.0', port=80)