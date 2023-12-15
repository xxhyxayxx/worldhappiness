import { useState, useEffect } from 'react';
import { getRegions } from '../api/data';

const useFetchRegions = () => {
  const [regions, setRegions] = useState([]);
  const [selectedRegionId, setSelectedRegionId] = useState('');

  useEffect(() => {
    const fetchRegions = async () => {
      try {
        const fetchedRegions = await getRegions();
        setRegions(fetchedRegions);
        if (fetchedRegions.length > 0) {
          setSelectedRegionId(fetchedRegions[0].id);
        }
      } catch (error) {
        console.error('Error fetching regions:', error);
      }
    };
    fetchRegions();
  }, []);

  return { regions, selectedRegionId, setSelectedRegionId };
};

export default useFetchRegions;
