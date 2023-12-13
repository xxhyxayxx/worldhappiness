import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getEconomicDataById, updateEconomicData, getCountryRegions, getYears } from '../api/data';

const EditEconomicDataForm = () => {
  // ステート変数の初期値として ID を使用
  const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
  const [selectedYearId, setSelectedYearId] = useState('');
  const [gdp, setGdp] = useState('');
  const [countryRegions, setCountryRegions] = useState([]);
  const [years, setYears] = useState([]);
  const { economicDataId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchEconomicDataAndOptions = async () => {
      try {
        const economicData = await getEconomicDataById(economicDataId);
        // 経済データのロード時に ID を使用
        setSelectedCountryRegionId(economicData.country_region.id);
        setSelectedYearId(economicData.year.id);
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
      // 更新時に ID を使用
      await updateEconomicData(economicDataId, {
        country_region_id: selectedCountryRegionId,
        year_id: selectedYearId,
        gdp
      });
      navigate('/economic-data');
    } catch (error) {
      // エラー処理
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* CountryRegion のセレクトボックス */}
      <select
        value={selectedCountryRegionId}
        onChange={(e) => setSelectedCountryRegionId(e.target.value)}
      >
        {countryRegions.map((cr) => (
          <option key={cr.id} value={cr.id}>
            {cr.country} - {cr.region}
          </option>
        ))}
      </select>

      {/* Year のセレクトボックス */}
      <select
        value={selectedYearId}
        onChange={(e) => setSelectedYearId(e.target.value)}
      >
        {years.map((y) => (
          <option key={y.id} value={y.id}>
            {y.year}
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
