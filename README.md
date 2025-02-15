## 📧 Voice-Controlled Email Bot 🤖

This project is a Python-based email bot that leverages speech recognition to streamline the email sending process.  No more typing! Just tell the bot who you want to email, what you want to say, and it handles the rest! 🚀

### ✨ Features ✨

* **Speech-to-Text:** Uses the `speech_recognition` library to convert your voice commands into text. 🎙️
* **Email Automation:**  Automatically sends emails via SMTP using the `smtplib` library. 📨
* **Environment Variables:** Securely stores your email credentials using the `python-dotenv` library. 🤫
* **Text-to-Speech:** Provides audible feedback using the `pyttsx3` library. 🗣️
* **Contact List:**  Maintains a dictionary of email addresses for easy recipient selection. 📖

### 🚀 How it Works 🚀

1. **Initialization:**  The bot initializes the speech recognizer, text-to-speech engine, and loads your email password from environment variables. ⚙️
2. **Voice Input:** The bot prompts you for recipient name, subject, and email body using voice prompts. 🎤
3. **Email Sending:**  The bot uses your voice input to construct and send the email. 📤
4. **Confirmation:** The bot confirms that the email has been sent and asks if you want to send another. ✅

### 🧰 Technologies Used 🧰

* Python 🐍
* `speech_recognition` 🎤
* `smtplib` 📨
* `pyttsx3` 🗣️
* `python-dotenv` 🤫

### 🏃‍♂️ How to Run 🏃‍♂️

1. **Clone the repository:** `git clone https://github.com/your-username/voice-email-bot.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set up environment variables:** Create a `.env` file and add your email password as `MY_SECRET_PASSWORD`.
4. **Run the script:** `python main.py`

### 💡 Future Enhancements 💡

* **Integration with other services:** Connect with calendar, to-do lists, and more. 📅
* **Natural Language Processing:**  Enable more sophisticated voice commands and email content generation. 🧠
* **GUI:** Develop a user-friendly graphical interface. 🖥️

**Have fun sending emails with your voice!** 🎉
