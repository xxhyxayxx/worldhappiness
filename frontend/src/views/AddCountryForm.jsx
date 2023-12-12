import { useEffect, useState } from 'react';
import { addCountry, getRegions } from '../api/data';
import { useNavigate } from 'react-router-dom';

const AddCountryForm = () => {
  const [name, setName] = useState('');
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    // Region のデータを取得
    const fetchRegions = async () => {
      const data = await getRegions();
      setRegions(data);
    };
    fetchRegions();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await addCountry({ name, region: selectedRegion });
      navigate('/countries');
      // 成功した場合の処理
    } catch (error) {
      // エラー処理
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* 国名の入力フィールド */}
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Country name"
      />
      {/* Region の選択 */}
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
      <button type="submit">Add Country</button>
    </form>
  );
};

export default AddCountryForm;