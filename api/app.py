from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "Background Remover API is live"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file uploaded', 400
    file = request.files['image']
    input_image = file.read()
    try:
        output_image = remove(input_image)
        return send_file(io.BytesIO(output_image), mimetype='image/png')
    except Exception as e:
        print("Error:", e)
        return 'Error processing image', 500

# Required for Vercel Python integration
def handler(request):
    return app(request)
