import { useEffect, useState } from 'react';
import { register } from '../utils/auth';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/auth';
import styles from '../styles/Data.module.css';

function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn);
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoggedIn()) {
            navigate('/');
        }
    }, []);

    const resetForm = () => {
        setUsername('');
        setPassword('');
        setPassword2('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { error } = await register(username, password, password2);
        if (error) {
            alert(JSON.stringify(error));
        } else {
            navigate('/');
            resetForm();
        }
    };

    return (
        <section className={styles.loginBox}>
            <form onSubmit={handleSubmit}>
                <h1 className={styles.registerTitle}>Register</h1>
                <div>
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Username"
                        required
                        className={styles.loginInput}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Password"
                        required
                        className={styles.loginInput}
                    />
                </div>
                <div>
                    <label htmlFor="confirm-password">Confirm Password</label>
                    <input
                        type="password"
                        id="confirm-password"
                        onChange={(e) => setPassword2(e.target.value)}
                        placeholder="Confirm Password"
                        required
                        className={styles.loginInput}
                    />
                    <p>
                        {password2 !== password ? 'Passwords do not match' : ''}
                    </p>
                </div>
                <button type="submit" className={styles.loginSubmit}>Register</button>
            </form>
        </section>
    );
}

export default Register;