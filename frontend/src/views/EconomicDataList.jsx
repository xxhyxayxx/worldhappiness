import { useEffect, useState, useMemo } from 'react';
import { getEconomicData, getYears, deleteEconomicData } from '../api/data';
import { Link } from 'react-router-dom';
import styles from '../styles/EconomicDataList.module.css';
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

    return (
        <div className={styles.box}>
            <h1>Economic Data</h1>
            <Link to="/add-economic-data">Add New Economic Data</Link>
            <select value={selectedYear} onChange={e => setSelectedYear(e.target.value)}>
                {years.map(year => <option key={year} value={year}>{year}</option>)}
            </select>
            <div className={styles.chartContainer}>
                <Bar options={{ responsive: true }} data={chartData} />
            </div>
            <ul>
                {filteredEconomicData.map(data => (
                    <li key={data.id}>
                        {data.country_region.country} - {data.country_region.region}:
                        Year {data.year.year}, GDP {data.gdp}
                        <Link to={`/edit-economic-data/${data.id}`}>Edit</Link>
                        <button onClick={() => handleDelete(data.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EconomicDataList;
