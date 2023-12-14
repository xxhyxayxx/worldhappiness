import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getEconomicDataById, updateEconomicData, getCountryRegions, getYears } from '../api/data';
import styles from '../styles/Data.module.css';

const EditEconomicDataForm = () => {
    // ステート変数の初期値として ID を使用
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    const [selectedYearId, setSelectedYearId] = useState('');
    const [gdp, setGdp] = useState('');
    const [countryRegions, setCountryRegions] = useState([]);
    const [years, setYears] = useState([]);
    const { economicDataId } = useParams();
    const navigate = useNavigate();
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchEconomicDataAndOptions = async () => {
            try {
                const economicData = await getEconomicDataById(economicDataId);
                // 経済データのロード時に ID を使用
                setSelectedCountryRegionId(economicData.country_region.id);
                setSelectedYearId(economicData.year.id);
                setGdp(economicData.gdp);

                const regionsData = await getCountryRegions();
                setCountryRegions(regionsData);

                const yearsData = await getYears();
                setYears(yearsData);
            } catch (error) {
                // エラー処理
            }
        };
        fetchEconomicDataAndOptions();
    }, [economicDataId]);

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

    const handleSubmit = async (event) => {
        event.preventDefault();
        const isValid = validateInput();
        if (!isValid) {
            return; // バリデーションが失敗した場合はここで処理を止める
        }

        try {
            // バリデーションが成功した場合のみAPI呼び出しを行う
            await updateEconomicData(economicDataId, {
                country_region_id: selectedCountryRegionId,
                year_id: selectedYearId,
                gdp
            });
            navigate('/economic-data');
        } catch (error) {
            // エラー処理
            setError('Failed to update economic data.');
        }
    };

    return (
        <div className={styles.editBox}>
            <h1 className={styles.dataTitle}>Edit Economic Data</h1>
            {error && <p className={styles.error}>{error}</p>}
            <form onSubmit={handleSubmit} className={styles.editData}>
                {/* CountryRegion のセレクトボックス */}
                <select
                    value={selectedCountryRegionId}
                    onChange={(e) => setSelectedCountryRegionId(e.target.value)}
                    className={styles.selectBox}
                >
                    {countryRegions.map((cr) => (
                        <option key={cr.id} value={cr.id}>
                            {cr.country} - {cr.region}
                        </option>
                    ))}
                </select>

                {/* Year のセレクトボックス */}
                <select
                    value={selectedYearId}
                    onChange={(e) => setSelectedYearId(e.target.value)}
                        className={styles.selectBox}
                >
                    {years.map((y) => (
                        <option key={y.id} value={y.id}>
                            {y.year}
                        </option>
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

                <button type="submit">Update Economic Data</button>
            </form>
        </div>
    );
};

export default EditEconomicDataForm;
