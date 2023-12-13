// components/Header.js
import { Link } from 'react-router-dom';
import { useAuthStore } from '../store/auth';

const Header = () => {
  const isLoggedIn = useAuthStore((state) => state.isLoggedIn());

  return (
    <header>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          {isLoggedIn ? (
            <>
              <li><Link to="/countries">Countries</Link></li>
              <li><Link to="/economic-data">Economic Data</Link></li>
              <li><Link to="/logout">Logout</Link></li>
            </>
          ) : (
            <>
              <li><Link to="/login">Login</Link></li>
              <li><Link to="/register">Register</Link></li>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;