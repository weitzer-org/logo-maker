# Logo Maker

A modern web application for generating ASCII art text logos.

## Features

- Clean, modern user interface
- Generate ASCII art from text input
- Multiple font styles available
- Copy generated ASCII art to clipboard
- Responsive design for all device sizes

## Installation

1. Clone this repository:
   ```
   git clone git@github.com:google-gemini/logo-maker.git
   cd logo-maker
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### Local Development

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Docker Container

1. Build the Docker image locally:
   ```
   # For Intel/AMD processors
   docker build -t logo-maker .
   
   # For Apple Silicon (M1/M2/M3) Macs
   docker build --platform=linux/amd64 -t logo-maker .
   ```

2. Run the container locally:
   ```
   # Run in the foreground (you'll see logs in the terminal)
   docker run -p 8080:8080 logo-maker
   
   # OR run in detached mode (in the background)
   docker run -d -p 8080:8080 logo-maker
   ```

3. Verify the container is running:
   ```
   docker ps
   ```

4. Check container logs if needed:
   ```
   # Replace CONTAINER_ID with the actual ID from docker ps
   docker logs CONTAINER_ID
   ```

5. Open your web browser and navigate to:
   ```
   http://localhost:8080/
   ```

6. Stop the container when done:
   ```
   # If running in foreground: press Ctrl+C
   # If running in background:
   docker stop CONTAINER_ID
   ```


### Deploying to Google Cloud Run

1. Set your Google Cloud project ID as an environment variable:
   ```sh
   export PROJECT_ID="your-gcp-project-id"
   ```

2. Create an Artifact Registry repository (first time only):
   ```sh
   gcloud artifacts repositories create logo-maker \
     --project=${PROJECT_ID} \
     --repository-format=docker \
     --location=us-central1 \
     --description="Docker repository for Logo Maker application"
   ```

3. Configure Docker to use Google Cloud as a credential helper:
   ```sh
   gcloud auth configure-docker us-central1-docker.pkg.dev
   ```

4. Build the Docker image locally:
   ```sh
   docker build --platform=linux/amd64 -t us-central1-docker.pkg.dev/${PROJECT_ID}/logo-maker/app:latest .
   ```

5. Push the image to Artifact Registry:
   ```sh
   docker push us-central1-docker.pkg.dev/${PROJECT_ID}/logo-maker/app:latest
   ```

   Alternatively, use Cloud Build to build and push in one step (recommended for Cloud Run):
   ```sh
   gcloud builds submit \
     --project=${PROJECT_ID} \
     --tag us-central1-docker.pkg.dev/${PROJECT_ID}/logo-maker/app:latest
   ```

6. Deploy to Cloud Run:
   ```sh
   gcloud run deploy logo-maker \
     --project=${PROJECT_ID} \
     --image us-central1-docker.pkg.dev/${PROJECT_ID}/logo-maker/app:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

7. Access your application at the URL provided by Cloud Run after deployment.

## Customizing ASCII Art Fonts

The application comes with over 100 different ASCII art font styles. To change the default font:

1. Open the `app.py` file
2. Locate the `generate_ascii_art()` function
3. Change the font parameter from 'slant' to any of the fonts listed in the comments
   ```python
   # Change this line:
   ascii_art = pyfiglet.figlet_format(text, font='slant')
   
   # To use a different font, for example:
   ascii_art = pyfiglet.figlet_format(text, font='banner')
   ```

## Project Structure

```
logo-maker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── css/
│       └── style.css      # CSS styles
└── templates/
    └── index.html         # HTML template
```

## Technologies Used

- Python 3
- Flask (Web framework)
- pyfiglet (ASCII art generation)
- HTML/CSS (Frontend)

## Contributing

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in
this project you agree to abide by its terms. See [Code of Conduct](CODE_OF_CONDUCT.md) for more
information.

## License

Apache 2.0 - See [LICENSE](LICENSE) for more information.