# FAQ Management System

This is a Django-based FAQ management system that allows you to store, manage, and retrieve FAQs with multi-language translation support. It includes a REST API, caching with Redis, and a user-friendly admin interface.

---

## Features
- **FAQ Management**: Store FAQs with questions and answers.
- **Multi-language Support**: Automatically translate FAQs into multiple languages (e.g., Hindi, Bengali) using the Google Translate API.
- **WYSIWYG Editor**: Use a rich text editor (CKEditor) to format answers.
- **REST API**: Fetch FAQs in different languages via API.
- **Caching**: Improve performance with Redis caching for translations.
- **Admin Panel**: Manage FAQs through Django’s admin interface.
- **Unit Tests**: Ensure code quality with unit tests.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.9 or higher
- Redis
- Git

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/faq-project.git
cd faq-project
