# Penguin Dashboard

## Overview

The Penguin Dashboard is a web application designed to visualize and analyze data on penguins. This project utilizes Vue.js for the front end and Flask as the back end to serve data and handle user interactions. Users can filter penguin data through a set of sliders and dropdowns, dynamically updating scatter plots and histograms based on their selections.

![Penguin Dashboard](client/src/assets/screencapture.png)

## Features

- Interactive scatter plots and histograms.
- Filtering options based on species, island, flipper length, and body mass.
- Responsive design for a seamless user experience.

## Technologies Used

- **Frontend**: Vue.js, Plotly.js
- **Backend**: Flask, Pandas
- **Package Management**: Pipenv

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Node.js
- Pipenv

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pebueno/penguin-dashboard.git
   cd penguin-dashboard
   ```

2. **Set up the Backend:**

   Navigate to the server directory:

   ```bash
   cd server
    ```
   Install dependencies using Pipenv:
   ```bash
   pipenv install
    ```
   Run the Flask server:
   ```bash
    pipenv shell
    flask run
    ```
    *Your backend will run on localhost:5000/api/data*

3. **Set up the Frontend:**

   Navigate to the client directory: *(You should do it in another shell and run both concurrently)*

   ```bash
   cd client
   ```

    Install dependencies using npm:
    ```bash
    npm install
    ```

    Run the Vue.js application:
    ```bash
    npm run dev
    ```