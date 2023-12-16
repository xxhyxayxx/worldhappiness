import { getHappinessScore, getYears, deleteHappinessScore } from '../api/data';
import useDataList from '../hooks/useDataList';
import useDeleteData from '../hooks/useDeleteData';
import useFilteredDataList from '../hooks/useFilteredDataList';
import DataList from './common/DataList';
import CategoryDataList from './common/CategoryDataList';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';

const HappinessScoreList = () => {
    const {
        dataList: happinessScoreList,
        setDataList,
        years,
        selectedYear,
        setSelectedYear
    } = useDataList(getHappinessScore, getYears);

    const deleteData = useDeleteData();

    const handleDelete = async (happinessScoreId) => {
        await deleteData(deleteHappinessScore, happinessScoreId, (id) => {
            const updatedDataList = happinessScoreList.filter(data => data.id !== id);
            setDataList(updatedDataList);
        });
    };

    const filteredHappinessScore = useFilteredDataList(happinessScoreList, selectedYear, 'happiness_score');

    const chartData = filteredHappinessScore.map(data => ({
        label: data.country_region.country,
        value: parseFloat(data.happiness_score)
    }));

    const renderListItem = (data) => (
        <>
            <p>{data.country_region.country} - {data.country_region.region}</p>
            <p>{data.year.year}</p>
            <p>{data.happiness_score}</p>
            <Link to={`/edit-happinessscore-data/${data.id}`} className={styles.editButton}>Edit</Link>
            <button onClick={() => handleDelete(data.id)} className={styles.deleteButton}>Delete</button>
        </>
    );

    return (
        <CategoryDataList
            title="Happiness Score"
            addButtonLink="/add-happinessscore-data"
            addButtonTitle="Add New Happiness Score"
            selectedYear={selectedYear}
            setSelectedYear={setSelectedYear}
            years={years}
            chartData={chartData}
            chartLabel={`Happiness Score in ${selectedYear}`}
            chartColor='rgba(255, 20, 147, 0.5)'
        >
            <DataList data={filteredHappinessScore} renderItem={renderListItem} />
        </CategoryDataList>
    );
};

export default HappinessScoreList;
