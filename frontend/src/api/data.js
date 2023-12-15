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

export const getYears = async () => {
    const axios = useAxios();
    const response = await axios.get('years/');
    return response.data;
};

export const getCountryRegions = async () => {
    const axios = useAxios();
    const response = await axios.get('countryregions/');
    return response.data;
};

/* Economic Data */
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

export const getEconomicDataById = async (economicDataId) => {
    const axios = useAxios();
    const response = await axios.get(`economicdata/${economicDataId}/`);
    return response.data;
};

/* Social Support Data */
export const getSocialSupportData = async () => {
    const axios = useAxios();
    const response = await axios.get('socialsupportdata/');
    return response.data;
};

export const addSocialSupportData = async (socialSupportData) => {
    const axios = useAxios();
    const response = await axios.post('socialsupportdata/', socialSupportData);
    return response.data;
};

export const updateSocialSupportData = async (socialSupportDataId, socialSupportData) => {
    const axios = useAxios();
    const response = await axios.put(`socialsupportdata/${socialSupportDataId}/`, socialSupportData);
    return response.data;
};

export const deleteSocialSupportData = async (socialSupportDataId) => {
    const axios = useAxios();
    await axios.delete(`socialsupportdata/${socialSupportDataId}/`);
};

export const getSocialSupportDataById = async (socialSupportDataId) => {
    const axios = useAxios();
    const response = await axios.get(`socialsupportdata/${socialSupportDataId}/`);
    return response.data;
};

/* Health Data */
export const getHealthData = async () => {
    const axios = useAxios();
    const response = await axios.get('healthdata/');
    return response.data;
};

export const addHealthData = async (healthData) => {
    const axios = useAxios();
    const response = await axios.post('healthdata/', healthData);
    return response.data;
};

export const updateHealthData = async (healthDataId, healthData) => {
    const axios = useAxios();
    const response = await axios.put(`healthdata/${healthDataId}/`, healthData);
    return response.data;
};

export const deleteHealthData = async (healthDataId) => {
    const axios = useAxios();
    await axios.delete(`healthdata/${healthDataId}/`);
};

export const getHealthDataById = async (healthDataId) => {
    const axios = useAxios();
    const response = await axios.get(`healthdata/${healthDataId}/`);
    return response.data;
};

/* Happiness Score */
export const getHappinessScore = async () => {
    const axios = useAxios();
    const response = await axios.get('happinessscore/');
    return response.data;
};

export const addHappinessScore = async (happinessScore) => {
    const axios = useAxios();
    const response = await axios.post('happinessscore/', happinessScore);
    return response.data;
};

export const updateHappinessScore = async (happinessScoreId, happinessScore) => {
    const axios = useAxios();
    const response = await axios.put(`happinessscore/${happinessScoreId}/`, happinessScore);
    return response.data;
};

export const deleteHappinessScore = async (happinessScoreId) => {
    const axios = useAxios();
    await axios.delete(`happinessscore/${happinessScoreId}/`);
};

export const getHappinessScoreById = async (happinessScoreId) => {
    const axios = useAxios();
    const response = await axios.get(`happinessscore/${happinessScoreId}/`);
    return response.data;
};