import React from "react";
import { Link } from "react-router-dom";

function EventList() {
  const events = [
    { id: 1, name: "Goa Beach Party" },
    { id: 2, name: "Tech Meetup" },
  ];

  return (
    <div>
      <h2>Upcoming Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            <Link to={`/events/${event.id}`}>{event.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EventList;
