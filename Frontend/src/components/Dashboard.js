import React, { useState, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import ExpenseChart from "./components/ExpenseChart";
import ExpenseTable from "./components/ExpenseTable";
import "./styles.css";

const Dashboard = () => {
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div className={`dashboard-container ${windowWidth < 768 ? "mobile" : "desktop"}`}>
      <Sidebar />
      <div className="main-content">
        <Header />
        <div className="dashboard-content">
          <ExpenseChart />
          <ExpenseTable />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;