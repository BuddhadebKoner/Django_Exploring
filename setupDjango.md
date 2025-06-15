# Django: Getting Started Guide

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. This guide will walk you through setting up your first Django project, creating a virtual environment, installing Django, and running your development server.

---

## 1. Setting Up a Python Virtual Environment

A virtual environment is an isolated environment for Python projects. It ensures your project dependencies are maintained separately.

```bash
python -m venv <environment_name>
```
- Replace `<environment_name>` with your preferred environment name (commonly `.venv` or `env`).

**Example:**
```bash
python -m venv .venv
```

### Activating the Virtual Environment

On **Linux/macOS**:
```bash
source .venv/bin/activate
```

On **Windows**:
```bash
.venv\Scripts\activate
```

When activated, your terminal prompt should change, indicating you're now inside the virtual environment.

---

## 2. Installing Django

With your virtual environment activated, install Django using pip:

```bash
pip install Django
```

You can verify the Django installation with:

```bash
python -m django --version
```

---

## 3. Creating a New Django Project

To create a new Django project, use the `django-admin` tool:

```bash
django-admin startproject my_website
```

- This command creates a new directory called `my_website` containing the initial project structure.

**Directory structure:**
```
my_website/
    manage.py
    my_website/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

> **Tip:** You can replace `my_website` with your desired project name.

---

## 4. Navigating to Your Project Directory

Change directory into your project folder (e.g., `jinjaTesting`):

```bash
cd jinjaTesting
```

> Replace `jinjaTesting` with your actual project folder name.

---

## 5. Running the Django Development Server

Start the built-in development server with:

```bash
python manage.py runserver
```

- By default, the server runs at `http://127.0.0.1:8000/`.
- Open this URL in your browser to see the Django welcome page.

**Additional Options:**
- To run the server on a different port:
  ```bash
  python manage.py runserver 8080
  ```
- To specify an IP and port:
  ```bash
  python manage.py runserver 0.0.0.0:8000
  ```

---

## 6. Next Steps

Now that your Django project is running, you can:
- Create apps within your project using `python manage.py startapp <app_name>`.
- Define models, views, and templates.
- Configure URLs and settings.
- Use Django's ORM, authentication system, and admin interface.

---

## 7. Common Django Commands

| Command                                          | Description                                    |
|--------------------------------------------------|------------------------------------------------|
| `python manage.py migrate`                       | Applies database migrations                    |
| `python manage.py createsuperuser`               | Creates an admin user                          |
| `python manage.py startapp <app_name>`           | Starts a new Django app                        |
| `python manage.py makemigrations`                | Prepares changes to your models for migration  |
| `python manage.py shell`                         | Opens a Python shell with Django context       |

---

## 8. Useful References

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Project Structure Explained](https://docs.djangoproject.com/en/stable/intro/overview/)
- [Virtual Environments in Python](https://docs.python.org/3/library/venv.html)

---

## 9. Example Session

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Django
pip install Django

# Start a new Django project
django-admin startproject jinjaTesting

# Move into your project directory
cd jinjaTesting

# Run the development server
python manage.py runserver
```

You should now be able to access your Django project in your web browser!

---