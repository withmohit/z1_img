# Image Resizer & X (Twitter) Auto-Post Web App

## 🚀 Tech Stack
- **Frontend:** ReactJS
- **Backend:** FastAPI (Python)
- **Database:** None (Uses local file storage for images)
- **Authentication:** X (Twitter) OAuth 1.0a (for posting images)
- **Hosting:** TBD

---

## 🔹 API Endpoints
### **Auth APIs**
- `GET /auth/login` → Redirects user to X (Twitter) authentication
- `GET /auth/callback` → Handles X (Twitter) OAuth callback and retrieves tokens

### **Image Processing APIs**
- `POST /upload` → Uploads an image and resizes it to predefined dimensions
- `GET /images` → Lists resized images

### **Twitter APIs**
- `POST /post` → Posts resized images to X (Twitter) (Requires paid API)

---

## 🔹 About X (Twitter) API
- **Free Tier:** Allows only text tweets (No media uploads)
- **Basic Plan ($100/month):** Required for posting images
- **OAuth 1.0a:** Used for posting images & tweets
- **OAuth 2.0:** Can be used for login & read-only access

🔗 [X API Pricing & Docs](https://developer.twitter.com/en/pricing)

---

📌 **Note:** To upload images to X (Twitter), you must subscribe to a **paid API plan**. The free tier does **not** support media uploads.

🚀 **Happy Coding!**

