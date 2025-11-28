# Django Blog Platform

A fully functional Blog/Article platform built with Django and Bootstrap.

## Features

- **Posts**: Create, read, update, and delete posts (via Admin).
- **Categories**: Organize posts into categories.
- **Comments**: Users can leave comments on posts (requires Admin approval).
- **Admin Panel**: Customized admin interface for managing content.
- **Responsive Design**: Built with Bootstrap 5.

## Setup

1.  **Clone the repository** (if applicable).
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment**:
    - Windows: `.\venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`
4.  **Install dependencies**:
    ```bash
    pip install django django-crispy-forms crispy-bootstrap5 Pillow
    ```
5.  **Run migrations**:
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
    (Or run `python create_superuser.py` if available)
7.  **Run the server**:
    ```bash
    python manage.py runserver
    ```

## Usage

- **Home**: View all latest posts.
- **Post Detail**: Click on a post to read more and leave a comment.
- **Categories**: Click on a category name to filter posts.
- **Admin**: Go to `/admin/` to log in and manage posts, categories, and comments.

## Project Structure

- `config/`: Main project settings and URLs.
- `blog/`: The blog application (Models, Views, URLs).
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JS).
- `media/`: User-uploaded media (Post images).
