import { useEffect, useState, useMemo } from 'react';
import { getEconomicData, getYears, deleteEconomicData } from '../api/data';
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

const EconomicDataList = () => {
    const [allEconomicData, setAllEconomicData] = useState([]);
    const [years, setYears] = useState([]);
    const [selectedYear, setSelectedYear] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const [economicData, yearsData] = await Promise.all([getEconomicData(), getYears()]);
            setAllEconomicData(economicData);
            const sortedYears = yearsData.map(y => y.year).sort((a, b) => b - a);
            setYears(sortedYears);
            setSelectedYear(sortedYears[0]?.toString());
        };
        fetchData();
    }, []);

    const handleDelete = async (economicDataId) => {
        if (window.confirm('Are you sure you want to delete this economic data?')) {
            await deleteEconomicData(economicDataId);
            setAllEconomicData(allEconomicData.filter(data => data.id !== economicDataId));
        }
    };

    const filteredEconomicData = useMemo(() => {
        const yearData = allEconomicData.filter(data => data.year.year.toString() === selectedYear);
        return yearData.sort((a, b) => parseFloat(b.gdp) - parseFloat(a.gdp));
    }, [allEconomicData, selectedYear]);

    const chartData = useMemo(() => ({
        labels: filteredEconomicData.map(data => data.country_region.country),
        datasets: [{
            label: `GDP in ${selectedYear}`,
            data: filteredEconomicData.map(data => parseFloat(data.gdp)),
            backgroundColor: 'rgba(53, 162, 235, 0.5)',
        }],
    }), [filteredEconomicData, selectedYear]);

    const options = {
        maintainAspectRatio: false,
        responsive: false, // ここで responsive を false に設定
    };

    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>Economic Data</h1>
            <Link to="/add-economic-data" className={styles.addData}>Add New Economic Data</Link>
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
                    <p>GDP</p>
                    <p>Edit</p>
                    <p>Delete</p>
                </li>
                {filteredEconomicData.map(data => (
                    <li key={data.id} className={styles.listItem}>
                        <p>{data.country_region.country} - {data.country_region.region}</p>
                        <p>{data.year.year}</p> <p>{data.gdp}</p>
                        <Link to={`/edit-economic-data/${data.id}`}className={styles.editButton}>Edit</Link>
                        <button onClick={() => handleDelete(data.id)}className={styles.deleteButton}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EconomicDataList;
