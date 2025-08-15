import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "1rem 2rem",
      backgroundColor: "#4CAF50",
      color: "white"
    }}>
      <h1>happnHere</h1>
      <div>
        <Link to="/" style={{ color: "white", textDecoration: "none" }}>Events</Link>
      </div>
    </nav>
  );
}

export default Navbar;
