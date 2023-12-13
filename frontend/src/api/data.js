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

export const getEconomicData = async () => {
    const axios = useAxios();
    const response = await axios.get('economicdata/');
    return response.data;
};

export const addEconomicData = async (economicData) => {
  const axios = useAxios();
  const response = await axios.post('economicdata/', economicData);
  return response.data;
};

export const updateEconomicData = async (economicDataId, economicData) => {
  const axios = useAxios();
  const response = await axios.put(`economicdata/${economicDataId}/`, economicData);
  return response.data;
};

export const deleteEconomicData = async (economicDataId) => {
  const axios = useAxios();
  await axios.delete(`economicdata/${economicDataId}/`);
};

export const getCountryRegions = async () => {
  const axios = useAxios();
  const response = await axios.get('countryregions/');
  return response.data;
};

export const getYears = async () => {
    const axios = useAxios();
    const response = await axios.get('years/');
    return response.data;
};

export const getEconomicDataById = async (economicDataId) => {
    const axios = useAxios();
    const response = await axios.get(`economicdata/${economicDataId}/`);
    return response.data;
};
