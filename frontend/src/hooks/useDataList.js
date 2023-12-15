import { useState, useEffect } from 'react';

const useDataList = (getDataFunc, getYearsFunc = null) => { // getYearsFunc をオプショナルにする
    const [dataList, setDataList] = useState([]);
    const [years, setYears] = useState([]);
    const [selectedYear, setSelectedYear] = useState('');

    const updateDataList = (newDataList) => {
        setDataList(newDataList);
    };

    useEffect(() => {
        const fetchData = async () => {
            const data = await getDataFunc();
            setDataList(data);

            if (getYearsFunc) { // getYearsFunc が提供されている場合のみ年のデータを取得
                const yearsData = await getYearsFunc();
                const sortedYears = yearsData.map(y => y.year).sort((a, b) => b - a);
                setYears(sortedYears);
                setSelectedYear(sortedYears[0]?.toString());
            }
        };
        fetchData();
    }, [getDataFunc, getYearsFunc]);

    return { dataList, setDataList: updateDataList, years, selectedYear, setSelectedYear };
};

export default useDataList;
