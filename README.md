
# 🛠️ Web Fullstack Starter — Django + Next.js

這是一個前後端分離的全端專案範本，使用 Django（後端 API）與 Next.js（前端）構建，包含：

- ✅ 使用者 CRUD API
- ✅ Django Admin 後台
- ✅ Faker 假資料自動生成
- 🔜 JWT 登入 / 註冊系統（開發中）

---

## 📁 專案結構
    web-django/ 
    ├── web-backend/ # Django 後端 
    │   ├── backend/ # Django 設定檔（settings, urls） 
    │   ├── users/ # 使用者 App（CRUD API, model, serializer） 
    │   └── manage.py 
    │ 
    ├── frontend/ # Next.js 前端（預設空） 
    │   └── ... # 可用於串接 API 顯示資料 
    │   
    ├── .github/ # CI/CD 或 GitHub workflows（可選） 
    ├── README.md # 本文件

---

## ⚙️ 環境安裝指南

### 後端（Django）

```bash
cd web-django/backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # 建立管理者帳號
python manage.py runserver # 啟動後端
```
後台入口：http://localhost:8000/admin/

自動建立假資料（可選）

```bash
python users/create_fake_users.py
```

📡 API 範例
方法	路徑	說明
GET	/api/users/	取得所有使用者
POST	/api/users/	建立新使用者
GET	/api/users/<id>/	單一使用者查詢
PUT	/api/users/<id>/	更新使用者
DELETE	/api/users/<id>/	刪除使用者

🧪 技術棧
🔙 Django 5.1 + Django REST Framework

📄 SQLite 預設資料庫（可換 PostgreSQL）

🎭 Faker 產生測試假資料

🔜 Next.js 前端整合

🔐 JWT 登入驗證（即將實作）

📌 待辦規劃（Roadmap）
 User CRUD API

 Admin 後台模型註冊

 Faker 假資料產生

 JWT 驗證系統

 前端串接 Next.js 顯示使用者清單

 註冊 / 登入前端畫面

 Docker 化 & CI/CD 部署

🤝 作者
由 vince115 製作，歡迎交流與改進建議 🙌
