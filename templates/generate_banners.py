import os
import subprocess

HTML_BANNER_A = """<!DOCTYPE html>
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
    background-color: #080a0c;
    color: #ffffff;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    position: relative;
  }

  /* Dark grid background matching user screenshot */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
  }

  /* Radial glow lights */
  .glow-lime {
    position: absolute;
    width: 600px;
    height: 400px;
    top: -100px;
    right: 150px;
    background: radial-gradient(circle, rgba(163, 230, 53, 0.12) 0%, rgba(163, 230, 53, 0.02) 50%, transparent 70%);
    pointer-events: none;
  }

  .glow-cyan {
    position: absolute;
    width: 500px;
    height: 350px;
    bottom: -150px;
    left: 200px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.08) 0%, transparent 70%);
    pointer-events: none;
  }

  .container {
    position: relative;
    width: 1584px;
    height: 396px;
    padding: 30px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }

  /* Left Main Content - positioned safe from avatar (safe zone of 280px) */
  .main-content {
    margin-left: 280px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 680px;
  }

  .top-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
  }

  .cmd-prompt {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #a3e635; /* Electric lime */
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(163, 230, 53, 0.1);
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
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .hero-title {
    font-family: 'Syne', 'Inter', sans-serif;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin-bottom: 8px;
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
    margin-bottom: 18px;
    line-height: 1.4;
  }

  /* Tool & Workflow badges bar */
  .tools-strip {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
  }

  .tool-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 5px 12px;
    background: rgba(18, 24, 27, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    color: #e2e8f0;
    letter-spacing: 0.01em;
    backdrop-filter: blur(8px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
  }

  .tool-pill.highlight {
    border-color: rgba(163, 230, 53, 0.4);
    background: rgba(163, 230, 53, 0.08);
    color: #ffffff;
  }

  .tool-pill svg {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
  }

  /* Right Side: Interactive Agent Workflow Terminal Card */
  .right-panel {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
  }

  .terminal-card {
    width: 530px;
    background: #0e1317;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8), 0 0 30px rgba(163, 230, 53, 0.06);
  }

  .terminal-header {
    background: #151c22;
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
    background: rgba(163, 230, 53, 0.1);
    padding: 2px 6px;
    border-radius: 4px;
  }

  .terminal-body {
    padding: 14px 16px;
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
  .t-purple { color: #c084fc; }
  .t-muted { color: #64748b; }
  .t-white { color: #ffffff; }

  /* Pipeline flowchart visual inside terminal */
  .workflow-pipeline {
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 10px 0 6px 0;
    padding: 8px 10px;
    background: rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.06);
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

  /* Bottom CTA row */
  .bottom-actions {
    display: flex;
    align-items: center;
    gap: 12px;
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
    padding: 8px 20px;
    border-radius: 6px;
    letter-spacing: -0.01em;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(163, 230, 53, 0.35);
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

  <div class="container">
    <!-- Left Main Content Area -->
    <div class="main-content">
      <div class="top-meta">
        <div class="cmd-prompt">
          <span>amir@design-core:~$</span>
          <span style="color:#ffffff;">cat workflow.ts</span>
        </div>
        <div class="status-badge">
          <div class="pulse-dot"></div>
          <span>AUTONOMOUS AGENTS ACTIVE</span>
        </div>
      </div>

      <div class="role-tag">// AMIR NIAZI — DESIGN ENGINEER</div>
      
      <div class="hero-title">
        CODE THAT <span class="accent">CONVERTS</span>
      </div>

      <div class="hero-subtitle">
        FROM FIGMA SPECS TO PRODUCTION AI AGENTS • VIBE CODING AT 10X SPEED
      </div>

      <!-- Frontier Tools & Vibe Coding Strip -->
      <div class="tools-strip">
        <!-- Claude -->
        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#D97706">
            <path d="M12 2L14.2 8.8L21 9.5L16 14.2L17.5 21L12 17.5L6.5 21L8 14.2L3 9.5L9.8 8.8L12 2Z"/>
          </svg>
          <span>Claude 3.7</span>
        </div>

        <!-- OpenAI -->
        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#10a37f">
            <circle cx="12" cy="12" r="9" stroke="#10a37f" stroke-width="2" fill="none"/>
            <circle cx="12" cy="12" r="3" fill="#10a37f"/>
          </svg>
          <span>OpenAI o3 / GPT-4o</span>
        </div>

        <!-- Antigravity -->
        <div class="tool-pill highlight">
          <svg viewBox="0 0 24 24" fill="#a3e635">
            <path d="M12 2L2 22H7L12 12L17 22H22L12 2Z"/>
            <circle cx="12" cy="8" r="2.5" fill="#38bdf8"/>
          </svg>
          <span>Google Antigravity</span>
        </div>

        <!-- Figma -->
        <div class="tool-pill">
          <svg viewBox="0 0 38 57" fill="none">
            <path d="M19 28.5C19 23.2533 23.2533 19 28.5 19C33.7467 19 38 23.2533 38 28.5C38 33.7467 33.7467 38 28.5 38C23.2533 38 19 33.7467 19 28.5Z" fill="#1ABCFE"/>
            <path d="M0 47.5C0 42.2533 4.25329 38 9.5 38H19V47.5C19 52.7467 14.7467 57 9.5 57C4.25329 57 0 52.7467 0 47.5Z" fill="#0ACF83"/>
            <path d="M19 0V19H28.5C33.7467 19 38 14.7467 38 9.5C38 4.25329 33.7467 0 28.5 0H19Z" fill="#FF7262"/>
            <path d="M0 9.5C0 14.7467 4.25329 19 9.5 19H19V0H9.5C4.25329 0 0 4.25329 0 9.5Z" fill="#F24E1E"/>
            <path d="M0 28.5C0 33.7467 4.25329 38 9.5 38H19V19H9.5C4.25329 19 0 23.2533 0 28.5Z" fill="#A259FF"/>
          </svg>
          <span>Figma</span>
        </div>

        <!-- Cursor / Vibe Tools -->
        <div class="tool-pill">
          <svg viewBox="0 0 24 24" fill="#60a5fa">
            <polygon points="12,2 22,8 22,16 12,22 2,16 2,8" stroke="#60a5fa" stroke-width="2" fill="rgba(96,165,250,0.2)"/>
          </svg>
          <span>Cursor AI</span>
        </div>

        <!-- v0 / Lovable -->
        <div class="tool-pill">
          <svg viewBox="0 0 24 24" fill="#ffffff">
            <path d="M12 3L2 21H22L12 3Z"/>
          </svg>
          <span>v0 & Bolt</span>
        </div>

        <!-- MCP / Agent Swarms -->
        <div class="tool-pill">
          <span style="color:#a3e635; font-size:14px;">⚡</span>
          <span>MCP & Agent Swarms</span>
        </div>
      </div>
    </div>

    <!-- Right Side: Terminal Execution HUD -->
    <div class="right-panel">
      <div class="terminal-card">
        <div class="terminal-header">
          <div class="traffic-lights">
            <div class="light red"></div>
            <div class="light yellow"></div>
            <div class="light green"></div>
          </div>
          <div class="terminal-title">agent_orchestrator.ts</div>
          <div class="terminal-tag">LIVE HUD</div>
        </div>

        <div class="terminal-body">
          <div class="terminal-line">
            <span class="t-green">$</span>
            <span class="t-white">agent.init({</span>
            <span class="t-muted">stack:</span>
            <span class="t-cyan">["Claude", "OpenAI", "AGY"]</span>
            <span class="t-white">})</span>
          </div>

          <!-- Flowchart Pipeline -->
          <div class="workflow-pipeline">
            <div class="wf-step figma">🎨 Figma UI/UX</div>
            <div class="wf-arrow">➔</div>
            <div class="wf-step agents">⚡ Vibe + Agent Swarm</div>
            <div class="wf-arrow">➔</div>
            <div class="wf-step prod">🚀 Prod App</div>
          </div>

          <div class="terminal-line" style="margin-top: 6px;">
            <span class="t-muted">▶ Protocol:</span>
            <span class="t-white">Model Context Protocol (MCP)</span>
            <span class="t-green">✔ CONNECTED</span>
          </div>
          <div class="terminal-line">
            <span class="t-muted">▶ Velocity:</span>
            <span class="t-white">Vibe Coding Workflows</span>
            <span class="t-cyan">⚡ 10x Velocity</span>
          </div>
        </div>
      </div>

      <!-- Action Button / Domain -->
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

os.makedirs("/Users/nael/Desktop/Amir/githubcover/templates", exist_ok=True)
with open("/Users/nael/Desktop/Amir/githubcover/templates/banner_a.html", "w") as f:
    f.write(HTML_BANNER_A)

print("Template banner_a.html written successfully")
