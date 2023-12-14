// DataBarChart.jsx
import React from 'react';
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

const DataBarChart = ({ data, label, backgroundColor, width, height }) => {
    const chartData = {
        labels: data.map(item => item.label),
        datasets: [{
            label: label,
            data: data.map(item => item.value),
            backgroundColor: backgroundColor,
        }]
    };

    const options = {
        maintainAspectRatio: false,
        responsive: false
    };

    return <Bar data={chartData} options={options} width={width} height={height}  />;
};

export default DataBarChart;
