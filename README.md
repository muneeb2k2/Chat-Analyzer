# 💬 Chat Analyzer

A modern **WhatsApp Chat Analysis tool** built with **Python + Streamlit** to uncover insights from conversations.

Supports both:

* 👤 **1-to-1 chats**
* 👥 **Group chats**

---

## 🚀 Features

* 📊 **Message Statistics**

  * Total messages
  * Total words
  * Media shared
  * Links shared

* 🏆 **Most Active Users (Group Chats)**

  * Message count per user
  * Percentage contribution

* ☁️ **Word Cloud**

  * Visual representation of most used words

* 🎨 **Modern UI**

  * Dark-themed dashboard
  * Clean and responsive layout

---

## 🧠 How it works

1. Export WhatsApp chat (without media)
2. Upload `.txt` file into the app
3. The system:

   * Parses chat using regex
   * Converts timestamps to structured data
   * Extracts features (time, users, messages)
   * Generates insights and visualizations

---

## 📁 Project Structure

```
Chat-Analyzer/
│── app.py             # Streamlit UI
│── helper.py          # Analytics & stats logic
│── preprocessor.py    # Chat parsing & cleaning
│── README.md
```

---

## ⚙️ Installation

```bash
pip install streamlit pandas matplotlib wordcloud urlextract
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📌 Usage

* Go to WhatsApp → Chat → More → **Export Chat**
* Choose **Without Media**
* Upload the `.txt` file in the app
* Click **Run Analysis**

---

## ⚠️ Note

* This project is for **educational and analytical purposes**
* Avoid uploading sensitive or private chat data publicly

---

## 📈 Future Improvements

* 📊 Activity timeline (daily/monthly trends)
* 🔥 Heatmap (day vs hour activity)
* 😂 Emoji analysis
* 🌐 Deployment (Streamlit Cloud)

---
<img width="1304" height="444" alt="image" src="https://github.com/user-attachments/assets/274e971f-4b4f-4366-8d2b-439fbaf74767" />
<img width="1074" height="417" alt="image" src="https://github.com/user-attachments/assets/af9bf599-7947-4bf2-bece-0b0216560cbc" />
<img width="897" height="644" alt="image" src="https://github.com/user-attachments/assets/64ab119d-d4a8-4c32-a6d7-d08f4c953c9a" />



---
