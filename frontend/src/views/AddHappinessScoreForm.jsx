import React from 'react';
import { addHappinessScore } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const AddHappinessScoreForm = () => {
    const { value: happiness_score, setValue: setHappiness, validateValue, error: happinessError } = useFormData('', 'number');
    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await addHappinessScore(payload);
    }, '/happinessscore-data');

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
            happiness_score: happiness_score
        };
        await handleSubmit(payload);
    };

    return (
        <CategoryDataForm
            title="Add Happiness Score"
            dataValue={happiness_score}
            setDataValue={setHappiness}
            dataLabel="Happiness"
            handleSubmit={handleFormSubmit}
            countryRegions={countryRegions}
            selectedCountryRegionId={selectedCountryRegionId}
            setSelectedCountryRegionId={setSelectedCountryRegionId}
            years={years}
            selectedYearId={selectedYearId}
            setSelectedYearId={setSelectedYearId}
            error={happinessError || submitError}
            formType="add"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default AddHappinessScoreForm;
