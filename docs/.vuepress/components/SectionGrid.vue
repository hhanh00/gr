<script setup>
const groups = [
  {
    number: '01',
    name: 'Foundations',
    desc: 'Build the mathematical and physical language needed for curved spacetime.',
    color: '#2563eb',
    soft: '#dbeafe',
    items: [
      { number: '01', title: 'Spacetime', desc: 'Describe events, intervals, light cones, and causality.', symbol: 'x^\u03bc' },
      { number: '02', title: 'Vectors and tensors', desc: 'Learn the objects that make physical laws coordinate-independent.', symbol: 'T^\u03bc\u03bd' },
      { number: '03', title: 'Curves and motion', desc: 'Move from ordinary trajectories to geometric paths through spacetime.', symbol: '\u03b3(\u03bb)' },
    ],
  },
  {
    number: '02',
    name: 'Differential geometry',
    desc: 'Turn curved spaces into a precise language for physics.',
    color: '#7c3aed',
    soft: '#ede9fe',
    items: [
      { number: '04', title: 'Manifolds', desc: 'Describe spaces locally with coordinates and globally with charts.', symbol: 'M' },
      { number: '05', title: 'Metrics', desc: 'Measure distances, times, angles, and causal structure geometrically.', symbol: 'g\u03bc\u03bd' },
      { number: '06', title: 'Connections and curvature', desc: 'Compare vectors at different points and measure geometric bending.', symbol: '\u2207, R' },
    ],
  },
  {
    number: '03',
    name: 'General relativity',
    desc: 'Build Einstein’s theory from the equivalence principle and an action.',
    color: '#059669',
    soft: '#d1fae5',
    items: [
      { number: '07', title: 'The equivalence principle', desc: 'Understand why gravity can be described as spacetime geometry.', symbol: 'g' },
      { number: '08', title: 'Einstein equations', desc: 'Relate spacetime curvature to matter and energy.', symbol: 'G\u03bc\u03bd' },
      { number: '09', title: 'Geodesics', desc: 'Derive free fall as extremal motion in curved spacetime.', symbol: '\u03b4S = 0' },
    ],
  },
  {
    number: '04',
    name: 'Spacetime solutions',
    desc: 'Explore the geometries that describe stars, black holes, and the universe.',
    color: '#d97706',
    soft: '#fef3c7',
    items: [
      { number: '10', title: 'Schwarzschild spacetime', desc: 'Study the geometry outside a spherical, non-rotating body.', symbol: 'r\u209b' },
      { number: '11', title: 'Black holes', desc: 'Understand horizons, singularities, and causal structure.', symbol: '\u0394t' },
      { number: '12', title: 'Cosmology', desc: 'Apply Einstein’s equations to an expanding homogeneous universe.', symbol: 'a(t)' },
    ],
  },
  {
    number: '05',
    name: 'Gravitational phenomena',
    desc: 'Connect the geometry to observable effects and experiments.',
    color: '#db2777',
    soft: '#fce7f3',
    items: [
      { number: '13', title: 'Gravitational waves', desc: 'Describe propagating distortions of spacetime and their detection.', symbol: 'h\u03bc\u03bd' },
      { number: '14', title: 'Lensing and redshift', desc: 'Calculate how gravity bends light and changes observed frequencies.', symbol: 'z' },
      { number: '15', title: 'Tests of relativity', desc: 'Compare geometric predictions with measurements in the solar system.', symbol: '\u0394\u03c4' },
    ],
  },
]
</script>

