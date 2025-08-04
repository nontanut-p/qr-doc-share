from flask import Flask, render_template, request, send_from_directory, url_for
import os
import qrcode

app = Flask(__name__)
DOCUMENT_FOLDER = 'documents'
QR_FOLDER = 'static/qrcodes'

os.makedirs(QR_FOLDER, exist_ok=True)

@app.route('/')
def index():
    query = request.args.get('q', '')
    files = [f for f in os.listdir(DOCUMENT_FOLDER)
             if query.lower() in f.lower()]
    return render_template('index.html', files=files, query=query)

@app.route('/generate_qr/<filename>')
def generate_qr(filename):
    file_url = url_for('download_file', filename=filename, _external=True)
    qr_path = os.path.join(QR_FOLDER, f"{filename}.png")

    qr = qrcode.make(file_url)
    qr.save(qr_path)

    return render_template('download.html', filename=filename, qr_image=url_for('static', filename=f'qrcodes/{filename}.png'))

@app.route('/documents/<filename>')
def download_file(filename):
    return send_from_directory(DOCUMENT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    # Use 0.0.0.0 to allow LAN access
    app.run(host='0.0.0.0', port=5000, debug=True)
