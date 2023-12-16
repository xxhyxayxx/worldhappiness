import { create } from 'zustand';
import { getCountryRegions, getYears } from '../api/data';

const useGlobalDataStore = create((set) => ({
  countryRegions: [],
  years: [],
  fetchCountryRegions: async () => {
    try {
      const data = await getCountryRegions();
      set({ countryRegions: data });
    } catch (error) {
      console.error('Failed to fetch country regions:', error);
    }
  },
  fetchYears: async () => {
    try {
      const data = await getYears();
      set({ years: data });
    } catch (error) {
      console.error('Failed to fetch years:', error);
    }
  },
}));

export { useGlobalDataStore };
