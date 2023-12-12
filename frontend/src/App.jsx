import './App.css';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Home from './views/Home';
import MainWrapper from '../layouts/MainWrapper';
import Login from './views/Login';
import PrivateRoute from '../layouts/PrivateRoute';
import Logout from './views/Logout';
import Private from './views/Private';
import Register from './views/Register';

function App() {
    return (
        <BrowserRouter>
            <MainWrapper>
                <Routes>
                    <Route
                        path="/private"
                        element={
                            <PrivateRoute>
                                <Private />
                            </PrivateRoute>
                        }
                    />
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/logout" element={<Logout />} />
                </Routes>
            </MainWrapper>
        </BrowserRouter>
    );
}

export default App;