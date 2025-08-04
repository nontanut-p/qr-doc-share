# 📄 QR Document Sharer (LAN only)

A simple Python Flask web application that lets you:

- Search for documents (PDFs, DOCXs, etc.) stored locally
- Generate a QR code that links to the document
- Scan the QR with an iPad or any mobile device
- Download the document through the local network

⚡ All files stay **inside your local network** — no cloud or internet required!

---

## 🌐 Use Case

Perfect for:

- Local office file sharing
- Internal QC or technical documentation download
- Classroom or workshop materials
- Factory environments with tablets

---

## 🛠 Features

- 🔎 File search
- 📥 One-click QR code generation
- 📲 iPad/mobile-friendly QR download
- 🛜 Works on LAN only (no internet needed)

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/qr-doc-share.git
cd qr-doc-share

```bash
pip install -r requirements.txt

### 2. Add your documents

Put all files you want to share in the documents/ folder.

### Run the app
```bash
python app.py

### Access the app
On your computer: http://localhost:5000
On your iPad: http://<your-computer-local-IP>:5000 (e.g. http://192.168.1.10:5000)
