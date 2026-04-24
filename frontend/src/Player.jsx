import { useEffect, useState } from "react";
import "./Player.css";
import { useParams } from "react-router-dom";

export default function Player() {
    const {player_name} = useParams();
    const [stats, setStats] = useState([]);
    const [awards, setAwards] = useState([]);

    useEffect(() => {
        Promise.all([
            fetch(`http://localhost:3000/api/stats/${encodeURIComponent(player_name)}`).then(r => r.json()),
            fetch(`http://localhost:3000/api/awards/${encodeURIComponent(player_name)}`).then(r => r.json()),
        ]).then(([statsData, awardsData]) => {
            setStats(statsData);
            setAwards(awardsData);
        });
    }, [player_name])

    return (
        <>
            <h1>{player_name}</h1>
            <h2>{JSON.stringify(stats)}</h2>
        </>
    );
}