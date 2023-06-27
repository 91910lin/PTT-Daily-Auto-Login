## PTT Daily Auto Login Python

##### 使用 Python 實作的 PTT 自動登入程式

### 內含檔案

---

**Login.py**

> 程式本體

**Login.bat**

> Windows 的執行程序，用來呼叫 Login.py，可以設定工作排程器來達成每日固定時間自動登入

**python_env.txt**

> 紀錄 Python 當下的套件(Python 版本是 3.11.1)，只要有 PTTLibrary 及 json 這兩個套件程式應該就能執行

**.gitignore**

> 設定 git 的忽略資料夾，本程式忽略的檔案為 file.json

**file.json**

> 請自行新增一個 file.json，內容為 json 格式的 PTT 帳號及密碼(如以下)

```json
{
    "username": "你的PTT帳號",
    "password": "你的PTT密碼"
}
```
