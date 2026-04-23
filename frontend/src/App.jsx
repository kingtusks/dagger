import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import Countries from './Countries';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/countries" element={<Countries />} />
      </Routes>
    </Router>
  );
}