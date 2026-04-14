import './Home.css'

const marqueeItems = ['PRECISION', 'PERFORMANCE', 'CONTROL', 'RELIABILITY', 'SPEED']

const features = [
  { num: '01', title: 'Surgical Precision', body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.' },
  { num: '02', title: 'Zero Overhead', body: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.' },
  { num: '03', title: 'Total Control', body: 'Sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque.' },
  { num: '04', title: 'Composable Core', body: 'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione.' },
  { num: '05', title: 'Edge-Native', body: 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Ut labore et dolore magnam aliquam quaerat.' },
  { num: '06', title: 'Unbreakable API', body: 'Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur vel illum qui dolorem eum fugiat.' },
]

const testimonials = [
  { text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla — exactly what we needed.', name: 'Alex Reinholt', role: 'Staff Engineer, Meridian Systems' },
  { text: 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque. Nemo enim ipsam voluptatem. We cut deployment time in half.', name: 'Priya Varma', role: 'CTO, Nullpoint Labs' },
  { text: 'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam. The edge performance is unlike anything we\'ve benchmarked.', name: 'Marcus Chen', role: 'Principal Architect, Vanta' },
  { text: 'Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae. Dagger removed every bottleneck we had in our pipeline.', name: 'Sofía Delgado', role: 'Lead Platform Engineer, Ironframe' },
]

export default function Home() {
  return (
    <>
      <nav>
        <a className="logo" href="#">DAG<span>G</span>ER</a>
        <ul>
          <li><a href="#">Product</a></li>
          <li><a href="#">Docs</a></li>
          <li><a href="#">Pricing</a></li>
          <li><a href="#" className="nav-cta">Get Access</a></li>
        </ul>
      </nav>

      <section className="hero">
        <div className="hero-line" />
        <div className="hero-eyebrow">Precision tooling — v2.4.0</div>
        <h1>CUT<br />THROUGH<br /><em>NOISE</em></h1>
        <p className="hero-sub">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua — sharp, fast, uncompromising.</p>
        <div className="hero-actions">
          <a href="#" className="btn-primary">Start Building</a>
          <a href="#" className="btn-ghost">See the docs</a>
        </div>
        <div className="hero-scroll">Scroll</div>
      </section>

      <div className="marquee-wrap">
        <div className="marquee-track">
          {[...marqueeItems, ...marqueeItems, ...marqueeItems].map((item, i) => (
            <div className="marquee-item" key={i}><span>—</span>{item}</div>
          ))}
        </div>
      </div>

      <section className="features">
        <div className="section-label">Core capabilities</div>
        <div className="features-grid">
          {features.map((f) => (
            <div className="feature-card" key={f.num}>
              <div className="feature-num">{f.num}</div>
              <div className="feature-title">{f.title}</div>
              <p className="feature-body">{f.body}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="split">
        <div className="split-left">
          <div className="section-label">Why Dagger</div>
          <h2>BUILT FOR THE UNFORGIVING</h2>
          <p className="body-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
          <p className="body-text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident sunt in culpa.</p>
          <div className="stat-row">
            <div>
              <div className="stat-num">99<span>.9%</span></div>
              <div className="stat-label">Uptime SLA</div>
            </div>
            <div>
              <div className="stat-num">0<span>ms</span></div>
              <div className="stat-label">Cold Start</div>
            </div>
            <div>
              <div className="stat-num">14<span>k+</span></div>
              <div className="stat-label">Teams</div>
            </div>
          </div>
        </div>
        <div className="split-right">
          <div className="section-label">Philosophy</div>
          <h2>LESS IS SHARP</h2>
          <p className="body-text" style={{ position: 'relative', zIndex: 1 }}>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam eaque ipsa quae ab illo inventore.</p>
          <p className="body-text" style={{ position: 'relative', zIndex: 1 }}>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione sequi nesciunt.</p>
        </div>
      </section>

      <section className="testimonials">
        <div className="section-label">From the field</div>
        <div className="testimonial-grid">
          {testimonials.map((t) => (
            <div className="testimonial" key={t.name}>
              <p className="testimonial-text">{t.text}</p>
              <div className="testimonial-author">
                <strong>{t.name}</strong>
                {t.role}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="cta">
        <h2>GO<br />SHARP</h2>
        <p className="body-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <a href="#" className="btn-primary">Request Early Access</a>
      </section>

      <footer>
        <div className="footer-copy">© 2025 Dagger Inc. All rights reserved.</div>
        <ul className="footer-links">
          <li><a href="#">Privacy</a></li>
          <li><a href="#">Terms</a></li>
          <li><a href="#">Status</a></li>
          <li><a href="#">GitHub</a></li>
        </ul>
      </footer>
    </>
  )
}