import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCountryById, updateCountry } from '../api/data';
import styles from '../styles/Data.module.css';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchRegions from '../hooks/useFetchRegions';

const EditCountryForm = () => {
    const { countryId } = useParams();
    const navigate = useNavigate();
    const { regions, selectedRegionId, setSelectedRegionId } = useFetchRegions();
    const { value: name, setValue: setName, validateValue, error: nameError } = useFormData('', 'text');

    const handleSubmitSuccess = () => {
        navigate('/countries', { state: { refresh: true } });
    };

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await updateCountry(countryId, payload);
        handleSubmitSuccess();
    }, '/countries');

    useEffect(() => {
        const fetchCountryData = async () => {
            try {
                const countryData = await getCountryById(countryId);
                setName(countryData.name);
                if (countryData.regions && countryData.regions.length > 0) {
                    console.log(countryData.regions); 
                    setSelectedRegionId(countryData.regions[0].id); // 最初のリージョンのIDを取得
                } else {
                    console.log('Region data is not available for this country');
                    setSelectedRegionId('');  // region がない場合は空文字列を設定
                }
            } catch (error) {
                console.error('Error fetching regions:', error);
            }
        };
        fetchCountryData();
    }, [countryId, setName, setSelectedRegionId]);    
    

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        if (!validateValue() || !selectedRegionId) {
            return;
        }
        const payload = {
            name,
            region_id: selectedRegionId
        };
        await handleSubmit(payload);
    };

    return (
        <div className={styles.addBox}>
            <h1 className={styles.dataTitle}>Edit Country Data</h1>
            {nameError && <p className={styles.error}>{nameError}</p>}
            {submitError && <p className={styles.error}>{submitError}</p>}
            <form onSubmit={handleFormSubmit} className={styles.addData}>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Country name"
                    className={styles.Input}
                />
                <select
                    value={selectedRegionId}
                    onChange={(e) => setSelectedRegionId(e.target.value)}
                    className={styles.selectBox}
                >
                    {regions.map((region) => (
                        <option key={region.id} value={region.id}>{region.name}</option>
                    ))}
                </select>
                <button type="submit">Update Country</button>
            </form>
        </div>
    );
};

export default EditCountryForm;
