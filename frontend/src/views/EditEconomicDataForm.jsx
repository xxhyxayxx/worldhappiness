import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getEconomicDataById, updateEconomicData, getCountryRegions, getYears } from '../api/data';

const EditEconomicDataForm = () => {
  const [countryRegion, setCountryRegion] = useState('');
  const [year, setYear] = useState('');
  const [gdp, setGdp] = useState('');
  const [countryRegions, setCountryRegions] = useState([]);
  const [years, setYears] = useState([]);
  const { economicDataId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchEconomicDataAndOptions = async () => {
      try {
        const economicData = await getEconomicDataById(economicDataId);
        setCountryRegion(economicData.country_region);
        setYear(economicData.year);
        setGdp(economicData.gdp);

        const regionsData = await getCountryRegions();
        setCountryRegions(regionsData);

        const yearsData = await getYears();
        setYears(yearsData);
      } catch (error) {
        // エラー処理
      }
    };
    fetchEconomicDataAndOptions();
  }, [economicDataId]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await updateEconomicData(economicDataId, { country_region: countryRegion, year, gdp });
      navigate('/economic-data');
    } catch (error) {
      // エラー処理
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* CountryRegion のセレクトボックス */}
      <select
        value={countryRegion}
        onChange={(e) => setCountryRegion(e.target.value)}
      >
        {countryRegions.map((cr) => (
          <option key={cr.id} value={cr.id}>
            {cr.country} - {cr.region}
          </option>
        ))}
      </select>

      {/* Year のセレクトボックス */}
      <select
        value={year}
        onChange={(e) => setYear(e.target.value)}
      >
        {years.map(year => (
          <option key={year} value={year}>
            {year}
          </option>
        ))}
      </select>

      {/* GDP の入力 */}
      <input
        type="number"
        value={gdp}
        onChange={(e) => setGdp(e.target.value)}
        placeholder="GDP"
      />

      <button type="submit">Update Economic Data</button>
    </form>
  );
};

export default EditEconomicDataForm;
