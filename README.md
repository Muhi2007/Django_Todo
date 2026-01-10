# Django Todo List App

A full-featured task management web application built with Django. This app allows users to create accounts, manage task groups, and track individual to-do items with a clean, responsive interface.

## 🚀 Features

* **User Authentication:** Secure Sign Up, Log In, and Log Out functionalities.
* **Profile Management:** Users can upload profile pictures, which are automatically resized for optimization.
* **Task Groups:** Organize tasks into specific categories or groups (e.g., "Work", "Groceries").
* **Todo Management:**
    * Add new items to specific groups.
    * Mark items as "Done" or "Undo" with a single click.
    * Edit existing tasks.
* **Password Reset:** Functional email-based password reset system.
* **Route Protection:** Users can only access and edit their own data.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (Default)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Utilities:**
    * `Pillow` (Image processing)
    * `django-crispy-forms` (Form styling)
    * `python-dotenv` (Environment variable management)

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone (https://github.com/Muhi2007/Django_Todo)
cd todo_list
```

### 2. Create and Activate Virtual Environment
```bash
#For windows
python -m venv venv
venv/Scripts/activate

#For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environmental Variables
Create a .env file in the root directory (same directory as manage.py file).

```
SECRET_KEY=your_django_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server

```bash
python manage.py runserver
```

## 🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.