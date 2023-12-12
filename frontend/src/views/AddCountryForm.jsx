import { useEffect, useState } from 'react';
import { addEconomicData, getCountryRegions, getYears } from '../api/data';
import { useNavigate } from 'react-router-dom';

const AddEconomicDataForm = () => {
    const [countryRegions, setCountryRegions] = useState([]);
    const [selectedCountryRegion, setSelectedCountryRegion] = useState('');
    const [years, setYears] = useState([]);
    const [selectedYear, setSelectedYear] = useState('');
    const [gdp, setGdp] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        // CountryRegion と Year のデータを取得
        const fetchData = async () => {
            const countryRegionsData = await getCountryRegions();
            setCountryRegions(countryRegionsData);
            const yearsData = await getYears();
            setYears(yearsData);
        };
        fetchData();
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await addEconomicData({ country_region_id: selectedCountryRegion, year_id: selectedYear, gdp });
            navigate('/economic-data');
            // 成功した場合の処理
        } catch (error) {
            // エラー処理
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* CountryRegion の選択 */}
            <select
                value={selectedCountryRegion}
                onChange={(e) => setSelectedCountryRegion(e.target.value)}
            >
                {countryRegions.map((cr) => (
                    <option key={cr.id} value={cr.id}>
                        {cr.country} - {cr.region}
                    </option>
                ))}
            </select>

            <select
                value={selectedYear}
                onChange={(e) => setSelectedYear(e.target.value)}
            >
                {years.map((year) => (
                    <option key={year} value={year}>
                        {year}
                    </option>
                ))}
            </select>

            {/* GDP の入力 */}
            <input
                type="number"
                value={gdp}
                onChange={(e) => setGdp(e.target.value)}
                placeholder="GDP"
            />
            <button type="submit">Add Economic Data</button>
        </form>
    );
};

export default AddEconomicDataForm;
