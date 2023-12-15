import { useState } from 'react';

const useFormData = (initialValue, validationType = 'number') => {
  const [value, setValue] = useState(initialValue);
  const [error, setError] = useState('');

  const validateValue = () => {
    if (value === '') {
      setError('Field must be filled.');
      return false;
    }

    // 数値のバリデーション
    if (validationType === 'number') {
      const numberRegex = /^\d{0,7}(\.\d{0,3})?$/;
      if (!numberRegex.test(value)) {
        setError('Value must be a number with up to 10 digits and 3 decimal places.');
        return false;
      }
    }

    // 文字列のバリデーション（半角英字および特定の記号）
    if (validationType === 'text') {
      const textRegex = /^[a-zA-Z\s\-]+$/;
      if (!textRegex.test(value)) {
        setError('Value must be a valid string (letters, spaces, hyphens).');
        return false;
      }
    }

    setError('');
    return true;
  };

  return { value, setValue, validateValue, error };
};

export default useFormData;
