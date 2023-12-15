import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getHealthDataById, updateHealthData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const EditHealthDataForm = () => {
    const { healthDataId } = useParams();
    const { countryRegions } = useFetchCountryRegions();
    const { years } = useFetchYears();
    const { value: life_expectancy, setValue: setHealth, validateValue, error: healthError } = useFormData('', 'number');
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    const [selectedYearId, setSelectedYearId] = useState('');

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await updateHealthData(healthDataId, payload);
    }, '/health-data');

    useEffect(() => {
        const fetchHealthData = async () => {
            try {
                const data = await getHealthDataById(healthDataId);
                setHealth(data.life_expectancy);
                setSelectedCountryRegionId(data.country_region.id);
                setSelectedYearId(data.year.id);
            } catch (error) {
                console.error("Error fetching health data:", error);
            }
        };
        fetchHealthData();
    }, [healthDataId]);

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
            life_expectancy: life_expectancy
        };
        await handleSubmit(payload);
    };

    return (
        <CategoryDataForm
            title="Edit Health Data"
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
            formType="edit"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default EditHealthDataForm;
