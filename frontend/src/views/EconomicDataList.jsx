import { getEconomicData, getYears, deleteEconomicData } from '../api/data';
import useDataList from '../hooks/useDataList';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';
import DataBarChart from './common/DataBarChart';
import useDeleteData from '../hooks/useDeleteData';
import useFilteredDataList from '../hooks/useFilteredDataList';
import DataList from './common/DataList';

const EconomicDataList = () => {
    const {
        dataList: economicDataList,
        setDataList,
        years,
        selectedYear,
        setSelectedYear
    } = useDataList(getEconomicData, getYears);

    const deleteData = useDeleteData();

    const handleDelete = async (economicDataId) => {
        await deleteData(deleteEconomicData, economicDataId, (id) => {
            const updatedDataList = economicDataList.filter(data => data.id !== id);
            setDataList(updatedDataList);
        });
    };

    const filteredEconomicData = useFilteredDataList(economicDataList, selectedYear, 'gdp');

    const chartData = filteredEconomicData.map(data => ({
        label: data.country_region.country,
        value: parseFloat(data.gdp)
    }));

    const renderListItem = (data) => (
        <>
            <p>{data.country_region.country} - {data.country_region.region}</p>
            <p>{data.year.year}</p>
            <p>{data.gdp}</p>
            <Link to={`/edit-economic-data/${data.id}`} className={styles.editButton}>Edit</Link>
            <button onClick={() => handleDelete(data.id)} className={styles.deleteButton}>Delete</button>
        </>
    );

    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Economic Data</h1>
            <Link to="/add-economic-data" className={styles.addDataButton}>Add New Economic Data</Link>
            <div className={styles.barBox}>
                <select value={selectedYear} onChange={e => setSelectedYear(e.target.value)} className={styles.selectYear}>
                    {years.map(year => <option key={year} value={year}>{year}</option>)}
                </select>
                <div className={styles.chartContainer}>
                    <DataBarChart
                        data={chartData}
                        label={`GDP in ${selectedYear}`}
                        backgroundColor='rgba(0, 223, 0, 0.5)'
                        width={1024}
                        height={320} />
                </div>
            </div>
            <DataList data={filteredEconomicData} renderItem={renderListItem} />
        </div>
    );
};

export default EconomicDataList;
