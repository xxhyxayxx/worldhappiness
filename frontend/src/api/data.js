import useAxios from '../utils/useAxios';

export const getCountries = async () => {
  const axios = useAxios();
  const response = await axios.get('countries/');
  return response.data;
};

export const getRegions = async () => {
  const axios = useAxios();
  const response = await axios.get('regions/');
  return response.data;
};

export const addCountry = async (countryData) => {
    const axios = useAxios();
    const response = await axios.post('countries/', countryData);
    return response.data;
};

export const updateCountry = async (countryId, countryData) => {
    const axios = useAxios();
    const response = await axios.put(`countries/${countryId}/`, countryData);
    return response.data;
};

export const deleteCountry = async (countryId) => {
    const axios = useAxios();
    await axios.delete(`countries/${countryId}/`);
};

export const getCountryById = async (countryId) => {
    const axios = useAxios();
    const response = await axios.get(`countries/${countryId}/`);
    return response.data;
  };
  