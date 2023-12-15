import React from 'react';
import styles from '../../styles/Data.module.css';
import { Link } from 'react-router-dom';
import DataBarChart from './DataBarChart';

const CategoryDataList = ({
    title,
    addButtonLink,
    addButtonTitle,
    selectedYear,
    setSelectedYear,
    years,
    chartData,
    chartLabel,
    chartColor,
    children // これはリストアイテムをレンダリングするために使用されます
}) => {
    return (
        <div className={styles.dataBox}>
            <h1 className={styles.dataTitle}>{title}</h1>
            <Link to={addButtonLink} className={styles.addDataButton}>{addButtonTitle}</Link>
            <div className={styles.barBox}>
                <select value={selectedYear} onChange={e => setSelectedYear(e.target.value)} className={styles.selectYear}>
                    {years.map(year => <option key={year} value={year}>{year}</option>)}
                </select>
                <div className={styles.chartContainer}>
                    <DataBarChart
                        data={chartData}
                        label={chartLabel}
                        backgroundColor={chartColor}
                        width={1024}
                        height={320} />
                </div>
            </div>
            {children}
        </div>
    );
};

export default CategoryDataList;
