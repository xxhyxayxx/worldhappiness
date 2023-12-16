import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getHappinessScoreById, updateHappinessScore } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const EditHappinessScoreForm = () => {
    const { happinessScoreId } = useParams();
    const { countryRegions } = useFetchCountryRegions();
    const { years } = useFetchYears();
    const { value: happiness_score, setValue: setHappiness, validateValue, error: happinessError } = useFormData('', 'number');
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    const [selectedYearId, setSelectedYearId] = useState('');

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await updateHappinessScore(happinessScoreId, payload);
    }, '/happinessscore-data');

    useEffect(() => {
        const fetchHappinessScore = async () => {
            try {
                const data = await getHappinessScoreById(happinessScoreId);
                setHappiness(data.happiness_score);
                setSelectedCountryRegionId(data.country_region.id);
                setSelectedYearId(data.year.id);
            } catch (error) {
                console.error("Error fetching happiness score data:", error);
            }
        };
        fetchHappinessScore();
    }, [happinessScoreId]);

    const handleCountryRegionChange = (e) => {
        setSelectedCountryRegionId(e.target.value);
    };

    const handleYearChange = (e) => {
        setSelectedYearId(e.target.value);
    };

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        if (!validateValue() || !selectedCountryRegionId || !selectedYearId) {
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
            title="Edit Happiness Score"
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
            formType="edit"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default EditHappinessScoreForm;