<template>
  <div class="gr-home">
    <section class="home-hero" aria-labelledby="home-title">
      <div class="hero-copy">
        <p class="kicker"><span class="kicker-dot"></span>General Relativity</p>
        <h1 id="home-title">Spacetime, explained step by step</h1>
        <p class="hero-text">
          Build the geometry first, then use it to understand gravity, black holes,
          gravitational waves, and the expanding universe.
        </p>
        <div class="hero-actions">
          <span class="start-button">Coming soon</span>
          <span class="chapter-count"><strong>{{ groups.length }}</strong> stages</span>
        </div>
      </div>

      <div class="field-visual" aria-hidden="true">
        <div class="visual-grid"></div>
        <svg class="field-lines" viewBox="0 0 520 420" fill="none">
          <path d="M20 226C87 87 176 82 256 218s172 151 244 4" />
          <path d="M20 276c68-81 142-77 217 2s169 84 263-7" />
          <path d="M42 157c74-74 136-77 202 9s149 89 238-12" />
          <ellipse cx="271" cy="215" rx="174" ry="73" transform="rotate(-24 271 215)" />
          <ellipse cx="271" cy="215" rx="174" ry="73" transform="rotate(34 271 215)" />
        </svg>
        <div class="visual-core">
          <span>g</span>
          <small>spacetime</small>
        </div>
        <span class="particle particle-a"></span>
        <span class="particle particle-b"></span>
        <span class="particle particle-c"></span>
        <div class="formula formula-a">ds² = gμν dxμ dxν</div>
        <div class="formula formula-b">Gμν = 8πTμν</div>
        <div class="axis-label axis-x">space</div>
        <div class="axis-label axis-t">time</div>
      </div>
    </section>

    <section class="curriculum" aria-labelledby="curriculum-title">
      <div class="curriculum-intro">
        <div>
          <p class="section-label">Contents</p>
          <h2 id="curriculum-title">The route through GR</h2>
        </div>
        <p>Chapters will be added in this order.</p>
      </div>

      <div class="stages">
        <section
          v-for="group in groups"
          :key="group.name"
          class="stage"
          :style="{ '--accent': group.color, '--accent-soft': group.soft }"
        >
          <div class="stage-marker" aria-hidden="true"><span>{{ group.number }}</span></div>
          <header class="stage-head">
            <p>{{ group.items.length }} chapters</p>
            <h3>{{ group.name }}</h3>
            <div class="stage-rule"></div>
            <p class="stage-desc">{{ group.desc }}</p>
          </header>
          <div class="cards">
            <div v-for="item in group.items" :key="item.number" class="chapter-card">
              <div class="card-topline">
                <span class="chapter-number">Chapter {{ item.number }}</span>
                <span class="chapter-symbol">{{ item.symbol }}</span>
              </div>
              <h4>{{ item.title }}</h4>
              <p>{{ item.desc }}</p>
              <span class="read-link">Coming soon</span>
            </div>
          </div>
        </section>
      </div>
    </section>
  </div>
</template>

