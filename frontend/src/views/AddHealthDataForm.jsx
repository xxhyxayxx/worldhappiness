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

    return (
        <CategoryDataForm
            title="Add Health Data"
            dataValue={life_expectancy}
            setDataValue={setHealth}
            dataLabel="Health"
            handleSubmit={handleFormSubmit}
            countryRegions={countryRegions}
            selectedCountryRegionId={selectedCountryRegionId}
            setSelectedCountryRegionId={setSelectedCountryRegionId}
            years={years}
            selectedYearId={selectedYearId}
            setSelectedYearId={setSelectedYearId}
            error={healthError || submitError}
            formType="add"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default AddHealthDataForm;
