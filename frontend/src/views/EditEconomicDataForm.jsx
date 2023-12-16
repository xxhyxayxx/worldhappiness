import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getEconomicDataById, updateEconomicData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const EditEconomicDataForm = () => {
    const { economicDataId } = useParams();
    const { countryRegions } = useFetchCountryRegions();
    const { years } = useFetchYears();
    const { value: gdp, setValue: setGdp, validateValue, error: gdpError } = useFormData('', 'number');
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    const [selectedYearId, setSelectedYearId] = useState('');

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await updateEconomicData(economicDataId, payload);
    }, '/economic-data');

    useEffect(() => {
        const fetchEconomicData = async () => {
            try {
                const data = await getEconomicDataById(economicDataId);
                setGdp(data.gdp);
                setSelectedCountryRegionId(data.country_region.id);
                setSelectedYearId(data.year.id);
            } catch (error) {
                console.error("Error fetching economic data:", error);
            }
        };
        fetchEconomicData();
    }, [economicDataId]);

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
            title="Edit Economic Data"
            handleSubmit={handleFormSubmit}
            inputs={inputs}
            buttonText="Update"
            error={gdpError || submitError}
        />
    );
};

export default EditEconomicDataForm;
