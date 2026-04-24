import "./Home.css";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [open, setOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (query.length < 2) {
      setSuggestions([]);
      setOpen(false);
      return;
    }

    const timeout = setTimeout(async () => {
      const res = await fetch(`http://localhost:3000/api/search/${query}`);
      const data = await res.json();
      setSuggestions(data);
      setOpen(true);
    }, 300);

    return () => clearTimeout(timeout);
  }, [query]);

  function handleSelect(name) {
    setQuery(name);
    setOpen(false);
    navigate(`/player/${encodeURIComponent(name)}`);
  }

  return (
    <>
      <h1>home</h1>
      <div className="search-container">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search player..."
          onBlur={() => setTimeout(() => setOpen(false), 150)}
          onFocus={() => suggestions.length > 0 && setOpen(true)}
        />
        {open && suggestions.length > 0 && (
          <ul className="suggestions">
            {suggestions.map((s) => (
              <li key={s.name} onMouseDown={() => handleSelect(s.name)}>
                {s.name}
              </li>
            ))}
          </ul>
        )}
      </div>
    </>
  );
}