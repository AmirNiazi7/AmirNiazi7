import os
import subprocess
import shutil

OUTPUT_DIR = "/Users/nael/Desktop/Amir/githubcover/assets"
TEMPLATES_DIR = "/Users/nael/Desktop/Amir/githubcover/templates"
ARTIFACTS_DIR = "/Users/nael/.gemini/antigravity-ide/brain/8ff77638-874e-4f02-9d9d-acc520b47b4f"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# -------------------------------------------------------------
# Template A: Neon Terminal Matrix (Amir Niazi — Design Engineer)
# -------------------------------------------------------------
HTML_A = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=Syne:wght@700;800&family=Inter:wght@400;500;600;700&display=swap');

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
  }

  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background-color: #07090b;
    color: #ffffff;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    position: relative;
  }

  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
    background-size: 36px 36px;
    pointer-events: none;
  }

  .glow-lime {
    position: absolute;
    width: 650px;
    height: 450px;
    top: -120px;
    right: 180px;
    background: radial-gradient(circle, rgba(163, 230, 53, 0.14) 0%, rgba(163, 230, 53, 0.02) 55%, transparent 70%);
    pointer-events: none;
  }

  .glow-cyan {
    position: absolute;
    width: 500px;
    height: 350px;
    bottom: -150px;
    left: 260px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.09) 0%, transparent 70%);
    pointer-events: none;
  }

  .top-telemetry {
    position: absolute;
    top: 24px;
    left: 48px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #64748b;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 16px;
    z-index: 5;
  }

  .top-telemetry span.active {
    color: #a3e635;
  }

  .container {
    position: relative;
    width: 1584px;
    height: 396px;
    padding: 38px 48px 30px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }

  .main-content {
    margin-left: 285px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 690px;
  }

  .top-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
  }

  .cmd-prompt {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #a3e635;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(163, 230, 53, 0.08);
    border: 1px solid rgba(163, 230, 53, 0.3);
    padding: 3px 10px;
    border-radius: 999px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #bef264;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .pulse-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: #a3e635;
    box-shadow: 0 0 8px #a3e635;
  }

  .role-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    color: #a3e635;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
  }

  .hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 45px;
    font-weight: 800;
    line-height: 1.02;
    letter-spacing: -0.035em;
    color: #ffffff;
    margin-bottom: 6px;
    text-transform: uppercase;
  }

  .hero-title span.accent {
    color: #a3e635;
    background: linear-gradient(135deg, #a3e635 0%, #4ade80 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .hero-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #94a3b8;
    letter-spacing: 0.02em;
    margin-bottom: 16px;
    line-height: 1.4;
  }

  .tools-strip {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 7px;
  }

  .tool-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 5px 11px;
    background: rgba(18, 24, 28, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 7px;
    font-size: 12px;
    font-weight: 600;
    color: #e2e8f0;
    letter-spacing: 0.01em;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
  }

  .tool-pill.highlight {
    border-color: rgba(163, 230, 53, 0.45);
    background: rgba(163, 230, 53, 0.08);
    color: #ffffff;
  }

  .tool-pill svg {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
  }

  .right-panel {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
  }

  .terminal-card {
    width: 535px;
    background: #0d1216;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.85), 0 0 35px rgba(163, 230, 53, 0.07);
  }

  .terminal-header {
    background: #141b21;
    padding: 9px 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .traffic-lights {
    display: flex;
    gap: 6px;
  }

  .light {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }

  .light.red { background: #ff5f56; }
  .light.yellow { background: #ffbd2e; }
  .light.green { background: #27c93f; }

  .terminal-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
    letter-spacing: 0.04em;
  }

  .terminal-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #a3e635;
    background: rgba(163, 230, 53, 0.12);
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 700;
  }

  .terminal-body {
    padding: 13px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 1.6;
    color: #e2e8f0;
  }

  .terminal-line {
    display: flex;
    align-items: baseline;
    gap: 8px;
    margin-bottom: 4px;
  }

  .t-green { color: #a3e635; font-weight: 700; }
  .t-cyan { color: #38bdf8; }
  .t-muted { color: #64748b; }
  .t-white { color: #ffffff; }

  .workflow-pipeline {
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 8px 0 6px 0;
    padding: 8px 10px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
  }

  .wf-step {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 5px;
    background: #1a2228;
    color: #f1f5f9;
  }

  .wf-step.figma { border-left: 3px solid #ff7262; }
  .wf-step.agents { border-left: 3px solid #a3e635; color: #a3e635; }
  .wf-step.prod { border-left: 3px solid #38bdf8; color: #38bdf8; }

  .wf-arrow {
    color: #64748b;
    font-size: 10px;
  }

  .bottom-actions {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .cta-button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #a3e635;
    color: #090d0b;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 800;
    padding: 8px 22px;
    border-radius: 6px;
    letter-spacing: -0.01em;
    box-shadow: 0 4px 18px rgba(163, 230, 53, 0.4);
  }

  .badge-metric {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
    display: flex;
    align-items: center;
    gap: 6px;
  }
</style>
</head>
<body>
  <div class="grid-bg"></div>
  <div class="glow-lime"></div>
  <div class="glow-cyan"></div>

  <div class="top-telemetry">
    <span>SYSTEM: <span class="active">AI-DESIGN-RUNNER // v3.8</span></span>
    <span>ENGINEER: <span class="active">AMIR NIAZI</span></span>
    <span>ROLE: <span class="active">DESIGN ENGINEER</span></span>
  </div>

  <div class="container">
    <div class="main-content">
      <div class="top-meta">
        <div class="cmd-prompt">
          <span>amir@design-core:~$</span>
          <span style="color:#ffffff;">cat workflow.ts</span>
        </div>
        <div class="status-badge">
          <div class="pulse-dot"></div>
          <span>AGENTS ACTIVE</span>
        </div>
      </div>

      <div class="role-tag">// AMIR NIAZI — DESIGN ENGINEER</div>
      
      <div class="hero-title">
        CODE THAT <span class="accent">CONVERTS</span>
      </div>

      <div class="hero-subtitle">
        FROM FIGMA SPECS TO PRODUCTION AI AGENTS • VIBE CODING AT 10X SPEED
      </div>

      <div class="tools-strip">
        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#D97706">
            <path d="M12 2L14.2 8.8L21 9.5L16 14.2L17.5 21L12 17.5L6.5 21L8 14.2L3 9.5L9.8 8.8L12 2Z"/>
          </svg>
          <span>Claude 3.7</span>
        </div>

        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#10a37f">
            <circle cx="12" cy="12" r="9" stroke="#10a37f" stroke-width="2" fill="none"/>
            <circle cx="12" cy="12" r="3" fill="#10a37f"/>
          </svg>
          <span>OpenAI o3 / GPT-4o</span>
        </div>

        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#a3e635">
            <path d="M12 2L2 22H7L12 12L17 22H22L12 2Z"/>
            <circle cx="12" cy="8" r="2.5" fill="#38bdf8"/>
          </svg>
          <span>Antigravity (AGY)</span>
        </div>

        <div class="tool-pill">
          <svg viewBox="0 0 38 57" fill="none">
            <path d="M19 28.5C19 23.2533 23.2533 19 28.5 19C33.7467 19 38 23.2533 38 28.5C38 33.7467 33.7467 38 28.5 38C23.2533 38 19 33.7467 19 28.5Z" fill="#1ABCFE"/>
            <path d="M0 47.5C0 42.2533 4.25329 38 9.5 38H19V47.5C19 52.7467 14.7467 57 9.5 57C4.25329 57 0 52.7467 0 47.5Z" fill="#0ACF83"/>
            <path d="M19 0V19H28.5C33.7467 19 38 14.7467 38 9.5C38 4.25329 33.7467 0 28.5 0H19Z" fill="#FF7262"/>
            <path d="M0 9.5C0 14.7467 4.25329 19 9.5 19H19V0H9.5C4.25329 0 0 4.25329 0 9.5Z" fill="#F24E1E"/>
            <path d="M0 28.5C0 33.7467 4.25329 38 9.5 38H19V19H9.5C4.25329 19 0 23.2533 0 28.5Z" fill="#A259FF"/>
          </svg>
          <span>Figma UI/UX</span>
        </div>

        <div class="tool-pill">
          <svg viewBox="0 0 24 24" fill="#60a5fa">
            <polygon points="12,2 22,8 22,16 12,22 2,16 2,8" stroke="#60a5fa" stroke-width="2" fill="rgba(96,165,250,0.2)"/>
          </svg>
          <span>Cursor AI</span>
        </div>

        <div class="tool-pill">
          <svg viewBox="0 0 24 24" fill="#ffffff">
            <path d="M12 3L2 21H22L12 3Z"/>
          </svg>
          <span>v0 & Lovable</span>
        </div>

        <div class="tool-pill">
          <span style="color:#a3e635; font-size:14px;">⚡</span>
          <span>MCP Protocol</span>
        </div>
      </div>
    </div>

    <div class="right-panel">
      <div class="terminal-card">
        <div class="terminal-header">
          <div class="traffic-lights">
            <div class="light red"></div>
            <div class="light yellow"></div>
            <div class="light green"></div>
          </div>
          <div class="terminal-title">amir_niazi.ts</div>
          <div class="terminal-tag">LIVE HUD</div>
        </div>

        <div class="terminal-body">
          <div class="terminal-line">
            <span class="t-green">$</span>
            <span class="t-white">design_engineer.init({</span>
            <span class="t-muted">stack:</span>
            <span class="t-cyan">["Figma", "Claude", "AGY"]</span>
            <span class="t-white">})</span>
          </div>

          <div class="workflow-pipeline">
            <div class="wf-step figma">🎨 Figma Design</div>
            <div class="wf-arrow">➔</div>
            <div class="wf-step agents">⚡ Vibe + Agent Swarm</div>
            <div class="wf-arrow">➔</div>
            <div class="wf-step prod">🚀 Prod App</div>
          </div>

          <div class="terminal-line" style="margin-top: 6px;">
            <span class="t-muted">▶ Speciality:</span>
            <span class="t-white">Amir Niazi — Design Engineer</span>
            <span class="t-green">✔ VERIFIED</span>
          </div>
          <div class="terminal-line">
            <span class="t-muted">▶ Velocity:</span>
            <span class="t-white">Autonomous Agent Loop</span>
            <span class="t-cyan">⚡ 10x Velocity</span>
          </div>
        </div>
      </div>

      <div class="bottom-actions">
        <div class="badge-metric">
          <span style="color:#a3e635;">●</span>
          <span>OPEN FOR HIGH-IMPACT PROJECTS</span>
        </div>
        <div class="cta-button">
          <span>Amir Niazi</span>
          <span>→</span>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# Template B: Cyber Spatial & Neural Architecture (Amir Niazi)
# -------------------------------------------------------------
HTML_B = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
  }

  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background: #06080d;
    color: #ffffff;
    font-family: 'Plus Jakarta Sans', sans-serif;
    position: relative;
  }

  .ambient-mesh {
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(circle at 15% 50%, rgba(99, 102, 241, 0.15) 0%, transparent 45%),
      radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.18) 0%, transparent 40%),
      radial-gradient(circle at 55% 80%, rgba(56, 189, 248, 0.12) 0%, transparent 50%),
      linear-gradient(180deg, rgba(6, 8, 13, 0.6) 0%, #06080d 100%);
  }

  .grid-overlay {
    position: absolute;
    inset: 0;
    background-image: 
      radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
    background-size: 24px 24px;
    opacity: 0.7;
  }

  .container {
    position: relative;
    width: 1584px;
    height: 396px;
    padding: 34px 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }

  .hero-block {
    margin-left: 285px;
    max-width: 680px;
  }

  .status-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 14px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.35);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: #34d399;
    letter-spacing: 0.06em;
    margin-bottom: 12px;
  }

  .pulse-indicator {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
  }

  .hero-headline {
    font-size: 46px;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.03em;
    margin-bottom: 10px;
    background: linear-gradient(180deg, #FFFFFF 20%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .hero-headline span.gradient-text {
    background: linear-gradient(90deg, #38bdf8 0%, #34d399 50%, #a3e635 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .hero-desc {
    font-size: 14px;
    color: #94a3b8;
    line-height: 1.5;
    margin-bottom: 20px;
  }

  .tech-cards-row {
    display: flex;
    gap: 10px;
    align-items: center;
  }

  .glass-card {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 7px 14px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(12px);
    font-size: 13px;
    font-weight: 600;
    color: #f1f5f9;
  }

  .glass-card.glow-border {
    border-color: rgba(56, 189, 248, 0.45);
    background: rgba(56, 189, 248, 0.08);
  }

  .orchestration-hud {
    width: 530px;
    background: rgba(13, 17, 23, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(56, 189, 248, 0.1);
  }

  .hud-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .hud-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .nodes-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 14px;
  }

  .node-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 9px 10px;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .node-box.active {
    border-color: rgba(52, 211, 153, 0.4);
    background: rgba(16, 185, 129, 0.08);
  }

  .node-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #64748b;
  }

  .node-name {
    font-size: 12px;
    font-weight: 700;
    color: #ffffff;
  }

  .hud-stats {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
  }

  .cta-pill {
    background: linear-gradient(135deg, #38bdf8 0%, #34d399 100%);
    color: #04121a;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 800;
    padding: 6px 16px;
    border-radius: 999px;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3);
  }
</style>
</head>
<body>
  <div class="ambient-mesh"></div>
  <div class="grid-overlay"></div>

  <div class="container">
    <div class="hero-block">
      <div class="status-tag">
        <div class="pulse-indicator"></div>
        <span>AMIR NIAZI // DESIGN ENGINEER</span>
      </div>

      <h1 class="hero-headline">
        Architecting <span class="gradient-text">Autonomous</span><br/>Design Systems & AI Workflows
      </h1>

      <p class="hero-desc">
        Amir Niazi — Design Engineer • Model Context Protocol • Figma to Code at Velocity
      </p>

      <div class="tech-cards-row">
        <div class="glass-card glow-border">
          <span style="color:#f59e0b;">✦</span>
          <span>Claude 3.7</span>
        </div>
        <div class="glass-card glow-border">
          <span style="color:#10b981;">✦</span>
          <span>OpenAI o3 / GPT-4o</span>
        </div>
        <div class="glass-card glow-border">
          <span style="color:#38bdf8;">✦</span>
          <span>Antigravity</span>
        </div>
        <div class="glass-card">
          <span>🎨 Figma UI</span>
        </div>
        <div class="glass-card">
          <span>⚡ Cursor / v0</span>
        </div>
      </div>
    </div>

    <div class="orchestration-hud">
      <div class="hud-header">
        <div class="hud-title">
          <span style="color:#34d399;">●</span>
          <span>DESIGN ENGINEERING PIPELINE</span>
        </div>
        <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#38bdf8;">AMIR NIAZI</span>
      </div>

      <div class="nodes-grid">
        <div class="node-box">
          <div class="node-label">01 // DESIGN</div>
          <div class="node-name">Figma Systems</div>
        </div>
        <div class="node-box active">
          <div class="node-label">02 // BRAIN</div>
          <div class="node-name">Claude & OpenAI</div>
        </div>
        <div class="node-box active">
          <div class="node-label">03 // AGENT</div>
          <div class="node-name">Google Antigravity</div>
        </div>
        <div class="node-box active">
          <div class="node-label">04 // TOOLS</div>
          <div class="node-name">MCP Protocol</div>
        </div>
        <div class="node-box">
          <div class="node-label">05 // VELOCITY</div>
          <div class="node-name">Vibe IDE (Cursor)</div>
        </div>
        <div class="node-box">
          <div class="node-label">06 // DEPLOY</div>
          <div class="node-name">Production App</div>
        </div>
      </div>

      <div class="hud-stats">
        <span>STATUS: DESIGN ENGINEER VERIFIED</span>
        <a class="cta-pill" href="#">Amir Niazi ↗</a>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# Template C: Minimalist Monochrome & Swiss Grid (Amir Niazi — Design Engineer)
# -------------------------------------------------------------
HTML_C = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
  }

  body {
    width: 1584px;
    height: 396px;
    overflow: hidden;
    background: #090a0f;
    color: #ffffff;
    font-family: 'Space Grotesk', sans-serif;
    position: relative;
  }

  .grid-pattern {
    position: absolute;
    inset: 0;
    background-size: 40px 40px;
    background-image:
      linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
  }

  .container {
    position: relative;
    width: 1584px;
    height: 396px;
    padding: 40px 52px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }

  .hero {
    margin-left: 285px;
    max-width: 700px;
  }

  .subhead-mono {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    color: #a3e635;
    letter-spacing: 0.12em;
    margin-bottom: 12px;
  }

  .headline {
    font-size: 48px;
    font-weight: 700;
    line-height: 1.04;
    letter-spacing: -0.04em;
    margin-bottom: 14px;
  }

  .tagline {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.6;
    margin-bottom: 18px;
  }

  .tagline b {
    color: #ffffff;
  }

  .badges {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }

  .badge {
    padding: 5px 12px;
    background: #141721;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #cbd5e1;
  }

  .badge.active {
    border-color: #a3e635;
    color: #a3e635;
    background: rgba(163, 230, 53, 0.08);
  }

  .arch-panel {
    width: 520px;
    background: #0f121a;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .arch-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .arch-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
  }

  .arch-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 7px 10px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 6px;
  }

  .arch-item .key {
    color: #94a3b8;
  }

  .arch-item .val {
    color: #a3e635;
    font-weight: 700;
  }

  .arch-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
  }

  .arch-btn {
    background: #ffffff;
    color: #000000;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 800;
    padding: 8px 18px;
    border-radius: 6px;
    text-decoration: none;
  }
</style>
</head>
<body>
  <div class="grid-pattern"></div>

  <div class="container">
    <div class="hero">
      <div class="subhead-mono">// AMIR NIAZI — DESIGN ENGINEER</div>
      <h1 class="headline">DESIGNING INTELLIGENCE.<br/>ENGINEERING EXPERIENCE.</h1>
      <p class="tagline">
        Bridging <b>Figma Design Systems</b> with <b>Autonomous Agent Workflows</b>.<br/>
        Design Engineering powered by Claude 3.7, OpenAI, and Google Antigravity.
      </p>

      <div class="badges">
        <span class="badge active">Claude 3.7</span>
        <span class="badge active">OpenAI o3</span>
        <span class="badge active">Google Antigravity</span>
        <span class="badge">Figma</span>
        <span class="badge">Cursor AI</span>
        <span class="badge">v0 / Lovable</span>
        <span class="badge">MCP Swarms</span>
      </div>
    </div>

    <div class="arch-panel">
      <div class="arch-header">
        <span>AMIR NIAZI // DESIGN ENGINEER</span>
        <span style="color:#a3e635;">● 100% OPERATIONAL</span>
      </div>

      <div class="arch-list">
        <div class="arch-item">
          <span class="key">Role:</span>
          <span class="val">Amir Niazi — Design Engineer</span>
        </div>
        <div class="arch-item">
          <span class="key">Agentic Intelligence:</span>
          <span class="val">Claude + OpenAI + Antigravity</span>
        </div>
        <div class="arch-item">
          <span class="key">Tooling / MCP:</span>
          <span class="val">Model Context Protocol</span>
        </div>
        <div class="arch-item">
          <span class="key">Design-to-Code:</span>
          <span class="val">Figma Tokens ➔ Production UI</span>
        </div>
      </div>

      <div class="arch-footer">
        <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#64748b;">AMIR NIAZI</span>
        <a class="arch-btn" href="#">Amir Niazi →</a>
      </div>
    </div>
  </div>
</body>
</html>
"""

with open(f"{TEMPLATES_DIR}/banner_a.html", "w") as f:
    f.write(HTML_A)
with open(f"{TEMPLATES_DIR}/banner_b.html", "w") as f:
    f.write(HTML_B)
with open(f"{TEMPLATES_DIR}/banner_c.html", "w") as f:
    f.write(HTML_C)

print("Updated banner HTML templates for Amir Niazi — Design Engineer.")
