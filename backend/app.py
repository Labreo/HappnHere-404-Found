from flask import Flask, request, jsonify
from flasgger import Swagger
from datetime import datetime

# -------------------------------------
# Basic Flask App Setup
# -------------------------------------
app = Flask(__name__)
# Configure Swagger UI
swagger = Swagger(app, template={
    "info": {
        "title": "happnHere API",
        "description": "API for finding and managing local events in Goa.",
        "version": "1.0.0"
    },
    "host": "127.0.0.1:5000",
    "schemes": ["http"],
})

# -------------------------------------
# In-Memory Database (using Lists of Dictionaries)
# -------------------------------------
# We use simple lists to store data. In a real application,
# this would be replaced by a database like PostgreSQL or MongoDB.
users = []
events = []
clubs = []
user_id_counter = 1
event_id_counter = 1
club_id_counter = 1

# -----------------------------------------------------------------------------
# USER AUTHENTICATION ENDPOINTS
# -----------------------------------------------------------------------------

@app.route('/api/users/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    ---
    tags:
      - User Authentication
    description: Creates a new user account with the provided details.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
            - password
          properties:
            name:
              type: string
              example: "John Doe"
            email:
              type: string
              example: "john.doe@example.com"
            phone:
              type: string
              example: "9876543210"
            password:
              type: string
              example: "securepassword123"
    responses:
      201:
        description: User registered successfully.
        schema:
          type: object
          properties:
            message:
              type: string
            user_id:
              type: integer
      400:
        description: Bad request, e.g., email already exists or missing fields.
        schema:
          type: object
          properties:
            error:
              type: string
    """
    global user_id_counter
    data = request.get_json()

    if not data or not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({"error": "Missing required fields"}), 400

    if any(u['email'] == data['email'] for u in users):
        return jsonify({"error": "Email already exists"}), 400

    new_user = {
        "id": user_id_counter,
        "name": data['name'],
        "email": data['email'],
        "phone": data.get('phone', ''),
        "password": data['password'], # In a real app, hash this password!
        "profile_pic": "",
        "interests": [],
        "created_at": datetime.utcnow().isoformat()
    }
    users.append(new_user)
    user_id_counter += 1

    return jsonify({"message": "User registered successfully", "user_id": new_user['id']}), 201


@app.route('/api/users/login', methods=['POST'])
def login():
    """
    User login.
    ---
    tags:
      - User Authentication
    description: Authenticates a user and returns a placeholder token.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: "john.doe@example.com"
            password:
              type: string
              example: "securepassword123"
    responses:
      200:
        description: Login successful.
        schema:
          type: object
          properties:
            token:
              type: string
              example: "jwt-token-placeholder-for-demo"
      401:
        description: Invalid credentials.
    """
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400

    user = next((u for u in users if u['email'] == data['email'] and u['password'] == data['password']), None)

    if user:
        # In a real app, you would generate a real JWT token here.
        return jsonify({"token": f"jwt-token-placeholder-for-user-{user['id']}"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# Note: The following /me endpoints are simplified. In a real app, you would extract
# the user ID from a JWT token sent in the Authorization header. For this assignment,
# we will use a static user ID (e.g., user 1) for demonstration.
@app.route('/api/users/me', methods=['GET', 'PUT'])
def user_profile():
    """
    Get or update the current user's profile.
    ---
    get:
      tags:
        - User Authentication
      summary: Get current user profile
      description: Retrieves the profile of the logged-in user (demonstrated with user ID 1).
      responses:
        200:
          description: User profile data.
          schema:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
              profile_pic:
                type: string
        404:
          description: User not found.
    put:
      tags:
        - User Authentication
      summary: Update profile
      description: Updates the profile of the logged-in user (demonstrated with user ID 1).
      parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: "John D."
              profile_pic:
                type: string
                example: "https://example.com/newpic.jpg"
              interests:
                type: array
                items:
                  type: string
                example: ["music", "food"]
      responses:
        200:
          description: Profile updated successfully.
        404:
          description: User not found.
    """
    # Simplified: Assumes user with ID 1 is the "logged-in" user.
    user = next((u for u in users if u['id'] == 1), None)
    if not user:
        return jsonify({"error": "User with ID 1 not found. Please register a user first."}), 404

    if request.method == 'GET':
        return jsonify({
            "id": user['id'],
            "name": user['name'],
            "email": user['email'],
            "profile_pic": user['profile_pic']
        })

    if request.method == 'PUT':
        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'profile_pic' in data:
            user['profile_pic'] = data['profile_pic']
        if 'interests' in data:
            user['interests'] = data['interests']
        return jsonify({"message": "Profile updated successfully"})

# -----------------------------------------------------------------------------
# EVENT ENDPOINTS
# -----------------------------------------------------------------------------

@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    """
    Get all events or create a new event.
    ---
    get:
      tags:
        - Events
      summary: Get all events
      description: Retrieves a list of all available events.
      responses:
        200:
          description: A list of events.
          schema:
            type: array
            items:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
                category:
                  type: string
                location:
                  type: string
                date_time:
                  type: string
                price:
                  type: number
    post:
      tags:
        - Events
      summary: Create an event
      description: Creates a new event (organizer only - not enforced in this demo).
      parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            required:
              - title
              - category
              - location
              - date_time
            properties:
              title:
                type: string
                example: "Goa Food Festival"
              description:
                type: string
                example: "Taste the best dishes in Goa!"
              category:
                type: string
                example: "Food"
              location:
                type: string
                example: "Panaji"
              date_time:
                type: string
                format: date-time
                example: "2025-08-20T18:00:00"
              price:
                type: number
                example: 200
      responses:
        201:
          description: Event created successfully.
        400:
          description: Missing required fields.
    """
    global event_id_counter
    if request.method == 'GET':
        # Return a summary of events
        summary_events = [{k: v for k, v in event.items() if k not in ['description', 'attendees', 'organizer_id']} for event in events]
        return jsonify(summary_events)

    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(k in data for k in ['title', 'category', 'location', 'date_time']):
            return jsonify({"error": "Missing required fields"}), 400

        new_event = {
            "id": event_id_counter,
            "title": data['title'],
            "description": data.get('description', ''),
            "category": data['category'],
            "location": data['location'],
            "date_time": data['date_time'],
            "price": data.get('price', 0),
            "organizer_id": 1,  # Simplified: assume organizer is user 1
            "attendees": [],
            "created_at": datetime.utcnow().isoformat()
        }
        events.append(new_event)
        event_id_counter += 1
        return jsonify({"message": "Event created successfully", "event_id": new_event['id']}), 201

@app.route('/api/events/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_event_by_id(id):
    """
    Get, update, or delete a specific event by its ID.
    ---
    get:
      tags:
        - Events
      summary: Get event by ID
      parameters:
        - in: path
          name: id
          type: integer
          required: true
      responses:
        200:
          description: Detailed information of a single event.
        404:
          description: Event not found.
    put:
      tags:
        - Events
      summary: Update event
      parameters:
        - in: path
          name: id
          type: integer
          required: true
        - in: body
          name: body
          schema:
            type: object
            properties:
              title:
                type: string
              price:
                type: number
      responses:
        200:
          description: Event updated successfully.
        404:
          description: Event not found.
    delete:
      tags:
        - Events
      summary: Delete event
      parameters:
        - in: path
          name: id
          type: integer
          required: true
      responses:
        200:
          description: Event deleted successfully.
        404:
          description: Event not found.
    """
    event = next((e for e in events if e['id'] == id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    if request.method == 'GET':
        return jsonify(event)

    if request.method == 'PUT':
        data = request.get_json()
        event.update(data)
        return jsonify({"message": "Event updated successfully"})

    if request.method == 'DELETE':
        events.remove(event)
        return jsonify({"message": "Event deleted successfully"})


@app.route('/api/events/<int:id>/join', methods=['POST'])
def join_event(id):
    """
    Join an event.
    ---
    tags:
      - Events
    summary: RSVP to an event
    description: Adds the current user (user ID 1 for demo) to the event's attendee list.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Successfully joined the event.
      404:
        description: Event not found.
      400:
        description: User already joined this event.
    """
    event = next((e for e in events if e['id'] == id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # Simplified: assume user 1 is joining
    user_id_to_add = 1
    if user_id_to_add in event['attendees']:
      return jsonify({"error": f"User {user_id_to_add} already joined this event"}), 400

    event['attendees'].append(user_id_to_add)
    return jsonify({"message": "Successfully joined the event"})

# -----------------------------------------------------------------------------
# CLUB & COMMUNITY ENDPOINTS (Simplified)
# -----------------------------------------------------------------------------

@app.route('/api/clubs', methods=['GET', 'POST'])
def handle_clubs():
    """
    Get all clubs or create a new one.
    ---
    get:
      tags:
        - Clubs & Communities
      summary: Get all clubs
      description: Retrieves a list of all clubs.
      responses:
        200:
          description: A list of clubs.
    post:
      tags:
        - Clubs & Communities
      summary: Create a club
      description: Creates a new club.
      parameters:
        - in: body
          name: body
          schema:
            type: object
            properties:
              name:
                type: string
                example: "Goa Hikers Club"
              description:
                type: string
                example: "A club for hiking enthusiasts in Goa."
      responses:
        201:
          description: Club created successfully.
    """
    global club_id_counter
    if request.method == 'GET':
        return jsonify(clubs)

    if request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('name'):
            return jsonify({"error": "Club name is required"}), 400

        new_club = {
            "id": club_id_counter,
            "name": data['name'],
            "description": data.get('description', ''),
            "members": [],
            "created_at": datetime.utcnow().isoformat()
        }
        clubs.append(new_club)
        club_id_counter += 1
        return jsonify({"message": "Club created successfully", "club_id": new_club['id']}), 201


@app.route('/api/clubs/<int:id>/follow', methods=['POST'])
def follow_club(id):
    """
    Follow a club.
    ---
    tags:
      - Clubs & Communities
    summary: Follow a club
    description: Adds the current user (user ID 1 for demo) to the club's member list.
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Successfully followed the club.
      404:
        description: Club not found.
    """
    club = next((c for c in clubs if c['id'] == id), None)
    if not club:
        return jsonify({"error": "Club not found"}), 404

    # Simplified: assume user 1 is following
    user_id_to_add = 1
    if user_id_to_add not in club['members']:
        club['members'].append(user_id_to_add)

    return jsonify({"message": "Successfully followed the club"})

# -----------------------------------------------------------------------------
# PLACEHOLDER ENDPOINTS for Notifications and Payments
# -----------------------------------------------------------------------------

@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    """
    Get notifications.
    ---
    tags:
      - Notifications
    summary: Get user notifications
    description: (Placeholder) Returns a sample list of notifications.
    responses:
      200:
        description: A list of notifications.
    """
    sample_notifications = [
        {"id": 1, "message": "Event 'Goa Food Festival' is starting soon!", "read": False},
        {"id": 2, "message": "New post in 'Goa Hikers Club'", "read": True}
    ]
    return jsonify(sample_notifications)

@app.route('/api/payments', methods=['POST'])
def create_payment():
    """
    Create a payment.
    ---
    tags:
      - Payments
    summary: Create a payment for an event
    description: (Placeholder) Simulates initiating a payment process.
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            event_id:
              type: integer
              example: 1
            amount:
              type: number
              example: 200
    responses:
      201:
        description: Payment initiated.
    """
    data = request.get_json()
    return jsonify({
        "message": "Payment initiated successfully",
        "payment_id": f"pay_{datetime.now().timestamp()}",
        "status": "pending",
        "details": data
    }), 201


@app.route('/api/payments/<string:id>/status', methods=['GET'])
def get_payment_status(id):
    """
    Get payment status.
    ---
    tags:
        - Payments
    summary: Get payment status
    description: (Placeholder) Returns the status of a simulated payment.
    parameters:
      - in: path
        name: id
        type: string
        required: true
        example: "pay_1660214890.123"
    responses:
        200:
            description: Payment status.
    """
    return jsonify({
        "payment_id": id,
        "status": "confirmed",
        "confirmation_time": datetime.utcnow().isoformat()
    })

# -------------------------------------
# Root endpoint for basic health check
# -------------------------------------
@app.route('/')
def index():
    return "Welcome to the happnHere API! Go to /apidocs to see the documentation."

# -------------------------------------
# Main execution block
# -------------------------------------
if __name__ == '__main__':
    app.run(debug=True)