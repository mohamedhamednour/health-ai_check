import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/consultations/';

export const fetchConsultations = createAsyncThunk('consultations/fetchConsultations', async () => {
    const response = await axios.get(BASE_URL);
    return response.data;
});

export const fetchConsultationById = createAsyncThunk('consultations/fetchConsultationById', async (id) => {
    const response = await axios.get(`${BASE_URL}${id}/`);
    return response.data;
});

export const addConsultation = createAsyncThunk('consultations/addConsultation', async (newConsultation) => {
    const response = await axios.post(BASE_URL, newConsultation);
    return response.data;
});

export const generateSummary = createAsyncThunk('consultations/generateSummary', async (id) => {
    const response = await axios.post(`${BASE_URL}${id}/generate_summary/`);
    return response.data;
});

const consultationsSlice = createSlice({
    name: 'consultations',
    initialState: {
        items: [],
        status: 'idle',
        error: null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchConsultations.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchConsultations.fulfilled, (state, action) => {
                state.status = 'succeeded';
                state.items = action.payload;
            })
            .addCase(fetchConsultations.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            })
            .addCase(fetchConsultationById.fulfilled, (state, action) => {
                const index = state.items.findIndex(item => item.id === action.payload.id);
                if (index !== -1) {
                    state.items[index] = action.payload;
                } else {
                    state.items.push(action.payload);
                }
            })
            .addCase(addConsultation.fulfilled, (state, action) => {
                state.items.push(action.payload);
            });
    }
});

export default consultationsSlice.reducer;
