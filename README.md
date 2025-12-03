# 🎉 Django Project Setup Guide

## 📦 Create Package Definition Files
📄 `pip freeze > requirements.txt`

---

## 🔄 Re-Create Virtual Environment (.venv / venv)
🆕 `python -m venv venv`  
🆕 `python -m venv .venv`

---

## 📥 Re-install Packages
📦 `pip install -r requirements.txt`

---

## ▶️ How to Activate venv

### 🪟 Windows:
⚡ `.venv\Scripts\activate`

### 🐧 Linux / 🍎 macOS:
⚡ `source .venv/bin/activate`

---

## 🚀 Run Project Again
🏃‍♂️ `python manage.py runserver`

---

## 🗂 Run Initial Migration
🛠 `python manage.py migrate`

---

## 🛠 Let's Create a Django App
🧱 `python manage.py startapp myapp`

---
---
# 🌟 Django Template Filters & Tags Cheat Sheet

| Category | Filter | Example |
|----------|--------|---------|
| 📝 TEXT FILTERS | ✨ Capital First | `{{ city&#124;capfirst }}` |
|  | 🔠 Uppercase | `{{ city&#124;upper }}` |
|  | 🔡 Lowercase | `{{ city&#124;lower }}` |
|  | 🧮 Word Count | `{{ city&#124;wordcount }}` |
|  | 🏷 Title Case | `{{ city&#124;title }}` |
|  | ✂️ Remove Letter "d" | `{{ city&#124;cut:"d" }}` |
| 🔢 NUMBER FILTERS | ➕ Add 10 | `{{ age&#124;add:10 }}` |
|  | 🔍 Divisible by 2 | `{{ age&#124;divisibleby:2 }}` |
|  | 🎯 Float (2 decimals) | `{{ age&#124;floatformat:2 }}` |
| 📋 LIST FILTERS | 📏 Length | `{{ skills&#124;length }}` |
|  | 🔹 First Item | `{{ skills&#124;first }}` |
|  | 🔸 Last Item | `{{ skills&#124;last }}` |
|  | 🔗 Join List | `{{ skills&#124;join:"," }}` |
| 🗓 DATE & TIME FILTERS | 📅 Original Date | `{{ dob }}` |
|  | 📆 Format (Y-m-d) | `{{ dob&#124;date:"Y-m-d" }}` |
|  | ⏳ Time Until | `{{ dob&#124;timeuntil }}` |
|  | 🕰 Time Since | `{{ dob&#124;timesince }}` |
| 🔐 ESCAPE FILTERS | ✅ Safe HTML | `{{ button&#124;safe }}` |
|  | 🚫 Escape HTML | `{{ button&#124;escape }}` |
| ⚙️ CONDITIONAL FILTERS | 🧩 Default Value | `{{ isBangladeshi&#124;default:"No Value" }}` |
| 📚 DICTIONARY FILTERS | 🗂 Dictionary | `{{ learners }}` |
|  | 🔤 Sort by Name | `{{ learners&#124;dictsort:'name' }}` |
|  | 🔁 Sort by Name (Reversed) | `{{ learners&#124;dictsortreversed:'name' }}` |


## 🔄 IF / ELSE (Condition)

---
---

# 🧩 Django Template Features

| Feature | Description |
|---------|-------------|
| 📄 Template Inheritance | ✨ Use `{% extends 'base.html' %}` for base templates<br>🔁 Use `{% block %}` for overridable sections |
| 🏷 Block Tags | 📌 Define reusable sections with `{% block %}` and `{% endblock %}` |
| 📁 Static File Management | 🖼 Include static files (CSS, JS, etc.) with `{% load static %}` |
| 💬 Comments | 💡 Add ignored comments with `{# This is a comment #}` |
