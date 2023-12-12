import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCountryById, updateCountry, getRegions } from '../api/data';

const EditCountryForm = () => {
  const [name, setName] = useState('');
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState('');
  const { countryId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCountryAndRegions = async () => {
      try {
        const countryData = await getCountryById(countryId);
        setName(countryData.name);
        setSelectedRegion(countryData.region);

        const regionsData = await getRegions();
        setRegions(regionsData);
      } catch (error) {
        // エラー処理
      }
    };
    fetchCountryAndRegions();
  }, [countryId]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await updateCountry(countryId, { name, region: selectedRegion });
      navigate('/countries');
    } catch (error) {
      // エラー処理
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Country name"
      />
      <select
        value={selectedRegion}
        onChange={(e) => setSelectedRegion(e.target.value)}
      >
        {regions.map((region) => (
          <option key={region.id} value={region.id}>
            {region.name}
          </option>
        ))}
      </select>
      <button type="submit">Update Country</button>
    </form>
  );
};

export default EditCountryForm;
