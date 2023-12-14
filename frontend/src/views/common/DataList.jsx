// DataList.jsx
import React from 'react';
import styles from '../../styles/Data.module.css';

const DataList = ({ data, renderItem }) => {
    return (
        <ul className={styles.dataList}>
            {data.map(item => (
                <li key={item.id} className={styles.listItem}>
                    {renderItem(item)}
                </li>
            ))}
        </ul>
    );
};

export default DataList;
