import "./Home.css";
import { Link } from "react-router-dom";

const today = new Date().toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
});

export default function Home() {
    return (
        <div className="home">
            <header className="masthead">
                <div className="masthead-top">
                    <span className="masthead-date">{today}</span>
                    <span className="masthead-label">The Complete Basketball Record</span>
                </div>

                <h1 className="site-title">
                    DAGG<span>ER</span>
                </h1>

                <nav className="nav-bar">
                    <Link to="/players">Players</Link>
                    <Link to="/teams">Teams</Link>
                    <Link to="/seasons">Seasons</Link>
                    <Link to="/games">Games</Link>
                    <Link to="/standings">Standings</Link>
                    <Link to="/stats">Stats Leaders</Link>
                    <Link to="/draft">Draft History</Link>
                    <Link to="/awards">Awards</Link>
                </nav>
            </header>

            <section className="hero">
                <div className="hero-main">
                    <p className="hero-eyebrow">Welcome to the Archive</p>
                    <h2 className="hero-headline">
                        Every game.<br />
                        Every player.<br />
                        Every <em>dynasty.</em>
                    </h2>
                    <p className="hero-description">
                        A comprehensive record of professional basketball history — from
                        box scores to biographical data, franchise timelines to individual
                        milestones. Browse, filter, and explore.
                    </p>
                    <Link to="/players" className="hero-cta">
                        Explore the database
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </Link>
                </div>

                <div className="hero-divider" />

                <aside className="hero-sidebar">
                    <p className="sidebar-title">By the numbers</p>
                    <div className="stat-item">
                        <span className="stat-number">4<span>,</span>971</span>
                        <span className="stat-label">Players on record</span>
                    </div>
                    <div className="stat-item">
                        <span className="stat-number">30</span>
                        <span className="stat-label">Active franchises</span>
                    </div>
                    <div className="stat-item">
                        <span className="stat-number">77</span>
                        <span className="stat-label">Seasons archived</span>
                    </div>
                    <div className="stat-item">
                        <span className="stat-number">60<span>k+</span></span>
                        <span className="stat-label">Games with box scores</span>
                    </div>
                </aside>
            </section>

            <section className="section-grid">
                <div className="section-card">
                    <p className="card-number">01</p>
                    <h3 className="card-title">Players &amp; Rosters</h3>
                    <p className="card-description">
                        Career stats, biographical data, and season-by-season breakdowns for
                        every player to appear in an NBA game.
                    </p>
                    <Link to="/players" className="card-link">Browse Players →</Link>
                </div>

                <div className="section-card">
                    <p className="card-number">02</p>
                    <h3 className="card-title">Teams &amp; Franchises</h3>
                    <p className="card-description">
                        Full franchise histories, season records, championship runs, and
                        coaching tenures from 1946 to present.
                    </p>
                    <Link to="/teams" className="card-link">Browse Teams →</Link>
                </div>

                <div className="section-card">
                    <p className="card-number">03</p>
                    <h3 className="card-title">Stats &amp; Leaders</h3>
                    <p className="card-description">
                        Season and career statistical leaders across all tracked categories —
                        traditional, advanced, and play-by-play.
                    </p>
                    <Link to="/stats" className="card-link">View Leaderboards →</Link>
                </div>
            </section>

            <footer className="home-footer">
                <span className="footer-brand">
                    DAGG<strong>ER</strong>
                </span>
                <span className="footer-note">Data updated nightly</span>
            </footer>

        </div>
    );
}