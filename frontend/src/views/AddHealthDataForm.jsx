import React from 'react';
import { addHealthData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const AddHealthDataForm = () => {
    const { value: life_expectancy, setValue: setHealth, validateValue, error: healthError } = useFormData('', 'number');
    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await addHealthData(payload);
    }, '/health-data');

    const { countryRegions, selectedCountryRegionId, setSelectedCountryRegionId } = useFetchCountryRegions();
    const { years, selectedYearId, setSelectedYearId } = useFetchYears();

    const handleCountryRegionChange = (e) => {
        setSelectedCountryRegionId(e.target.value);
    };

    const handleYearChange = (e) => {
        setSelectedYearId(e.target.value);
    };

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        if (!selectedCountryRegionId || !selectedYearId || !validateValue()) {
            return;
        }
        const payload = {
            country_region_id: selectedCountryRegionId,
            year_id: selectedYearId,
            life_expectancy: life_expectancy
        };
        await handleSubmit(payload);
    };

    const inputs = [
        {
            type: 'select',
            value: selectedCountryRegionId,
            onChange: handleCountryRegionChange,
            options: countryRegions.map(cr => ({ value: cr.id, label: `${cr.country} - ${cr.region}` })),
        },
        {
            type: 'select',
            value: selectedYearId,
            onChange: handleYearChange,
            options: years.map(year => ({ value: year.id, label: year.year })),
        },
        {
            type: 'number',
            value: life_expectancy,
            onChange: (e) => setHealth(e.target.value),
            placeholder: 'Health',
        }
    ];

    return (
        <CategoryDataForm
            title="Add Health Data"
            handleSubmit={handleFormSubmit}
            inputs={inputs}
            buttonText="Add"
            error={healthError || submitError}
        />
    );
};

export default AddHealthDataForm;
