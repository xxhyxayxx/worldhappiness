import { useEffect, useState, useMemo } from 'react';
import { getSocialSupportData, getYears, deleteSocialSupportData } from '../api/data';
import { Link } from 'react-router-dom';
import styles from '../styles/Data.module.css';
import { Bar } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

const SocialSupportDataList = () => {
    const [allSocialSupportData, setAllSocialSupportData] = useState([]);
    const [years, setYears] = useState([]);
    const [selectedYear, setSelectedYear] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const [socialSupportData, yearsData] = await Promise.all([getSocialSupportData(), getYears()]);
            console.log(socialSupportData);
            setAllSocialSupportData(socialSupportData);
            const sortedYears = yearsData.map(y => y.year).sort((a, b) => b - a);
            setYears(sortedYears);
            setSelectedYear(sortedYears[0]?.toString());
        };
        fetchData();
    }, []);

    const handleDelete = async (socialSupportDataId) => {
        if (window.confirm('Are you sure you want to delete this economic data?')) {
            await deleteEconomicData(socialSupportId);
            setAllEconomicData(allsocialSupportData.filter(data => data.id !== socialSupportDataId));
        }
    };

    const filteredSocialSupportData = useMemo(() => {
        const yearData = allSocialSupportData.filter(data => data.year.year.toString() === selectedYear);
        return yearData.sort((a, b) => parseFloat(b.social_support) - parseFloat(a.social_support));
    }, [allSocialSupportData, selectedYear]);

    const chartData = useMemo(() => ({
        labels: filteredSocialSupportData.map(data => data.country_region.country),
        datasets: [{
            label: `Social Support in ${selectedYear}`,
            data: filteredSocialSupportData.map(data => parseFloat(data.social_support)),
            backgroundColor: 'rgba(112, 0, 223, 0.5)',
        }],
    }), [filteredSocialSupportData, selectedYear]);

    const options = {
        maintainAspectRatio: false,
        responsive: false,
    };

    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Social Support Data</h1>
            <Link to="/add-economic-data" className={styles.addData}>Add New Social Support Data</Link>
            <div className={styles.barBox}>
                <select value={selectedYear} onChange={e => setSelectedYear(e.target.value)} className={styles.selectYear}>
                    {years.map(year => <option key={year} value={year}>{year}</option>)}
                </select>
                <div className={styles.chartContainer}>
                    <Bar data={chartData} options={options} width={1024} height={320}/>
                </div>
            </div>
            <ul className={styles.dataList}>
                <li className={styles.listItem}>
                    <p>Country - Region</p>
                    <p>Year</p>
                    <p>Social Support</p>
                    <p>Edit</p>
                    <p>Delete</p>
                </li>
                {filteredSocialSupportData.map(data => (
                    <li key={data.id} className={styles.listItem}>
                        <p>{data.country_region.country} - {data.country_region.region}</p>
                        <p>{data.year.year}</p> <p>{data.social_support}</p>
                        <Link to={`/edit-socialsupport-data/${data.id}`}className={styles.editButton}>Edit</Link>
                        <button onClick={() => handleDelete(data.id)}className={styles.deleteButton}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SocialSupportDataList;
