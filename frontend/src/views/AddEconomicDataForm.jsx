import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { addEconomicData, getCountryRegions, getYears } from '../api/data';
import styles from '../styles/Data.module.css';

const AddEconomicDataForm = () => {
    const [gdp, setGdp] = useState('');
    const [countryRegions, setCountryRegions] = useState([]);
    const [years, setYears] = useState([]);
    const navigate = useNavigate();
    // 選択された CountryRegion の ID を保持するための State
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    // 選択された Year の ID を保持するための State
    const [selectedYearId, setSelectedYearId] = useState('');
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const countryRegionsData = await getCountryRegions();
            const yearsData = await getYears();

            if (countryRegionsData.length > 0) {
                setSelectedCountryRegionId(countryRegionsData[0].id); // 最初の要素のIDを初期値に設定
            }
            if (yearsData.length > 0) {
                setSelectedYearId(yearsData[0].id); // 最初の要素のIDを初期値に設定
            }

            setCountryRegions(countryRegionsData);
            setYears(yearsData);
        };
        fetchData();
    }, []);

    const validateInput = () => {
        // 全てのフィールドが入力されているか確認
        if (!selectedCountryRegionId || !selectedYearId || !gdp) {
            setError('All fields must be filled.');
            return false;
        }
        // gdp の入力値が適切な形式であるか確認
        const regex = /^\d{0,7}(\.\d{0,3})?$/;
        if (!regex.test(gdp)) {
            setError('GDP must be a number with up to 10 digits and 3 decimal places.');
            return false;
        }
        // 他のバリデーションロジックが必要な場合はここに追加
        setError('');
        return true;
    };

    // onChangeハンドラー
    const handleCountryRegionChange = (e) => {
        setSelectedCountryRegionId(e.target.value); // 選択されたIDをステートにセット
    };

    const handleYearChange = (e) => {
        setSelectedYearId(e.target.value); // 選択されたIDをステートにセット
    };


    const handleSubmit = async (event) => {
        event.preventDefault();
        const isValid = validateInput();
        if (!isValid) {
            return; // バリデーションが失敗した場合はここで処理を止める
        }
        const payload = {
            country_region_id: selectedCountryRegionId, // 正しいステートを使用
            year_id: selectedYearId,                    // 正しいステートを使用
            gdp: gdp
        };
        console.log('Sending payload:', payload);
        try {
            const response = await addEconomicData(payload);
            console.log('Response:', response);
            navigate('/economic-data');
        } catch (error) {
            console.error('Error submitting data:', error);
        }
    };



    return (
        <div className={styles.addBox}>
            <h1 className={styles.dataTitle}>Add Economic Data</h1>
            {error && <p className={styles.error}>{error}</p>}
            <form onSubmit={handleSubmit} className={styles.addData}>
                <select value={selectedCountryRegionId} onChange={handleCountryRegionChange} className={styles.selectBox}>
                    {countryRegions.map((cr) => (
                        <option key={cr.id} value={cr.id}>{cr.country} - {cr.region}</option>
                    ))}
                </select>
                <select value={selectedYearId} onChange={handleYearChange} className={styles.selectBox}>
                    {years.map((year) => (
                        <option key={year.id} value={year.id}>{year.year}</option>
                    ))}
                </select>

                {/* GDP の入力 */}
                <input
                    type="number"
                    value={gdp}
                    onChange={(e) => setGdp(e.target.value)}
                    placeholder="GDP"
                    className={styles.Input}
                />

                <button type="submit">Add Economic Data</button>
            </form>
        </div>
    );
};

export default AddEconomicDataForm;
