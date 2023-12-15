import { useState, useEffect } from 'react';
import { getCountryRegions } from '../api/data';

const useFetchCountryRegions = () => {
  const [countryRegions, setCountryRegions] = useState([]);
  const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getCountryRegions();
        setCountryRegions(data);
        if (data.length > 0) {
          setSelectedCountryRegionId(data[0].id);
        }
      } catch (error) {
        console.error('Error fetching country regions:', error);
      }
    };
    fetchData();
  }, []);

  return { countryRegions, selectedCountryRegionId, setSelectedCountryRegionId };
};

export default useFetchCountryRegions;
