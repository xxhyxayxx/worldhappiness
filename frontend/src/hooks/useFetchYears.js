import { useState, useEffect } from 'react';
import { getYears } from '../api/data';

const useFetchYears = () => {
  const [years, setYears] = useState([]);
  const [selectedYearId, setSelectedYearId] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getYears();
        setYears(data);
        if (data.length > 0) {
          setSelectedYearId(data[0].id);
        }
      } catch (error) {
        console.error('Error fetching years:', error);
      }
    };
    fetchData();
  }, []);

  return { years, selectedYearId, setSelectedYearId };
};

export default useFetchYears;
