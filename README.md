📝 Be_er Blogging API

A Django REST Framework–based blogging API that allows users to create, edit, publish, and delete blog posts. The project is designed to serve as the backend for a modern blog platform.

🚀 Features

User registration and login (authentication-ready setup)

Create, edit, delete, and publish/unpublish posts

Featured images and image galleries for posts

RESTful API endpoints for easy frontend integration

Organized folder structure for scalability

Home route returning a simple welcome message

🗂️ Project Structure
Be_er-blogging-API/
├── be_er/
│   ├── be_er/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── manage.py
├── venv/
└── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/Be_er-blogging-API.git
cd Be_er-blogging-API

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
django, djangoretframework

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Run the development server
python manage.py runserver


Then open your browser and visit:

http://127.0.0.1:8000/

📡 API Endpoints
Method	Endpoint	Description
GET	/	Home page
GET	/api/posts/	List all posts
POST	/api/posts/	Create a new post
GET	/api/posts/<id>/	Retrieve a single post
PUT	/api/posts/<id>/	Update a post
DELETE	/api/posts/<id>/	Delete a post
PATCH	/api/posts/<id>/publish/	Publish/unpublish a post
🧩 Tech Stack

Backend: Django, Django REST Framework

Language: Python 3.13

Database: Mysql

Auth: Django’s built-in user system

🧠 Future Improvements

Add user registration & JWT authentication endpoints

Add comments and likes

Enable search and filtering for posts

Add API documentation with Swagger or ReDoc

🧑‍💻 Author

Bethelhem Daniel Fenta
Passionate backend developer building meaningful and scalable applications.
