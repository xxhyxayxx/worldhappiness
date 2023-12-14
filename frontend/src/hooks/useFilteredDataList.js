// useFilteredDataList.js
import { useMemo } from 'react';

const useFilteredDataList = (dataList, selectedYear, sortKey) => {
    const filteredDataList = useMemo(() => {
        const yearData = dataList.filter(data => data.year.year.toString() === selectedYear);
        return yearData.sort((a, b) => parseFloat(b[sortKey]) - parseFloat(a[sortKey]));
    }, [dataList, selectedYear, sortKey]);

    return filteredDataList;
};

export default useFilteredDataList;
