import { Link } from 'react-router-dom';
import { useAuthStore } from '../store/auth';
import styles from '../styles/Home.module.css';

const Home = () => {
    const [isLoggedIn, user] = useAuthStore((state) => [
        state.isLoggedIn,
        state.user,
    ]);
    return (
        <div className={styles.homeBox}>
            {isLoggedIn() ? <LoggedInView user={user()} /> : <LoggedOutView />}
        </div>
    );
};

const LoggedInView = ({ user }) => {
    return (
        <div className={styles.home}>
            <h1 className={styles.homeTitle}>Welcome {user.username}</h1>
            <div className={styles.homeText}>
                <h2>What is The World Happiness Report?</h2>
                <p>The World Happiness Report is a survey of happiness levels published by the Sustainable Development Solutions Network of the United Nations. In this survey, happiness is measured as the average of responses to public opinion polls asking individuals to rate their own happiness on a scale from 0 to 10, representing a subjective value with data provided by Gallup. The report conducts regression analysis on this measure of happiness using six explanatory variables, including GDP and healthy life expectancy, to determine the contribution of each variable to overall happiness.</p>
                <p>The first report was published in April 2012. The second report followed in 2013, and since then, the report has been published annually.</p>
            </div>
        </div>
    );
};

export const LoggedOutView = () => {
    return (
        <div className={styles.home}>
            <h1 className={styles.homeTitle}>Welcome</h1>
            <div className={styles.homeText}>
                <h2>What is The World Happiness Report?</h2>
                <p>The World Happiness Report is a survey of happiness levels published by the Sustainable Development Solutions Network of the United Nations. In this survey, happiness is measured as the average of responses to public opinion polls asking individuals to rate their own happiness on a scale from 0 to 10, representing a subjective value with data provided by Gallup. The report conducts regression analysis on this measure of happiness using six explanatory variables, including GDP and healthy life expectancy, to determine the contribution of each variable to overall happiness.</p>
                <p>The first report was published in April 2012. The second report followed in 2013, and since then, the report has been published annually.</p>
            </div>
            <ul className={styles.buttons}>
                <li>
                    <Link to="/login">
                        <button>Login</button>
                    </Link>
                </li>
                <li>
                    <Link to="/register">
                        <button>Register</button>
                    </Link>
                </li>
            </ul>
        </div>
    );
};

export default Home;