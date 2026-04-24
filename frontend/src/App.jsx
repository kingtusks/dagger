import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Player from './Player';
import Countries from './Countries';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/countries" element={<Countries />} />
        <Route path="/player/:player_name" element={<Player />} />
      </Routes>
    </Router>
  );
}