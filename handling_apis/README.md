# Handling APIs - FreeAPI Username Fetcher

This folder contains Python scripts that interact with external APIs. The script in this folder fetches random user data from the **FreeAPI**.

## 📂 Script: `freeapi_username.py`

This script fetches a random user's data from **FreeAPI** and extracts the following details:

- **Username**
- **Country**

### 🛠️ How It Works:

- The script makes a request to the FreeAPI to fetch random user data.
- It checks if the request is successful (`data["success"]`).
- If successful, it extracts the `username` and `country` of the user and prints them.

### 📥 Dependencies:

- `requests`: Make sure to install the `requests` library if it's not already installed:

```bash
pip install requests
