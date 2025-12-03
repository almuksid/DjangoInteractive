# 🎉 Django Project Setup Guide

## 📦 Create Package Definition Files
- 📄 `pip freeze > requirements.txt`

---

## 🔄 Re-Create Virtual Environment (.venv / venv)
- 🆕 `python -m venv venv`
- 🆕 `python -m venv .venv`

---

## 📥 Re-install Packages
- 📦 `pip install -r requirements.txt`

---

## ▶️ How to Activate venv

### 🪟 Windows:
- ⚡ `.venv\Scripts\activate`

### 🐧 Linux / 🍎 macOS:
- ⚡ `source .venv/bin/activate`

---

## 🚀 Run Project Again
- 🏃‍♂️ `python manage.py runserver`

---

## 🗂 Run Initial Migration
- 🛠 `python manage.py migrate`

---

## 🛠 Let's Create a Django App
- 🧱 `python manage.py startapp myapp`



---
---

# 🌟 Django Template Filters & Tags Cheat Sheet

## 📝 TEXT FILTERS
- ✨ Capital First: `{{ city|capfirst }}`
- 🔠 Uppercase: `{{ city|upper }}`
- 🔡 Lowercase: `{{ city|lower }}`
- 🧮 Word Count: `{{ city|wordcount }}`
- 🏷 Title Case: `{{ city|title }}`
- ✂️ Remove Letter "d": `{{ city|cut:"d" }}`

---

## 🔢 NUMBER FILTERS
- ➕ Add 10: `{{ age|add:10 }}`
- 🔍 Divisible by 2: `{{ age|divisibleby:2 }}`
- 🎯 Float (2 decimals): `{{ age|floatformat:2 }}`

---

## 📋 LIST FILTERS
- 📏 Length: `{{ skills|length }}`
- 🔹 First Item: `{{ skills|first }}`
- 🔸 Last Item: `{{ skills|last }}`
- 🔗 Join List: `{{ skills|join:"," }}`

---

## 🗓 DATE & TIME FILTERS
- 📅 Original Date: `{{ dob }}`
- 📆 Format (Y-m-d): `{{ dob|date:"Y-m-d" }}`
- ⏳ Time Until: `{{ dob|timeuntil }}`
- 🕰 Time Since: `{{ dob|timesince }}`

---

## 🔐 ESCAPE FILTERS
- ✅ Safe HTML: `{{ button|safe }}`
- 🚫 Escape HTML: `{{ button|escape }}`

---

## ⚙️ CONDITIONAL FILTERS
- 🧩 Default Value: `{{ isBangladeshi|default:"No Value" }}`

---

## 📚 DICTIONARY FILTERS
- 🗂 Dictionary: `{{ learners }}`
- 🔤 Sort by Name: `{{ learners|dictsort:'name' }}`
- 🔁 Sort by Name (Reversed): `{{ learners|dictsortreversed:'name' }}`

---

## 🔄 IF / ELSE (Condition)

