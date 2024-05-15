# Get Random Anime PFP

This is a Flask-based web application that provides random anime profile pictures (PFP). It uses a SQLite database to store information about available avatars and provides endpoints to fetch and download avatars in various formats and sizes.

## Features

- Fetch a random anime avatar.
- Download avatars in different formats (`jpeg`, `png`, `webp`, `jpg`) and sizes.
- Responsive design with Tailwind CSS.
- Easy setup and deployment.

## Project Structure

```plaintext
get-random-anime-pfp/
├── static/
│   ├── avatars/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── app.py
├── db.sqlite3
└── README.md
```

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ch1kulya/get-random-anime-pfp.git
   cd get-random-anime-pfp
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```sh
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Fetch a random avatar:**

   Go to the homepage and click on "Get Anime PFP" to fetch a random anime avatar.

2. **Download the avatar:**

   Select the desired format and dimensions, then click on "Download" to download the avatar.

## API Endpoints

- **GET `/random-avatar`**: Fetch a random avatar.
- **GET `/download/<int:avatar_id>/<format>/<int:width>/<int:height>`**: Download an avatar with specified format and dimensions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

Created by [ch1kulya](https://github.com/ch1kulya) - feel free to contact me!
