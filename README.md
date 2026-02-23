### Environment Variables
Before starting, you need to create an `.env` file for your Django backend with the necessary environment variables.

1.  **Create `health/.env`:**
    Create a file named `.env` inside the `health/` directory with the following content. **Remember to replace placeholder values with your actual secrets.**

    ```dotenv
    SECRET_KEY=your_secret_key_here_change_this_in_production
    DEBUG=True
    POSTGRES_DB=healthdb
    POSTGRES_USER=healthuser
    POSTGRES_PASSWORD=healthpassword
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
2.  **Create `health_front/.env` (Optional):**
    If your React frontend requires specific environment variables (e.g., API keys, base URLs), create a `.env` file in the `health_front/` directory.

### Building and Running
1.  **Navigate to the project root:**
    Open your terminal and change directory to the root of this project, where `docker-compose.yml` is located.
    ```bash
    cd /health-ai_check
    ```
2.  **Build the Docker images:**
    This command will build the Docker images for the `health` (Django) and `health_front` (React) services, as well as pull the `postgres` image.
    ```bash
    docker-compose build
    ```
3.  **Start the services:**
    Once the images are built, start all services in detached mode (runs in the background).
    ```bash
    docker-compose up -d
    ```
    This will start the PostgreSQL database, run Django migrations, start the Django backend using Gunicorn, and start the React development server.

### Accessing Applications
After the services are up and running:
-   **Django Backend (API):** `http://localhost:8000`
-   **React Frontend:** `http://localhost:3000`

### Stopping Services
To stop all running services and remove their containers, networks, and volumes (for PostgreSQL data volume, it will remain unless you use `-v` option):
```bash
docker-compose down
```
To remove volumes as well:
```bash
docker-compose down -v
```

### Viewing Logs
To view the logs from all running services in real-time:
```bash
docker-compose logs -f
```
To view logs for a specific service (e.g., `health`):
```bash
docker-compose logs -f health
```

## Local Development (Optional)
If you prefer to run the backend or frontend locally without Docker Compose (e.g., for faster iteration on one part), you can do so. **Note: For local development of the backend, you'll still need a PostgreSQL database running, which you can provide via Docker Compose by only starting the `db` service.**

### Backend (Django)

1.  **Start Database (if not already running):**
    ```bash
    docker-compose up -d db
    ```
2.  **Navigate to backend directory:**
    ```bash
    cd health
    ```
3.  **Create a Python virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Apply migrations:**
    Ensure your `health/.env` file is configured for your local PostgreSQL (if not using the Dockerized `db` service, you'll need to adjust `POSTGRES_HOST` and `POSTGRES_PORT` in `.env` to point to your local DB).
    ```bash
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

### Frontend (React)

1.  **Navigate to frontend directory:**
    ```bash
    cd health_front
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Start the development server:**
    ```bash
    npm start
    ```
    This will usually open `http://localhost:3000` in your browser.
