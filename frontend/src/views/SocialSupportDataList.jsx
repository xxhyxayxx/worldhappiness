import { getSocialSupportData, getYears, deleteSocialSupportData } from '../api/data';
import useDataList from '../hooks/useDataList';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';
import DataBarChart from './common/DataBarChart';
import useDeleteData from '../hooks/useDeleteData';
import useFilteredDataList from '../hooks/useFilteredDataList';
import DataList from './common/DataList';

const SocialSupportDataList = () => {
    const {
        dataList: socialSupportDataList,
        setDataList,
        years,
        selectedYear,
        setSelectedYear
    } = useDataList(getSocialSupportData, getYears);

    const deleteData = useDeleteData();

    const handleDelete = async (socialSupportDataId) => {
        await deleteData(deleteSocialSupportData, socialSupportDataId, (id) => {
            const updatedDataList = socialSupportDataList.filter(data => data.id !== id);
            setDataList(updatedDataList);
        });
    };

    const filteredSocialSupportData = useFilteredDataList(socialSupportDataList, selectedYear, 'social_support');

    const chartData = filteredSocialSupportData.map(data => ({
        label: data.country_region.country,
        value: parseFloat(data.social_support)
    }));

    const renderListItem = (data) => (
        <>
            <p>{data.country_region.country} - {data.country_region.region}</p>
            <p>{data.year.year}</p>
            <p>{data.social_support}</p>
            <Link to={`/edit-socialsupport-data/${data.id}`} className={styles.editButton}>Edit</Link>
            <button onClick={() => handleDelete(data.id)} className={styles.deleteButton}>Delete</button>
        </>
    );

    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Social Support Data</h1>
            <Link to="/add-socialsupport-data" className={styles.addDataButton}>Add New Social Support Data</Link>
            <div className={styles.barBox}>
                <select value={selectedYear} onChange={e => setSelectedYear(e.target.value)} className={styles.selectYear}>
                    {years.map(year => <option key={year} value={year}>{year}</option>)}
                </select>
                <div className={styles.chartContainer}>
                    <DataBarChart
                        data={chartData}
                        label={`Social Support in ${selectedYear}`}
                        backgroundColor='rgba(112, 0, 223, 0.5)'
                        width={1024}
                        height={320} />
                </div>
            </div>
            <DataList data={filteredSocialSupportData} renderItem={renderListItem} />
        </div>
    );
};

export default SocialSupportDataList;
