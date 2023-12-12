import { useEffect, useState } from 'react';
import { getCountries, deleteCountry } from '../api/data';
import { Link } from 'react-router-dom';

const Countries = () => {
  const [countries, setCountries] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getCountries();
      setCountries(data);
    };
    fetchData();
  }, []);

  const handleDelete = async (countryId) => {
    // ユーザーに削除確認を求める
    if (window.confirm('Are you sure you want to delete this country?')) {
      try {
        await deleteCountry(countryId);
        // 削除後、国のリストを再取得して更新
        const data = await getCountries();
        setCountries(data);
      } catch (error) {
        // エラー処理
      }
    }
  };

  return (
    <div>
      <h1>Countries</h1>
      <Link to="/add-country">Add New Country</Link>
      <ul>
        {countries.map(country => (
          <li key={country.id}>
            {country.name}
            <Link to={`/edit-country/${country.id}`}>Edit</Link>
            <button onClick={() => handleDelete(country.id)}>Delete</button>
        </li>
        ))}
      </ul>
    </div>
  );
};

export default Countries;