import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'; // To get event ID from URL
import { getEventById } from '../services/api'; // Pranav’s API
const EventDetailPage = () => {
  const { id } = useParams(); // Get the ID from the URL
  const [event, setEvent] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    getEventById(id).then(data => {
      setEvent(data);
      setLoading(false);
    });
  }, [id]);
  if (loading) return <p>Loading...</p>;
  if (!event) return <p>Event not found!</p>;
  return (
    <div style={{ padding: '1rem' }}>
      <h1>{event.title}</h1>
      <p>{event.date} - {event.location}</p>
      <p>{event.description}</p>
    </div>
  );
};

export default EventDetailPage;
