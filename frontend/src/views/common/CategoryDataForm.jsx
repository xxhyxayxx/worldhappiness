import styles from '../../styles/Data.module.css';

const CategoryDataForm = ({
    title,
    dataValue,
    setDataValue,
    dataLabel,
    handleSubmit,
    countryRegions,
    selectedCountryRegionId,
    years,
    selectedYearId,
    error,
    formType,
    handleCountryRegionChange,
    handleYearChange,
}) => {

    const handleDataChange = (e) => {
        setDataValue(e.target.value);
    };

    const buttonText = formType === 'edit' ? 'Update' : 'Add';

    return (
        <div className={styles.addBox}>
            <h1 className={styles.dataTitle}>{title}</h1>
            {error && <p className={styles.error}>{error}</p>}

            <form onSubmit={handleSubmit} className={styles.addData}>
                <select 
                    value={selectedCountryRegionId} 
                    onChange={handleCountryRegionChange} 
                    className={styles.selectBox}
                >
                    {countryRegions.map((cr) => (
                        <option key={cr.id} value={cr.id}>{cr.country} - {cr.region}</option>
                    ))}
                </select>
                <select 
                    value={selectedYearId} 
                    onChange={handleYearChange} 
                    className={styles.selectBox}
                >
                    {years.map((year) => (
                        <option key={year.id} value={year.id}>{year.year}</option>
                    ))}
                </select>
                <input
                    type="number"
                    value={dataValue}
                    onChange={handleDataChange}
                    placeholder={dataLabel}
                    className={styles.Input}
                />
                <button type="submit" className={styles.submitButton}>{buttonText} {dataLabel} Data</button>
            </form>
        </div>
    );
};

export default CategoryDataForm;
