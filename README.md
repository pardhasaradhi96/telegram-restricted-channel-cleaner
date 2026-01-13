# telegram-restricted-channel-cleaner
A fast Python script that scans your Telegram account, detects channels blocked due to copyright infringement, and optionally leaves them automatically

problem i face : 
When Telegram’s channel limit is reached, it suggests leaving inactive channels, but it does not highlight channels blocked due to copyright infringement.
This code removes such unusable (copyrighted) channels, freeing up join slots without losing any useful content.

## 🔧 Setup Instructions

### ✅ Step 1: Get Telegram API ID & API Hash

1. Open:  
   👉 https://my.telegram.org/

2. Log in:
   - Enter your phone number with country code  
     Example: `+91XXXXXXXXXX`
   - Click **Next**
   - Enter the confirmation code sent to your Telegram app  
     (check the chat named **Telegram**)

3. After login, click **“API development tools”**

4. Fill the form:
   - **App title** → Any name (e.g., `MyTelegramApp`)
   - **Short name** → Any short identifier (e.g., `myapp`)
   - **Platform** → Anything (Android / Desktop / Web)

5. Click **Create application**

6. Copy your:
   - `api_id` (integer)
   - `api_hash` (string)

---

### ✅ Step 2: Install Python

- Install **Python 3.12+**
- Tested on **Python 3.12.10**

Verify installation:
```bash
python --version
```

---

### ✅ Step 3: Install Required Library

Open **Command Prompt / Terminal** and run:
```bash
pip install telethon
```

---

### ✅ Step 4: Configure the Script

1. Open the file:
```
telegram-restricted-channel-cleaner.py
```

2. Paste your credentials:
```python
api_id = 12345678
api_hash = "12345678901234567890123456789012"
```

> ⚠️ `api_id` must be an **integer**  
> ⚠️ `api_hash` must be a **string**

---

### ✅ Step 5: Run the Script

```bash
python telegram-restricted-channel-cleaner.py
```

#### First run (login required):
- Enter your phone number:
```
Please enter your phone (or bot token): +91XXXXXXXXXX
```
- Enter the login code (from Telegram app)
- Enter your password (if 2FA is enabled)

---

## 📄 What the Script Does

- Scans **all channels** in your account
- Detects channels showing:
  > **This channel is unavailable due to copyright infringement.**
- Displays channel **names + IDs**
- Prompts:
```
Leave all channels? (type yes):
```
- If you type **yes**, it **leaves all detected channels**

---

## 🔁 Future Runs

- Session is saved locally
- Just run again:
```bash
python telegram-restricted-channel-cleaner.py
```
- Type **yes** when prompted

---

## ⚠️ Notes

- Uses **channel IDs**, not names
- Very fast 

---

## 📜 License

For educational and personal use only.
