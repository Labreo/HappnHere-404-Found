import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import EventList from "./pages/EventList";
import EventDetails from "./pages/EventDetails";

function App() {
  return (
    <Router>
      <div style={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>
        <Navbar />
        <div style={{ flex: 1, padding: "1rem" }}>
          <Routes>
            <Route path="/" element={<EventList />} />
            <Route path="/events/:id" element={<EventDetails />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
