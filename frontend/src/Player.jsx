import { useEffect, useState } from "react";
import "./Player.css";
import { useParams } from "react-router-dom";

export default function Player() {
    const {player_name} = useParams();
    const [stats, setStats] = useState([])

    useEffect(() => {
        fetch(`http://localhost:3000/api/stats/${encodeURIComponent(player_name)}`)
            .then(r => r.json()) //r.json() converts to data
            .then(data => setStats(data));
    }, [player_name])

    return (
        <>
            <h1>{player_name}</h1>
            <h2>{JSON.stringify(stats)}</h2>
        </>
    );
}