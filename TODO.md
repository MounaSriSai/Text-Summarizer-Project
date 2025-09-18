# TODO for Building and Running Text Summarizer Docker Container

## Steps to Complete:
- [ ] Build the Docker image using `docker build -t text-summarizer .`
- [ ] Run the Docker container using `docker run -p 8080:8080 text-summarizer`
- [ ] Test the FastAPI endpoints (e.g., /docs, /predict)
- [ ] Verify the app is running correctly on localhost:8080

## Notes:
- Ensure Docker Desktop is running (from the provided log, it appears to be installed and up to date).
- The Dockerfile uses Python 3.8, installs dependencies, and runs app.py with FastAPI on port 8080.
- If any issues arise during build or run, troubleshoot based on error messages.
