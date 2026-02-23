import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchPatients, addPatient } from '../features/patients/patientsSlice';

const Patients = () => {
    const dispatch = useDispatch();
    const patients = useSelector((state) => state.patients.items);
    const status = useSelector((state) => state.patients.status);
    const error = useSelector((state) => state.patients.error);

    const [formData, setFormData] = useState({
        full_name: '',
        date_of_birth: '',
        email: ''
    });

    useEffect(() => {
        if (status === 'idle') {
            dispatch(fetchPatients());
        }
    }, [status, dispatch]);

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch(addPatient(formData));
        setFormData({ full_name: '', date_of_birth: '', email: '' });
    };

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold mb-4">Patients</h2>
            
            <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded shadow">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Full Name</label>
                        <input
                            type="text"
                            value={formData.full_name}
                            onChange={(e) => setFormData({...formData, full_name: e.target.value})}
                            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-2 border"
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Date of Birth</label>
                        <input
                            type="date"
                            value={formData.date_of_birth}
                            onChange={(e) => setFormData({...formData, date_of_birth: e.target.value})}
                            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-2 border"
                            required
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700">Email</label>
                        <input
                            type="email"
                            value={formData.email}
                            onChange={(e) => setFormData({...formData, email: e.target.value})}
                            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-2 border"
                            required
                        />
                    </div>
                </div>
                <button type="submit" className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
                    Add Patient
                </button>
            </form>

            {status === 'loading' && <p>Loading...</p>}
            {status === 'failed' && <p className="text-red-500">{error}</p>}
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {patients.map((patient) => (
                    <div key={patient.id} className="bg-white p-4 rounded shadow border">
                        <h3 className="font-bold text-lg">{patient.full_name}</h3>
                        <p className="text-gray-600">Email: {patient.email}</p>
                        <p className="text-gray-600">DOB: {patient.date_of_birth}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Patients;
