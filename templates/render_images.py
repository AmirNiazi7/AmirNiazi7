import os
import subprocess

TEMPLATES = [
    ("templates/banner_a.html", "assets/linkedin_banner_neon.png", "assets/linkedin_banner_neon_retina.png"),
    ("templates/banner_b.html", "assets/linkedin_banner_cyber.png", "assets/linkedin_banner_cyber_retina.png"),
    ("templates/banner_c.html", "assets/linkedin_banner_minimal.png", "assets/linkedin_banner_minimal_retina.png")
]

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

for tpl, out_1x, out_2x in TEMPLATES:
    file_url = f"file://{os.path.abspath(tpl)}"
    print(f"Rendering {out_1x}...")
    cmd_1x = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=2000",
        "--window-size=1584,396",
        f"--screenshot={out_1x}",
        file_url
    ]
    subprocess.run(cmd_1x, capture_output=True)

    print(f"Rendering {out_2x} (2x Retina)...")
    cmd_2x = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=2000",
        "--window-size=1584,396",
        "--force-device-scale-factor=2",
        f"--screenshot={out_2x}",
        file_url
    ]
    subprocess.run(cmd_2x, capture_output=True)

print("Render complete! Checking file sizes:")
for _, out_1x, out_2x in TEMPLATES:
    s1 = os.path.getsize(out_1x) // 1024 if os.path.exists(out_1x) else 0
    s2 = os.path.getsize(out_2x) // 1024 if os.path.exists(out_2x) else 0
    print(f"{out_1x}: {s1} KB | {out_2x}: {s2} KB")
