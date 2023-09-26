import React from "react";
import "./NavBar.css";

const NavBar = () => {
  return (
    <div className="Navbar">
      <div className="n-left">
        <div className="Getting-Started">
          <a href="/">Getting Started</a>
        </div>
        <div className="About">
          <a href="/">About</a>
        </div>
        <div className="Exhibitions">
          <a href="/">Exhibitions</a>
        </div>
        <div className="Products">
          <a href="/">Products</a>
        </div>
        <div className="Media">
          <a href="/">Media</a>
        </div>
        <div className="Apply online">
          <a href="/">Apply online</a>
        </div>
        <div className="Contact">
          <a href="/">Contact</a>
        </div>
        <div className="Shop">
          <a href="/">Shop</a>
        </div>
        <div className="Search-here">Search Here</div>
      </div>
    </div>
  );
};

export default NavBar;
