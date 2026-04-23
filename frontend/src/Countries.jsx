import "./Countries.css";
import { useState, useEffect } from "react";

export default function Countries() {
    const [countries, setCountries] = useState([]);

    useEffect(() => {
    fetch('http://localhost:3000/api/countries')
        .then(res => res.json())
        .then(data => setCountries(data));
    }, []);

    return (
        <>
            <h1>countries</h1>
            <p>{JSON.stringify(countries, null)}</p>
        </>
    );
}