# 🎉 Django Project Setup Guide

## 📦 Create Package Definition Files
- `pip freeze > requirements.txt`

---

## 🔄 Re-Create Virtual Environment (.venv / venv)
- `python -m venv venv`
- `python -m venv .venv`

---

## 📥 Re-install Packages
- `pip install -r requirements.txt`

---

## ▶️ How to Activate venv

### 🪟 Windows:
- `.venv\Scripts\activate`

### 🐧 Linux / 🍎 macOS:
- `source .venv/bin/activate`

---

## 🚀 Run Project Again
- `python manage.py runserver`

---

## 🗂 Run Initial Migration
- `python manage.py migrate`

---

## 🛠 Let's Create a Django App
- `python manage.py startapp myapp`
