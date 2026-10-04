# Inventory Management System - Flask REST API

This project is a back-end inventory management system built for a small retail company. It features a Flask REST API with full CRUD functionality, an external API integration, a command-line interface (CLI), and a comprehensive unit testing suite.

## Features
* **RESTful API:** Manage inventory using standard HTTP methods (GET, POST, PATCH, DELETE).
* **External API Integration:** Fetches real-time product data using the OpenFoodFacts API.
* **Interactive CLI:** A terminal-based user interface to easily interact with the API without needing a web browser or Postman.
* **Automated Testing:** Fully tested routes using `pytest` and Flask's built-in test client.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd inventory-flask-api