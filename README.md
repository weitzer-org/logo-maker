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

1. Set your Google Cloud project ID, location, and service name as environment variables:
   ```sh
   export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
   export GOOGLE_CLOUD_LOCATION="us-central1"  # or your preferred region
   export LOGO_MAKER_SERVICE="logo-maker"      # or your preferred service name
   ```

2. Create an Artifact Registry repository (first time only):
   ```sh
   gcloud artifacts repositories create ${LOGO_MAKER_SERVICE} \
     --project=${GOOGLE_CLOUD_PROJECT} \
     --repository-format=docker \
     --location=${GOOGLE_CLOUD_LOCATION} \
     --description="Docker repository for Logo Maker application"
   ```

3. Configure Docker to use Google Cloud as a credential helper:
   ```sh
   gcloud auth configure-docker \
     ${GOOGLE_CLOUD_LOCATION}-docker.pkg.dev
   ```

4. Build and push the Docker image with Cloud Build:
   ```sh
   gcloud builds submit \
     --project=${GOOGLE_CLOUD_PROJECT} \
     --tag ${GOOGLE_CLOUD_LOCATION}-docker.pkg.dev/${GOOGLE_CLOUD_PROJECT}/logo-maker/app:latest
   ```

5. Deploy to Cloud Run:
   ```sh
   gcloud run deploy ${LOGO_MAKER_SERVICE} \
     --project=${GOOGLE_CLOUD_PROJECT} \
     --image ${GOOGLE_CLOUD_LOCATION}-docker.pkg.dev/${GOOGLE_CLOUD_PROJECT}/${LOGO_MAKER_SERVICE}/app:latest \
     --platform managed \
     --region=${GOOGLE_CLOUD_LOCATION} \
     --allow-unauthenticated
   ```

6. Access your application at the URL provided by Cloud Run after deployment.

## Running the GitHub Actions Cloud Run Deployment Workflow

This project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically builds and deploys your app to Google Cloud Run on every push to `main` and for every pull request (PR) for preview deployments.

### How to Use

1. In your GitHub repository, go to **Settings > Variables** and add the following repository variables:
   - `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID
   - `GOOGLE_CLOUD_LOCATION`: The region for your Cloud Run service (e.g., `us-central1`)
   - `GCP_WIF_PROVIDER`: The Workload Identity Federation provider resource name

2. Push to the `main` branch or open a pull request. The workflow will:
   - Build and push a Docker image to Artifact Registry using Cloud Build
   - Deploy to Cloud Run
   - For PRs, deploy to a unique preview service (e.g., `pr-123-logo-maker`)
   - For `main`, deploy to the production service (default: `logo-maker`)

3. The workflow output will include the deployed service URL.

**Note:**
- By default, deployed services require authentication. To make the service public, add `--allow-unauthenticated` to the deploy step in `.github/workflows/ci.yml`.
- You can monitor workflow runs and logs in the **Actions** tab of your GitHub repository.

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