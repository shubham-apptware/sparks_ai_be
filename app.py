from flask import Flask, request, jsonify
from seo_generator import SEOGenerator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
gen = SEOGenerator()

@app.route('/getResponse', methods=['POST'])
def add():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400
    
    result = gen.generate_description(data)
    return jsonify(result), 200

    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)