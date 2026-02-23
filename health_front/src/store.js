import { configureStore } from '@reduxjs/toolkit';
import patientsReducer from './features/patients/patientsSlice';
import consultationsReducer from './features/consultations/consultationsSlice';

export const store = configureStore({
  reducer: {
    patients: patientsReducer,
    consultations: consultationsReducer,
  },
});
