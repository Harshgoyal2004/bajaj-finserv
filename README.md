# Bajaj Finserv Health Full Stack Assessment

This project is a REST API built with Flask that processes an array of data and returns a structured JSON response.

## API Endpoint

- **Method**: POST
- **Route**: `/bfhl`

## Setup and Deployment

### Prerequisites

- Python 3.x
- Pip
- Git

### Local Setup

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   flask run
   ```

The API will be running at `http://127.0.0.1:5000`.

### Deployment to Vercel

1. **Create a Vercel account** at [vercel.com](https://vercel.com).

2. **Install the Vercel CLI:**

   ```bash
   npm install -g vercel
   ```

3. **Log in to your Vercel account:**

   ```bash
   vercel login
   ```

4. **Deploy the application:**

   ```bash
   vercel
   ```

Vercel will automatically detect the Flask application and deploy it. After deployment, you will receive a unique URL for your API.

## Submitting Your Solution

1. **Push your code to a public GitHub repository.**

2. **Submit the following information to the form at [forms.office.com/r/ZeVpUYp3zV](https://forms.office.com/r/ZeVpUYp3zV):**

   - Your Name
   - Roll Number
   - Email ID
   - GitHub repository URL
   - Hosted API URL (including the `/bfhl` route)