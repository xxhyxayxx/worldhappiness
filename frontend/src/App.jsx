import './App.css';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Home from './views/Home';
import MainWrapper from '../layouts/MainWrapper';
import Login from './views/Login';
import PrivateRoute from '../layouts/PrivateRoute';
import Logout from './views/Logout';
import Private from './views/Private';
import Register from './views/Register';
import Countries from './views/Countries';
import AddCountryForm from './views/AddCountryForm';
import EditCountryForm from './views/EditCountryForm';
import EconomicDataList from './views/EconomicDataList';
import AddEconomicDataForm from './views/AddEconomicDataForm';
import EditEconomicDataForm from './views/EditEconomicDataForm';


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
                    <Route path="/countries" element={<Countries />} />
                    <Route path="/add-country" element={<AddCountryForm />} />
                    <Route path="/edit-country/:countryId" element={<EditCountryForm />} />

                    <Route path="/economic-data" element={<EconomicDataList />} />
                    <Route path="/add-economic-data" element={<AddEconomicDataForm />} />
                    <Route path="/edit-economic-data/:economicDataId" element={<EditEconomicDataForm />} />
                </Routes>
            </MainWrapper>
        </BrowserRouter>
    );
}

export default App;