import React from 'react';
import { addCountry } from '../api/data';
import styles from '../styles/Data.module.css';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchRegions from '../hooks/useFetchRegions';

const AddCountryForm = () => {
    const { value: name, setValue: setName, validateValue, error: nameError } = useFormData('', 'text');
    const { regions, selectedRegionId, setSelectedRegionId } = useFetchRegions();

    const handleRegionChange = (e) => {
        setSelectedRegionId(e.target.value);
    };

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await addCountry(payload);
    }, '/countries');

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        if (!validateValue() || !selectedRegionId) {
            return;
        }
        const payload = {
            name,
            region_id: parseInt(selectedRegionId, 10)
        };
        await handleSubmit(payload);
    };

    return (
        <div className={styles.addBox}>
            <h1 className={styles.dataTitle}>Add Country</h1>
            <form onSubmit={handleFormSubmit} className={styles.addData}>
                {nameError && <p className={styles.error}>{nameError}</p>}
                {submitError && <p className={styles.error}>{submitError}</p>}
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Country name"
                    className={styles.Input}
                />
                <select
                    value={selectedRegionId}
                    onChange={handleRegionChange}
                    className={styles.selectBox}
                >
                    {regions.map((region) => (
                        <option key={region.id} value={region.id}>{region.name}</option>
                    ))}
                </select>
                <button type="submit">Add Country</button>
            </form>
        </div>
    );
};

export default AddCountryForm;
