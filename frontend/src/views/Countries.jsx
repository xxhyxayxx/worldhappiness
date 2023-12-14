import { useEffect, useState } from 'react';
import { getCountries, deleteCountry } from '../api/data';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';

const Countries = () => {
    const [countries, setCountries] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            let data = await getCountries();
            // 国名でソート
            data.sort((a, b) => a.name.localeCompare(b.name));
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
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Countries</h1>
            <Link to="/add-country" className={styles.addData}>Add New Country</Link>
            <ul className={styles.coutryDataList}>
                {countries.map(country => (
                    <li key={country.id} className={styles.countryListItem}>
                        <p className={styles.dataName}>{country.name}</p>
                        <Link to={`/edit-country/${country.id}`} className={styles.editButton}>Edit</Link>
                        <button onClick={() => handleDelete(country.id)} className={styles.deleteButton}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Countries;