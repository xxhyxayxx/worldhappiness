import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const useSubmitForm = (submitFunction, successPath) => {
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (formData) => {
    try {
      await submitFunction(formData);
      navigate(successPath);
    } catch (error) {
      setError(error.message || 'An error occurred while submitting the form.');
    }
  };

  return { handleSubmit, error };
};

export default useSubmitForm;
