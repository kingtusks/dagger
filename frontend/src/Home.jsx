import "./Home.css";
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <>
      <h1>home</h1>
      <Link to="/countries">countries</Link>
    </>
  );
}