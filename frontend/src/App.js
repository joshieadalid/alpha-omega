import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import MainMenu from "./pages/MainMenu";
import MeetingMode from "./pages/MeetingMode";
import MinutesMode from "./pages/MinutesMode";
import About from "./pages/About";
import MinutesHistory from "./pages/MinutesHistory";
import WelcomeScreen from "./pages/Welcome";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/menu" element={<MainMenu />} />
        <Route path="/meeting-mode" element={<MeetingMode />} />
        <Route path="/minutes-mode" element={<MinutesMode />} />
        <Route path="/about" element={<About />} />
        <Route path="/minutes-history" element={<MinutesHistory />} />
      </Routes>
    </Router>
  );
}

export default App;
