import React from 'react';
import { addEconomicData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const AddEconomicDataForm = () => {
    const { value: gdp, setValue: setGdp, validateValue, error: gdpError } = useFormData('', 'number');
    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await addEconomicData(payload);
    }, '/economic-data');

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
            gdp: gdp
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
            value: gdp,
            onChange: (e) => setGdp(e.target.value),
            placeholder: 'GDP',
        }
    ];

    return (
        <CategoryDataForm
            title="Add Economic Data"
            handleSubmit={handleFormSubmit}
            inputs={inputs}
            buttonText="Add"
            error={gdpError || submitError}
        />
    );
};

export default AddEconomicDataForm;