<style>
.vp-home .vp-hero { display: none; }
.vp-home { padding: 0; max-width: none; }
.vp-home [vp-content] { max-width: none; padding: 0; }
.vp-home [vp-content] > div { max-width: none; }
.gr-home { --ink: #152238; --muted: #5f6b7c; color: var(--ink); overflow: hidden; }
.home-hero { position: relative; display: grid; grid-template-columns: minmax(0, 1fr) minmax(380px, .9fr); align-items: center; gap: clamp(2rem, 6vw, 6.5rem); max-width: 1280px; min-height: 560px; margin: 0 auto; padding: clamp(4.5rem, 8vw, 7.5rem) clamp(2rem, 6vw, 5.5rem) 4.5rem; }
.hero-copy { position: relative; z-index: 2; }
.kicker, .section-label { margin: 0; color: #2563eb; font-size: .73rem; font-weight: 750; letter-spacing: .14em; text-transform: uppercase; }
.kicker { display: flex; align-items: center; gap: .6rem; }
.kicker-dot { width: 7px; height: 7px; border-radius: 50%; background: #2563eb; box-shadow: 0 0 0 5px rgba(37, 99, 235, .12); }
.home-hero h1 { max-width: 40rem; margin: 1.25rem 0 1.35rem; color: var(--ink); font-size: clamp(3.1rem, 6vw, 5.3rem); font-weight: 700; letter-spacing: -.055em; line-height: .98; }
.hero-text { max-width: 35rem; margin: 0; color: var(--muted); font-size: clamp(1.05rem, 1.7vw, 1.3rem); line-height: 1.65; }
.hero-actions { display: flex; align-items: center; gap: 1.5rem; margin-top: 2rem; }
.start-button { display: inline-flex; align-items: center; padding: .85rem 1.1rem; border-radius: 8px; color: #fff; background: #152238; font-size: .9rem; font-weight: 650; box-shadow: 0 9px 24px rgba(21, 34, 56, .16); }
.chapter-count { color: var(--muted); font-size: .84rem; }
.chapter-count strong { color: var(--ink); font-family: Georgia, serif; font-size: 1.2rem; }
.field-visual { position: relative; width: min(100%, 500px); aspect-ratio: 1.18; justify-self: center; border: 1px solid rgba(37, 99, 235, .18); border-radius: 50% 50% 48% 52% / 43% 55% 45% 57%; background: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, .1), transparent 24%), linear-gradient(145deg, rgba(219, 234, 254, .7), rgba(238, 242, 255, .2)); transform: rotate(-2deg); }
.visual-grid { position: absolute; inset: 7%; border-radius: inherit; opacity: .35; background-image: linear-gradient(rgba(37, 99, 235, .15) 1px, transparent 1px), linear-gradient(90deg, rgba(37, 99, 235, .15) 1px, transparent 1px); background-size: 38px 38px; mask-image: radial-gradient(circle, #000 20%, transparent 72%); }
.field-lines { position: absolute; inset: 3%; width: 94%; height: 94%; stroke: #2563eb; stroke-width: 1.2; opacity: .5; }
.field-lines ellipse { stroke-dasharray: 4 7; opacity: .65; }
.visual-core { position: absolute; top: 50%; left: 52%; display: grid; place-items: center; width: 102px; height: 102px; border: 1px solid rgba(37, 99, 235, .25); border-radius: 50%; background: rgba(255, 255, 255, .8); box-shadow: 0 22px 60px rgba(37, 99, 235, .18), inset 0 0 0 8px rgba(37, 99, 235, .04); transform: translate(-50%, -50%); }
.visual-core span { margin-top: .55rem; color: #2563eb; font-family: Georgia, serif; font-size: 2.4rem; font-style: italic; line-height: 1; }
.visual-core small { align-self: start; color: var(--muted); font-size: .62rem; letter-spacing: .14em; text-transform: uppercase; }
.particle { position: absolute; width: 10px; height: 10px; border: 3px solid #fff; border-radius: 50%; background: #7c3aed; box-shadow: 0 3px 12px rgba(124, 58, 237, .4); }
.particle-a { top: 24%; left: 18%; } .particle-b { right: 14%; bottom: 29%; background: #059669; } .particle-c { right: 20%; top: 20%; width: 7px; height: 7px; background: #d97706; }
.formula { position: absolute; color: #5f6b7c; font-family: Georgia, serif; font-size: .9rem; font-style: italic; white-space: nowrap; }
.formula-a { top: 12%; right: 8%; } .formula-b { bottom: 13%; left: 7%; }
.axis-label { position: absolute; color: #7c3aed; font-size: .62rem; letter-spacing: .13em; text-transform: uppercase; } .axis-x { right: 9%; bottom: 12%; } .axis-t { top: 11%; left: 10%; }
.curriculum { max-width: 1280px; margin: 0 auto; padding: 1rem clamp(2rem, 6vw, 5.5rem) 6rem; }
.curriculum-intro { display: flex; justify-content: space-between; align-items: end; gap: 2rem; padding: 2rem 0 2.5rem; border-top: 1px solid #dfe5ec; }
.curriculum-intro h2 { margin: .45rem 0 0; font-size: clamp(2rem, 4vw, 3.25rem); letter-spacing: -.045em; } .curriculum-intro > p { max-width: 20rem; margin: 0; color: var(--muted); line-height: 1.6; }
.stage { position: relative; display: grid; grid-template-columns: 4rem minmax(170px, .28fr) 1fr; gap: 1.4rem; padding: 2.5rem 0; border-top: 1px solid #dfe5ec; }
.stage-marker { display: grid; place-items: center; width: 2.7rem; height: 2.7rem; border-radius: 50%; color: var(--accent); background: var(--accent-soft); font-size: .72rem; font-weight: 750; }
.stage-head > p:first-child { margin: .15rem 0 .45rem; color: var(--accent); font-size: .7rem; font-weight: 750; letter-spacing: .12em; text-transform: uppercase; }
.stage-head h3 { margin: 0; font-size: 1.55rem; letter-spacing: -.035em; } .stage-rule { width: 3rem; height: 3px; margin: 1rem 0; background: var(--accent); } .stage-desc { margin: 0; color: var(--muted); font-size: .9rem; line-height: 1.55; }
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: .85rem; } .chapter-card { min-height: 190px; padding: 1.15rem; border: 1px solid #dfe5ec; border-radius: 10px; background: #fff; box-shadow: 0 8px 24px rgba(21, 34, 56, .04); }
.card-topline { display: flex; justify-content: space-between; gap: .6rem; color: #8290a1; font-size: .68rem; letter-spacing: .06em; text-transform: uppercase; } .chapter-symbol { color: var(--accent); font-family: Georgia, serif; font-size: .9rem; text-transform: none; }
.chapter-card h4 { margin: 1.4rem 0 .55rem; font-size: 1.05rem; } .chapter-card p { margin: 0; color: var(--muted); font-size: .86rem; line-height: 1.55; } .read-link { display: block; margin-top: 1.2rem; color: var(--accent); font-size: .76rem; font-weight: 700; }
@media (max-width: 900px) { .home-hero { grid-template-columns: 1fr; } .field-visual { width: min(100%, 520px); } .stage { grid-template-columns: 3.5rem 1fr; } .cards { grid-column: 2; grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { .home-hero { min-height: auto; padding-top: 3.5rem; } .field-visual { width: 100%; } .curriculum-intro { display: block; } .curriculum-intro > p { margin-top: 1rem; } .stage { grid-template-columns: 2.7rem 1fr; gap: .9rem; } .cards { grid-column: 1 / -1; grid-template-columns: 1fr; } }
</style>
