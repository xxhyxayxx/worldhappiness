import { getHealthData, getYears, deleteHealthData } from '../api/data';
import useDataList from '../hooks/useDataList';
import useDeleteData from '../hooks/useDeleteData';
import useFilteredDataList from '../hooks/useFilteredDataList';
import DataList from './common/DataList';
import CategoryDataList from './common/CategoryDataList';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';

const HealthDataList = () => {
    const {
        dataList: healthDataList,
        setDataList,
        years,
        selectedYear,
        setSelectedYear
    } = useDataList(getHealthData, getYears);

    const deleteData = useDeleteData();

    const handleDelete = async (healthDataId) => {
        await deleteData(deleteHealthData, healthDataId, (id) => {
            const updatedDataList = healthDataList.filter(data => data.id !== id);
            setDataList(updatedDataList);
        });
    };

    const filteredHealthData = useFilteredDataList(healthDataList, selectedYear, 'life_expectancy');

    const chartData = filteredHealthData.map(data => ({
        label: data.country_region.country,
        value: parseFloat(data.life_expectancy)
    }));

    const renderListItem = (data) => (
        <>
            <p>{data.country_region.country} - {data.country_region.region}</p>
            <p>{data.year.year}</p>
            <p>{data.life_expectancy}</p>
            <Link to={`/edit-health-data/${data.id}`} className={styles.editButton}>Edit</Link>
            <button onClick={() => handleDelete(data.id)} className={styles.deleteButton}>Delete</button>
        </>
    );

    return (
        <CategoryDataList
            title="Health Data"
            addButtonLink="/add-health-data"
            addButtonTitle="Add New Health Data"
            selectedYear={selectedYear}
            setSelectedYear={setSelectedYear}
            years={years}
            chartData={chartData}
            chartLabel={`Health in ${selectedYear}`}
            chartColor='rgba(0, 74, 223, 0.5)'
        >
            <DataList data={filteredHealthData} renderItem={renderListItem} />
        </CategoryDataList>
    );
};

export default HealthDataList;
