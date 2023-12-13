import { useEffect, useState } from 'react';
import { getEconomicData, deleteEconomicData } from '../api/data';
import { Link } from 'react-router-dom';

const EconomicDataList = () => {
  const [economicDataList, setEconomicDataList] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getEconomicData();
      setEconomicDataList(data);
    };
    fetchData();
  }, []);

  const handleDelete = async (economicDataId) => {
    if (window.confirm('Are you sure you want to delete this economic data?')) {
      try {
        await deleteEconomicData(economicDataId);
        const updatedData = await getEconomicData();
        setEconomicDataList(updatedData);
      } catch (error) {
        // エラー処理
      }
    }
  };

  return (
    <div>
      <h1>Economic Data</h1>
      <Link to="/add-economic-data">Add New Economic Data</Link>
      <ul>
        {economicDataList.map(data => (
          <li key={data.id}>
            {data.country_region.country} - {data.country_region.region}: Year {data.year.year}, GDP {data.gdp}
            <Link to={`/edit-economic-data/${data.id}`}>Edit</Link>
            <button onClick={() => handleDelete(data.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EconomicDataList;
