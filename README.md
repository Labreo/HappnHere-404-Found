# HappnHere-404-Found

## HappnHere

Goa’s vibrant and diverse event scene is often fragmented and under-promoted. Tourists and even locals miss out on exciting activities simply because they’re not aware of what’s happening nearby. Grassroots events such as free or low-cost community gatherings, cultural performances like Tiatrs and Nataks, independent shows by local artists or performers with small fanbases, and various social, technical, or educational meetups are typically under-promoted or scattered across multiple unorganized platforms. As a result, many people miss out not just due to limited visibility, but also because they lack company or are unaware of communities that share their interests.

## Teammates

[Link to Gracy's Github](https://github.com/gracyntaxx)

[Link to Kanak's Github](https://github.com/Labreo)

[Link to Ruben's Github](https://github.com/Rub3n404)

[Link to Pranav's Github](https://github.com/pranavbhat55)

[Link to Flavia's Github](https://github.com/flavia2706)

## Tech Stack

[TBD]

# happnHere - Backend Server

The backend directory contains the Python Flask backend for the happnHere application. It provides all the necessary API endpoints to manage users, events, and clubs, using a simple in-memory data store.

The API is fully documented using Swagger/OpenAPI, which is accessible for interactive testing.

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.8+
- `pip` (Python package installer)

### **Instructions**

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd happnHere/backend
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    - **macOS/Linux:**
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - **Windows:**
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

3.  **Install Dependencies:**
    Install all the required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Server:**
    Start the Flask development server.
    ```bash
    python backend/app.py
    ```

    You should see output indicating that the server is running, typically on `http://127.0.0.1:5000`.

    ```
     * Serving Flask app 'app'
     * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000) (Press CTRL+C to quit)
    ```

---

## **Accessing the API Documentation**

Once the server is running, you can access the interactive Swagger UI to view all endpoints and test them directly from your browser.

-   **Swagger UI URL:** [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)



From this interface, you can:
-   View all available API endpoints.
-   See details about request parameters, headers, and body schemas.
-   Execute API requests and see live responses.


