// Routes
import { BrowserRouter,Routes,Route } from 'react-router-dom';

// Components
import NavBar from './Components/NavBar/NavBar.jsx';

// css imports
import './App.css';
import Intropage from './pages/Intropage';
import Errorpage from './pages/Errorpage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />

        <Routes>
          <Route path="" element={<Intropage />} />

          {/* For Other Pages */}
          <Route path="*" element={<Errorpage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
