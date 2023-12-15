// useDataList.js
import { useState, useEffect } from 'react';

const useDataList = (getDataFunc, getYearsFunc = () => Promise.resolve([])) => {
  const [dataList, setDataList] = useState([]);
  const [years, setYears] = useState([]);
  const [selectedYear, setSelectedYear] = useState('');
  const [isDataFetched, setIsDataFetched] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getDataFunc();
      const yearsData = await getYearsFunc();

      setDataList(data);
      const sortedYears = yearsData.map(y => y.year).sort((a, b) => b - a);
      setYears(sortedYears);
      setSelectedYear(sortedYears[0]?.toString());
    };
    
    if (!isDataFetched) {
      fetchData();
      setIsDataFetched(true);
    }
  }, [isDataFetched]);

  return { dataList, setDataList, years, selectedYear, setSelectedYear };
};

export default useDataList;
