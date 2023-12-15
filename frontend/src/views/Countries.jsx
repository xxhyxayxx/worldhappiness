import { getCountries, deleteCountry } from '../api/data';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';
import useDataList from '../hooks/useDataList'; // Assuming similar to useDataList in EconomicDataList
import useDeleteData from '../hooks/useDeleteData'; // Reusing or creating similar hook
import DataList from './common/DataList'; // Reusing or creating a common DataList component

const Countries = () => {
    const { dataList: countries, setDataList } = useDataList(getCountries);

    const deleteData = useDeleteData();

    const handleDelete = async (countryId) => {
        await deleteData(deleteCountry, countryId, (id) => {
            const updatedCountries = countries.filter(country => country.id !== id);
            setDataList(updatedCountries);
        });
    };

    const renderListItem = (country) => (
        <>
            <p className={styles.dataName}>{country.name}</p>
            <Link to={`/edit-country/${country.id}`} className={styles.editButton}>Edit</Link>
            <button onClick={() => handleDelete(country.id)} className={styles.deleteButton}>Delete</button>
        </>
    );

    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Countries</h1>
            <Link to="/add-country" className={styles.addDataButton}>Add New Country</Link>
            <DataList data={countries} renderItem={renderListItem} />
        </div>
    );
};

export default Countries;
