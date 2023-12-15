import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getSocialSupportDataById, updateSocialSupportData } from '../api/data';
import useFormData from '../hooks/useFormData';
import useSubmitForm from '../hooks/useSubmitForm';
import useFetchCountryRegions from '../hooks/useFetchCountryRegions';
import useFetchYears from '../hooks/useFetchYears';
import CategoryDataForm from './common/CategoryDataForm';

const EditSocialSupportDataForm = () => {
    const { socialSupportDataId } = useParams();
    const { countryRegions } = useFetchCountryRegions();
    const { years } = useFetchYears();
    const { value: socialSupport, setValue: setSocialSupport, validateValue, error: socialSupportError } = useFormData('', 'number');
    const [selectedCountryRegionId, setSelectedCountryRegionId] = useState('');
    const [selectedYearId, setSelectedYearId] = useState('');

    const { handleSubmit, error: submitError } = useSubmitForm(async (payload) => {
        await updateSocialSupportData(socialSupportDataId, payload);
    }, '/socialsupport-data');

    useEffect(() => {
        const fetchSocialSupportData = async () => {
            try {
                const data = await getSocialSupportDataById(socialSupportDataId);
                setSocialSupport(data.social_support);
                setSelectedCountryRegionId(data.country_region.id);
                setSelectedYearId(data.year.id);
            } catch (error) {
                console.error("Error fetching social support data:", error);
            }
        };
        fetchSocialSupportData();
    }, [socialSupportDataId]);

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
            social_support: socialSupport
        };
        await handleSubmit(payload);
    };

    return (
        <CategoryDataForm
            title="Edit Social Support Data"
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
            formType="edit"
            handleCountryRegionChange={handleCountryRegionChange}
            handleYearChange={handleYearChange}
        />
    );
};

export default EditSocialSupportDataForm;
