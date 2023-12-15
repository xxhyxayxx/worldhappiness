import React from 'react';
import { addSocialSupportData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const AddSocialSupportDataForm = () => {
    const { value: socialSupport, setValue: setSocialSupport, validateValue, error: socialSupportError } = useFormData('', 'number');
    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await addSocialSupportData(payload);
    }, '/socialsupport-data');

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
            social_support: socialSupport
        };
        await handleSubmit(payload);
    };

    return (
        <CategoryDataForm
            title="Add Social Support Data"
            dataValue={socialSupport}
            setDataValue={setSocialSupport}
            dataLabel="Social Support"
            handleSubmit={handleFormSubmit}
            countryRegions={countryRegions}
            selectedCountryRegionId={selectedCountryRegionId}
            setSelectedCountryRegionId={setSelectedCountryRegionId}
            years={years}
            selectedYearId={selectedYearId}
            setSelectedYearId={setSelectedYearId}
            error={socialSupportError || submitError}
            formType="add"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default AddSocialSupportDataForm;
