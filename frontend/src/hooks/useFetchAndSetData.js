import { useState, useEffect } from 'react';

// dataFetcher はデータを取得する関数、extractData は取得したデータから必要な情報を抽出する関数
const useFetchAndSetData = (dataFetcher, extractData) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await dataFetcher();
        setData(extractData(result));
      } catch (error) {
        setError(error);
      }
    };
    fetchData();
  }, [dataFetcher, extractData]);

  return [data, error];
};

export default useFetchAndSetData;
