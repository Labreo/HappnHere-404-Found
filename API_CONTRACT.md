# **happnHere – API Contract**

## **1. Application Features**

1. **User Registration & Authentication**

   * Sign up with email/phone.
   * Login & logout.
   * Profile creation & editing.
   * Profile picture upload.

2. **Event Discovery**

   * Browse free & paid events in Goa.
   * Search by category (music, food, sports, culture, tech).
   * Filter by date, price, location.
   * View event details (time, location, description, price).

3. **Local Business Promotion**

   * Businesses can create event listings.
   * Highlight featured events.
   * Add offers or discounts.

4. **Social Matching**

   * See other users attending the same event.
   * Connect with people having similar interests.
   * Join communities/clubs.

5. **Event Management**

   * Create, update, delete events (organizer access).
   * Set RSVP limits.
   * Track attendees.

6. **Community Features**

   * Users can follow clubs/organizers.
   * Create interest-based groups.
   * Group chats/events.

7. **Notifications**

   * Event reminders.
   * Updates from followed organizers/clubs.
   * Special offers & announcements.

8. **Payments (for Paid Events)**

   * Secure checkout.
   * Payment confirmation.

---

## **2. Data Models**

### **User**

| Field        | Type     | Description                 |
| ------------ | -------- | --------------------------- |
| id           | Integer  | Unique user ID              |
| name         | String   | Full name                   |
| email        | String   | Email address               |
| phone        | String   | Phone number                |
| password     | String   | Hashed password             |
| profile\_pic | String   | URL to profile picture      |
| interests    | Array    | List of interest categories |
| created\_at  | DateTime | Account creation date       |

---

### **Event**

| Field         | Type     | Description                          |
| ------------- | -------- | ------------------------------------ |
| id            | Integer  | Unique event ID                      |
| title         | String   | Event title                          |
| description   | String   | Event details                        |
| category      | String   | Event type (music, food, tech, etc.) |
| location      | String   | Address or venue name                |
| date\_time    | DateTime | Event start time                     |
| price         | Decimal  | Ticket price (0 if free)             |
| organizer\_id | Integer  | User ID of organizer                 |
| attendees     | Array    | List of user IDs                     |
| created\_at   | DateTime | Date created                         |

---

### **Club/Community**

| Field       | Type     | Description      |
| ----------- | -------- | ---------------- |
| id          | Integer  | Unique club ID   |
| name        | String   | Club name        |
| description | String   | Club purpose     |
| members     | Array    | List of user IDs |
| created\_at | DateTime | Date created     |

---

## **3. API Endpoints**

---

### **User Authentication**

**Feature:** Register New User
**Method:** POST
**Endpoint:** `/api/users/register`
**Description:** Create a new user account.
**Request Body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "password": "securepassword"
}
```

**Success Response (201):**

```json
{
  "message": "User registered successfully",
  "user_id": 12
}
```

**Error Response (400):**

```json
{
  "error": "Email already exists"
}
```

---

**Feature:** Login
**Method:** POST
**Endpoint:** `/api/users/login`
**Description:** Authenticate user and return token.
**Request Body:**

```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Success Response (200):**

```json
{
  "token": "jwt-token-here"
}
```

**Error Response (401):**

```json
{
  "error": "Invalid credentials"
}
```

---

**Feature:** Get Current User Profile
**Method:** GET
**Endpoint:** `/api/users/me`
**Description:** Get details of logged-in user.
**Success Response (200):**

```json
{
  "id": 12,
  "name": "John Doe",
  "email": "john@example.com",
  "profile_pic": "https://example.com/pic.jpg"
}
```

---

### **Events**

**Feature:** Get All Events
**Method:** GET
**Endpoint:** `/api/events`
**Description:** Retrieve all events.
**Success Response (200):**

```json
[
  {
    "id": 1,
    "title": "Goa Food Festival",
    "category": "Food",
    "location": "Panaji",
    "date_time": "2025-08-20T18:00:00",
    "price": 200
  }
]
```

---

**Feature:** Create Event
**Method:** POST
**Endpoint:** `/api/events`
**Description:** Create a new event (organizer only).
**Request Body:**

```json
{
  "title": "Goa Food Festival",
  "description": "Taste the best dishes in Goa!",
  "category": "Food",
  "location": "Panaji",
  "date_time": "2025-08-20T18:00:00",
  "price": 200
}
```

**Success Response (201):**

```json
{
  "message": "Event created successfully",
  "event_id": 45
}
```

**Error Response (403):**

```json
{
  "error": "Unauthorized"
}
```

---

*(Continue similarly for join event, get event by ID, follow clubs, etc.)*

---

## **4. Notes**

* All protected endpoints require **JWT authentication** in headers.
* Errors follow this format:

```json
{
  "error": "Error message here"
}
```

---



If you want, I can also **finish the remaining endpoints list** so your file is 100% complete before committing — that way your teammates won’t need to fill in much.
Do you want me to do that now so you just copy-paste?
