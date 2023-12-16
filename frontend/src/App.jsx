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
import SocialSupportDataList from './views/SocialSupportDataList';
import AddSocialSupportDataForm from './views/AddSocialSupportDataForm';
import EditSocialSupportDataForm from './views/EditSocialSupportDataForm';
import Header from './views/common/Header';
import HealthDataList from './views/HealthDataList';
import AddHealthDataForm from './views/AddHealthDataForm';
import EditHealthDataForm from './views/EditHealthDataForm';
import HappinessScoreList from './views/HappinessScoreList';
import AddHappinessScoreForm from './views/AddHappinessScoreForm';
import EditHappinessScoreForm from './views/EditHappinessScoreForm';

function App() {
    return (
        <BrowserRouter>
        <Header />
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

                    <Route path="/socialsupport-data" element={<SocialSupportDataList />} />
                    <Route path="/add-socialsupport-data" element={<AddSocialSupportDataForm />} />
                    <Route path="/edit-socialsupport-data/:socialSupportDataId" element={<EditSocialSupportDataForm />} />

                    <Route path="/health-data" element={<HealthDataList />} />
                    <Route path="/add-health-data" element={<AddHealthDataForm />} />
                    <Route path="/edit-health-data/:healthDataId" element={<EditHealthDataForm />} />

                    <Route path="/happinessscore-data" element={<HappinessScoreList />} />
                    <Route path="/add-happinessscore-data" element={<AddHappinessScoreForm />} />
                    <Route path="/edit-happinessscore-data/:happinessScoreId" element={<EditHappinessScoreForm />} />
                </Routes>
            </MainWrapper>
        </BrowserRouter>
    );
}

export default App;