# Personal Blog – Built with Django, Python & HTMX

Welcome to my personal blog project! This web application is built using **Django** for the backend, **Python** as the core programming language, and **HTMX** for dynamic and modern frontend interactivity without writing heavy JavaScript.

## Features

- Clean and responsive blog layout
- Create, edit, and delete posts (CRUD)
- HTMX-powered dynamic content loading (e.g. comments, pagination, inline editing)
- Lightweight frontend with progressive enhancement
- Admin interface for managing content
- Markdown support for blog posts (optional)
- SEO-friendly structure

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Tailwind CSS (or Bootstrap), HTMX
- **Database**: SQLite (default), easily swappable with PostgreSQL or MySQL
- **Templating**: Django Templates
- **Dynamic UI**: HTMX for AJAX-like interactions without writing JS

## How HTMX Is Used
HTMX is used throughout the site to enhance interactivity:

- **Inline Post Editing**: Edit posts without a full page reload.
- **Comment Loading**: Fetch and submit comments dynamically.
- **Pagination**: Paginate posts with partial HTML updates.
- **Form Handling**: Submit and validate forms asynchronously.

All of this is accomplished without writing custom JavaScript — just using HTMX attributes like hx-get, hx-post, hx-target, and hx-swap.

## Author
Matthew Johnson

## License
This project is licensed under the MIT License.
