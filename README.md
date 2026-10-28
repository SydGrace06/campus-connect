# Campus Connect

Campus Connect is a campus event finder that helps students discover, save, and register for campus events.

## Project Goals

- Browse campus events by date, location, club, and category.
- Search and filter events.
- View event locations on an interactive map using Leaflet.
- Allow students to favorite and register for events.
- Allow club organizers to create and manage events.

## Technology Stack

- **Frontend:** TypeScript
- **Backend:** Python and Flask
- **Database:** SQLAlchemy
- **Map:** Leaflet with OpenStreetMap

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/campus-connect.git
cd campus-connect
```

Replace `YOUR-USERNAME` with the GitHub username or organization that owns the repository.

### 2. Create a Python virtual environment

Make sure Python 3 and the `venv` package are installed.

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux or WSL:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

Once the Flask application is configured, run it using the command specified by the project. For example, if the Flask application entry point is `app.py`:

```bash
flask --app app run --debug
```

Open the local URL printed in your terminal, usually `http://127.0.0.1:5000`.

**Note:** The application may require database initialization and environment variables before it can run. Follow any additional instructions provided by the team.


## Project Status

Currently in development phase 1.
