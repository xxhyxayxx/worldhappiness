import React from 'react';
import styles from '../../styles/Data.module.css';

const CategoryDataForm = ({
    title,
    handleSubmit,
    inputs,
    buttonText,
    error,
}) => {
    return (
        <div className={styles.addBox}>
            <h1 className={styles.dataTitle}>{title}</h1>
            {error && <p className={styles.error}>{error}</p>}

            <form onSubmit={handleSubmit} className={styles.addData}>
                {inputs.map((input, index) => (
                    <React.Fragment key={index}>
                        {input.type === 'select' ? (
                            <select 
                                value={input.value} 
                                onChange={input.onChange} 
                                className={styles.selectBox}
                            >
                                {input.options.map((option) => (
                                    <option key={option.value} value={option.value}>{option.label}</option>
                                ))}
                            </select>
                        ) : (
                            <input
                                type={input.type}
                                value={input.value}
                                onChange={input.onChange}
                                placeholder={input.placeholder}
                                className={styles.Input}
                            />
                        )}
                    </React.Fragment>
                ))}
                <button type="submit" className={styles.submitButton}>{buttonText}</button>
            </form>
        </div>
    );
};

export default CategoryDataForm;
