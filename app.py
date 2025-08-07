from flask import Flask

app = Flask(__name__)

def baca_pesan():
    try:
        with open('data/pesan.txt', 'r') as file:
            pesan = file.read()
            return pesan
    except FileNotFoundError:
        return "File tidak ditemukan."
    
@app.route('/')
def hello():
    pesan = baca_pesan()
    return f"Pesan: {pesan}"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')