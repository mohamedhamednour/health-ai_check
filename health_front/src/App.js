import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Patients from './components/Patients';
import Consultations from './components/Consultations';
import ConsultationAISummary from './components/ConsultationAISummary';
import './App.css';

function App() {
  return (
    <div className="App min-h-screen bg-gray-100">
      <nav className="bg-white shadow-lg mb-8">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-16">
            <div className="flex space-x-8 items-center">
              <Link to="/" className="text-xl font-bold text-blue-600">Health App</Link>
              <Link to="/patients" className="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md font-medium">
                Patients
              </Link>
              <Link to="/consultations" className="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md font-medium">
                Consultations
              </Link>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Routes>
          <Route path="/patients" element={<Patients />} />
          <Route path="/consultations" element={<Consultations />} />
          <Route path="/consultations/:id/summary" element={<ConsultationAISummary />} />
          <Route path="/" element={
            <div className="text-center py-12">
              <h1 className="text-4xl font-bold text-gray-900 mb-4">Welcome to Health Management System</h1>
              <p className="text-lg text-gray-600">Manage patients and consultations efficiently.</p>
              <div className="mt-8 flex justify-center gap-4">
                <Link to="/patients" className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
                  Manage Patients
                </Link>
                <Link to="/consultations" className="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition">
                  View Consultations
                </Link>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </div>
  );
}

export default App;
