from flask import Flask, request, send_file, render_template
from rembg import remove
import io
import os

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    file = request.files['image']
    input_image = file.read()
    try:
        output_image = remove(input_image)
        return send_file(
            io.BytesIO(output_image),
            mimetype='image/png',
            download_name='output.png'
        )
    except Exception as e:
        print("Error:", e)
        return 'Error processing image', 500

# ✅ Required for local testing (ignored by Gunicorn in Render)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
