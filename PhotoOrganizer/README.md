# Image Tagging and Search with Django, OpenAI, and spaCy

This project is a web application built with Django that uses OpenAI for image analysis and spaCy for natural language processing. The application allows users to upload images, tag them automatically using OpenAI, and search for images based on the generated tags.

This project was created based on the Zenva course: [Link](https://academy.zenva.com/course/openai-vision-apps/)


## Features

- **Image Upload**: Users can upload images to the web application.
- **Automatic Tagging**: Images are automatically tagged using OpenAI's image analysis API.
- **Tag Search**: Users can search for images based on tags using spaCy for natural language processing.

## Requirements

- Python 3.x
- Django 3.x or later
- OpenAI API key
- spaCy
- requests

## Installation

1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install spaCy model**:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4. **Configure environment variables**:
    Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Upload an Image**:
   - Go to `http://localhost:8000/gallery/upload/`.
   - Upload an image file.

2. **Automatic Tagging**:
   - The uploaded image will be automatically tagged using OpenAI's API.

3. **Search for Images**:
   - Go to `http://localhost:8000/gallery/search/`.
   - Enter a search term to find images based on the generated tags.

4. **See the tags created**:
   - Go to `http://localhost:8000/gallery/admin/`.
   - You will need to create a Django superuser to access it
   - Find all uploaded images and see their tags

