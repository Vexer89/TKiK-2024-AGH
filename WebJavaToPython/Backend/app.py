import sys

sys.path.insert(0, 'D:\Studia\Semestr4\TKiK\JavaToPython\src')

from flask import Flask, jsonify, request
from flask_cors import CORS
from converter import convert

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate_code():
    data = request.get_json()
    java_code = data.get('javaCode')
    python_code = translate_java_to_python(java_code)
    return jsonify(pythonCode=python_code)

def translate_java_to_python(java_code):
    # Integration of ANTLR and Python logic here
    # Placeholder logic:
    # return convert(java_code)
    return f"Translated Python code for:\n{java_code}"

if __name__ == '__main__':
    app.run(debug=True)
