import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/patients/';

export const fetchPatients = createAsyncThunk('patients/fetchPatients', async () => {
    const response = await axios.get(BASE_URL);
    return response.data;
});

export const addPatient = createAsyncThunk('patients/addPatient', async (newPatient) => {
    const response = await axios.post(BASE_URL, newPatient);
    return response.data;
});

const patientsSlice = createSlice({
    name: 'patients',
    initialState: {
        items: [],
        status: 'idle',
        error: null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchPatients.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchPatients.fulfilled, (state, action) => {
                state.status = 'succeeded';
                state.items = action.payload;
            })
            .addCase(fetchPatients.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            })
            .addCase(addPatient.fulfilled, (state, action) => {
                state.items.push(action.payload);
            });
    }
});

export default patientsSlice.reducer;
