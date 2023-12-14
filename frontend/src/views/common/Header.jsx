// components/Header.js
import { Link } from 'react-router-dom';
import { useAuthStore } from '../../store/auth';
import styles from '../../styles/Header.module.css';

const Header = () => {
  const isLoggedIn = useAuthStore((state) => state.isLoggedIn());

  return (
    <header className={styles.header}>
      <nav>
        <ul className={styles.nav}>
          <li className={styles.home}><Link to="/">WORLD HAPPINESS DATA</Link></li>
          {isLoggedIn ? (
            <ul className={styles.subNav}>
              <li className={styles.subNavItem}><Link to="/countries">Countries</Link></li>
              <li className={styles.subNavItem}><Link to="/economic-data">Economic</Link></li>
              <li className={styles.subNavItem}><Link to="/socialsupport-data">Social Support</Link></li>
              <li className={styles.subNavItem}><Link to="/logout">Logout</Link></li>
            </ul>
          ) : (
            <ul className={styles.subNav}>
              <li className={styles.subNavItem}><Link to="/login">Login</Link></li>
              <li className={styles.subNavItem}><Link to="/register">Register</Link></li>
            </ul>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;