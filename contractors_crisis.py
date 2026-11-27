import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import math
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(page_title="Contractor's Crisis", page_icon="🚧", layout="centered")

# --- VISUAL FORMULA SHEET GENERATOR ---
@st.cache_data
def generate_formula_sheet():
    fig, axes = plt.subplots(3, 4, figsize=(12, 8.5))
    fig.patch.set_facecolor('#102538')
    
    for ax in axes.flat:
        ax.set_facecolor('#16324a')
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor('#3a6ea5')
            spine.set_linewidth(1.5)

    # --- ROW 1: 2D AREA FORMULAS ---
    # 1. Circle
    ax = axes[0, 0]
    c = patches.Circle((0.5, 0.58), 0.25, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(c)
    ax.plot([0.5, 0.75], [0.58, 0.58], color='#ffcc00', lw=2)
    ax.text(0.625, 0.63, "r", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("CIRCLE AREA", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.14, "A = π · r²", color='white', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 2. Parallelogram / Rectangle
    ax = axes[0, 1]
    p = patches.Polygon([(0.2, 0.35), (0.75, 0.35), (0.85, 0.8), (0.3, 0.8)], closed=True, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(p)
    ax.plot([0.3, 0.3], [0.35, 0.8], color='#ffcc00', ls='--', lw=1.5)
    ax.text(0.52, 0.23, "b", color='white', ha='center', fontweight='bold', fontsize=10)
    ax.text(0.24, 0.57, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("PARALLELOGRAM", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.1, "A = b · h", color='white', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 3. Triangle
    ax = axes[0, 2]
    t = patches.Polygon([(0.2, 0.35), (0.8, 0.35), (0.55, 0.82)], closed=True, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(t)
    ax.plot([0.55, 0.55], [0.35, 0.82], color='#ffcc00', ls='--', lw=1.5)
    ax.text(0.5, 0.23, "b", color='white', ha='center', fontweight='bold', fontsize=10)
    ax.text(0.61, 0.57, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("TRIANGLE AREA", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.1, "A = ½ · b · h", color='white', ha='center', va='center', fontsize=11, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 4. Trapezoid
    ax = axes[0, 3]
    tr = patches.Polygon([(0.18, 0.35), (0.82, 0.35), (0.68, 0.8), (0.32, 0.8)], closed=True, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(tr)
    ax.plot([0.32, 0.32], [0.35, 0.8], color='#ffcc00', ls='--', lw=1.5)
    ax.text(0.5, 0.84, "b₁", color='white', ha='center', fontweight='bold', fontsize=9)
    ax.text(0.5, 0.23, "b₂", color='white', ha='center', fontweight='bold', fontsize=9)
    ax.text(0.25, 0.57, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("TRAPEZOID AREA", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.1, "A = ½(b₁ + b₂) · h", color='white', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # --- ROW 2: 3D VOLUME FORMULAS ---
    # 5. Prism (Rectangular & General)
    ax = axes[1, 0]
    front = patches.Rectangle((0.22, 0.32), 0.42, 0.42, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(front)
    ax.plot([0.22, 0.36], [0.74, 0.86], color='white', lw=1.5)
    ax.plot([0.64, 0.78], [0.74, 0.86], color='white', lw=1.5)
    ax.plot([0.64, 0.78], [0.32, 0.44], color='white', lw=1.5)
    ax.plot([0.36, 0.78], [0.86, 0.86], color='white', lw=1.5)
    ax.plot([0.78, 0.78], [0.44, 0.86], color='white', lw=1.5)
    ax.text(0.43, 0.53, "Base
Area (B)", color='#ffcc00', ha='center', va='center', fontsize=8, fontweight='bold')
    ax.text(0.84, 0.65, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("PRISM VOLUME", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.13, "V = B · h
(Rect: l · w · h)", color='white', ha='center', va='center', fontsize=9.5, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 6. Pyramid
    ax = axes[1, 1]
    base_pyr = patches.Polygon([(0.2, 0.35), (0.65, 0.35), (0.8, 0.5), (0.35, 0.5)], closed=True, edgecolor='white', facecolor='#2b547e', lw=1.5)
    ax.add_patch(base_pyr)
    apex = (0.5, 0.85)
    for pt in [(0.2, 0.35), (0.65, 0.35), (0.8, 0.5)]:
        ax.plot([pt[0], apex[0]], [pt[1], apex[1]], color='white', lw=1.8)
    ax.plot([0.35, apex[0]], [0.5, apex[1]], color='white', ls=':', lw=1.2)
    ax.plot([0.5, 0.5], [0.42, 0.85], color='#ffcc00', ls='--', lw=1.5)
    ax.text(0.55, 0.62, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("PYRAMID VOLUME", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.13, "V = ⅓ · B · h", color='white', ha='center', va='center', fontsize=10.5, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 7. Cylinder
    ax = axes[1, 2]
    cyl_r = patches.Rectangle((0.32, 0.35), 0.36, 0.42, edgecolor='white', facecolor='#2b547e', lw=1.8)
    top_e = patches.Ellipse((0.5, 0.77), 0.36, 0.12, edgecolor='white', facecolor='#3a6ea5', lw=1.8)
    bot_e = patches.Ellipse((0.5, 0.35), 0.36, 0.12, edgecolor='white', ls='--', facecolor='none', lw=1.5)
    ax.add_patch(cyl_r); ax.add_patch(bot_e); ax.add_patch(top_e)
    ax.plot([0.5, 0.68], [0.77, 0.77], color='#ffcc00', lw=1.8)
    ax.text(0.59, 0.82, "r", color='#ffcc00', ha='center', fontweight='bold', fontsize=9)
    ax.text(0.75, 0.56, "h", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("CYLINDER VOLUME", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.13, "V = π · r² · h", color='white', ha='center', va='center', fontsize=10.5, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 8. Sphere
    ax = axes[1, 3]
    sph = patches.Circle((0.5, 0.56), 0.25, edgecolor='white', facecolor='#2b547e', lw=2)
    eq = patches.Ellipse((0.5, 0.56), 0.5, 0.14, edgecolor='white', ls='--', facecolor='none', lw=1.3)
    ax.add_patch(sph); ax.add_patch(eq)
    ax.plot([0.5, 0.75], [0.56, 0.56], color='#ffcc00', lw=2)
    ax.text(0.62, 0.62, "r", color='#ffcc00', ha='center', fontweight='bold', fontsize=10)
    ax.set_title("SPHERE VOLUME", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.13, "V = (4/3) · π · r³", color='white', ha='center', va='center', fontsize=10.5, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # --- ROW 3: RIGHT TRIANGLE TRIGONOMETRY & REFLECTION ---
    # 9. Right Triangle Labels
    ax = axes[2, 0]
    rt = patches.Polygon([(0.2, 0.32), (0.8, 0.32), (0.8, 0.8)], closed=True, edgecolor='white', facecolor='#2b547e', lw=2)
    ax.add_patch(rt)
    ax.add_patch(patches.Rectangle((0.73, 0.32), 0.07, 0.07, edgecolor='white', facecolor='none', lw=1.2))
    ax.text(0.35, 0.36, "θ", color='#ffcc00', fontweight='bold', fontsize=11)
    ax.text(0.5, 0.22, "Adjacent", color='white', ha='center', fontsize=8.5, fontweight='bold')
    ax.text(0.89, 0.56, "Opp", color='white', ha='center', rotation=270, fontsize=8.5, fontweight='bold')
    ax.text(0.45, 0.62, "Hyp", color='#ffcc00', ha='center', rotation=38, fontsize=8.5, fontweight='bold')
    ax.set_title("RIGHT TRIANGLE", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.1, "SOH - CAH - TOA", color='#ffcc00', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 10. Sine
    ax = axes[2, 1]
    ax.set_title("SINE (SOH)", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.55, "sin(θ) = Opposite / Hypotenuse", color='white', ha='center', va='center', fontsize=9.5, fontweight='bold')
    ax.text(0.5, 0.25, "Use when finding or using
Opposite & Hypotenuse", color='#a8d0e6', ha='center', va='center', fontsize=8.5)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 11. Cosine
    ax = axes[2, 2]
    ax.set_title("COSINE (CAH)", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.55, "cos(θ) = Adjacent / Hypotenuse", color='white', ha='center', va='center', fontsize=9.5, fontweight='bold')
    ax.text(0.5, 0.25, "Use when finding or using
Adjacent & Hypotenuse", color='#a8d0e6', ha='center', va='center', fontsize=8.5)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    # 12. Tangent & Reflection
    ax = axes[2, 3]
    ax.set_title("TANGENT & REFLECTION", color='#ffcc00', fontsize=10, fontweight='bold', pad=4)
    ax.text(0.5, 0.62, "tan(θ) = Opposite / Adjacent", color='white', ha='center', va='center', fontsize=9.5, fontweight='bold')
    ax.text(0.5, 0.25, "Reflection: Angle In = Angle Out
(Keep calculator in DEGREE mode!)", color='#ffcc00', ha='center', va='center', fontsize=8.5, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    plt.tight_layout(pad=1.0)
    return fig


# --- BLUEPRINT GENERATORS ---
def draw_composite_floor(w1, h1, w2, h2):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    total_h = h1 + h2
    coords = [(0, 0), (w1, 0), (w1, h1), (w2, h1), (w2, total_h), (0, total_h)]
    poly = patches.Polygon(coords, closed=True, edgecolor='white', facecolor='#2b547e', linewidth=2)
    ax.add_patch(poly)
    
    ax.text(w1 / 2, -total_h * 0.08, f"{w1} ft", color='white', ha='center', fontweight='bold')
    ax.text(-w1 * 0.08, total_h / 2, f"{total_h} ft", color='white', va='center', rotation=90, fontweight='bold')
    ax.text(w2 / 2, total_h + total_h * 0.04, f"{w2} ft", color='white', ha='center', fontweight='bold')
    ax.text(w1 + w1 * 0.05, h1 / 2, f"{h1} ft", color='white', va='center', rotation=270, fontweight='bold')
    
    ax.set_xlim(-w1 * 0.2, w1 * 1.2)
    ax.set_ylim(-total_h * 0.2, total_h * 1.2)
    ax.axis('off')
    ax.set_title("BLUEPRINT: L-SHAPED ROOM FLOORPLAN", color='white', pad=8)
    return fig

def draw_cylinder_piers(diam, depth, qty):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rect = patches.Rectangle((3.5, 2), 3, 7, edgecolor='white', facecolor='#2b547e', linewidth=2)
    top_e = patches.Ellipse((5, 9), 3, 1, edgecolor='white', facecolor='#3a6ea5', linewidth=2)
    bot_e = patches.Ellipse((5, 2), 3, 1, edgecolor='white', linestyle='--', facecolor='none', linewidth=1.5)
    ax.add_patch(rect)
    ax.add_patch(bot_e)
    ax.add_patch(top_e)
    
    ax.plot([3.5, 6.5], [9, 9], color='#ffcc00', linestyle=':', linewidth=2)
    ax.text(5, 10.1, f"Diameter = {diam} ft", color='#ffcc00', ha='center', fontweight='bold')
    ax.text(7.2, 5.5, f"Depth = {depth} ft", color='white', va='center', fontweight='bold')
    
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 11.5)
    ax.axis('off')
    ax.set_title(f"BLUEPRINT: SUPPORT PIER (QTY: {qty})", color='white', pad=8)
    return fig

def draw_siding_wall(w, h, win_w, win_h, qty_win):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    wall = patches.Rectangle((0, 0), w, h, edgecolor='white', facecolor='#2b547e', linewidth=2)
    ax.add_patch(wall)
    
    spacing = w / (qty_win + 1)
    for i in range(1, qty_win + 1):
        wx = spacing * i - (win_w / 2)
        wy = h * 0.35
        win = patches.Rectangle((wx, wy), win_w, win_h, edgecolor='#ffcc00', facecolor='#1e3d59', linewidth=1.5)
        ax.add_patch(win)
        
    ax.text(w / 2, -h * 0.1, f"Wall Width = {w} ft", color='white', ha='center', fontweight='bold')
    ax.text(-w * 0.06, h / 2, f"Height = {h} ft", color='white', va='center', rotation=90, fontweight='bold')
    ax.text(w / 2, h * 1.06, f"{qty_win} Windows (Each {win_w} ft x {win_h} ft)", color='#ffcc00', ha='center', fontweight='bold')
    
    ax.set_xlim(-w * 0.15, w * 1.15)
    ax.set_ylim(-h * 0.2, h * 1.2)
    ax.axis('off')
    ax.set_title("BLUEPRINT: EXTERIOR WALL ELEVATION", color='white', pad=8)
    return fig

def draw_clerestory_window(dist, angle_deg):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rad = math.radians(angle_deg)
    h = dist * math.tan(rad)
    
    ax.plot([0, 0], [0, h * 1.25], color='white', linewidth=3)
    ax.plot([0, dist * 1.2], [0, 0], color='white', linewidth=3)
    ax.plot([0, 0], [h * 0.85, h], color='#00ffff', linewidth=5)
    ax.plot([0, dist], [h, 0], color='#ffcc00', linestyle='--', linewidth=2)
    
    ax.add_patch(patches.Rectangle((0, 0), dist * 0.08, dist * 0.08, edgecolor='white', facecolor='none'))
    ax.text(dist * 0.72, h * 0.08, f"{angle_deg}°", color='#ffcc00', fontweight='bold', fontsize=11)
    ax.text(dist / 2, -h * 0.14, f"Floor Reach = {dist} ft", color='white', ha='center', fontweight='bold')
    ax.text(-dist * 0.08, h / 2, "Window
Height = ?", color='#00ffff', ha='right', va='center', fontweight='bold')
    
    ax.set_xlim(-dist * 0.32, dist * 1.25)
    ax.set_ylim(-h * 0.25, h * 1.35)
    ax.axis('off')
    ax.set_title("BLUEPRINT: CLERESTORY WINDOW DAYLIGHTING", color='white', pad=8)
    return fig

def draw_light_reflection(d1, d2, angle_deg):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rad = math.radians(angle_deg)
    h1 = d1 * math.tan(rad)
    h2 = d2 * math.tan(rad)
    total_w = d1 + d2
    max_h = max(h1, h2) * 1.3
    
    ax.plot([0, 0], [0, max_h], color='white', linewidth=3)
    ax.plot([total_w, total_w], [0, max_h], color='white', linewidth=3)
    ax.plot([0, total_w], [0, 0], color='white', linewidth=3)
    
    ax.plot([0, d1], [h1, 0], color='#ffcc00', linestyle='--', linewidth=2)
    ax.plot([d1, total_w], [0, h2], color='#00ffff', linestyle='--', linewidth=2)
    ax.scatter([d1], [0], color='#00ffff', s=60, zorder=5)
    
    ax.text(d1 * 0.75, max_h * 0.07, f"{angle_deg}°", color='#ffcc00', fontweight='bold')
    ax.text(d1 + d2 * 0.18, max_h * 0.07, f"{angle_deg}°", color='#00ffff', fontweight='bold')
    ax.text(d1 / 2, -max_h * 0.1, f"{d1} ft", color='white', ha='center', fontweight='bold')
    ax.text(d1 + d2 / 2, -max_h * 0.1, f"{d2} ft", color='white', ha='center', fontweight='bold')
    ax.text(total_w + total_w * 0.04, h2 / 2, "Target
Height = ?", color='#00ffff', ha='left', va='center', fontweight='bold')
    
    ax.set_xlim(-total_w * 0.15, total_w * 1.32)
    ax.set_ylim(-max_h * 0.2, max_h * 1.1)
    ax.axis('off')
    ax.set_title("BLUEPRINT: REFLECTIVE LIGHT WELL", color='white', pad=8)
    return fig

def draw_solar_strut(base_run, angle_deg):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rad = math.radians(angle_deg)
    rise = base_run * math.tan(rad)
    
    ax.plot([0, base_run], [0, 0], color='white', linewidth=3)
    ax.plot([base_run, base_run], [0, rise], color='white', linestyle=':', linewidth=2)
    ax.plot([0, base_run], [0, rise], color='#00ffff', linewidth=4)
    
    ax.add_patch(patches.Rectangle((base_run * 0.92, 0), base_run * 0.08, base_run * 0.08, edgecolor='white', facecolor='none'))
    ax.text(base_run * 0.22, rise * 0.08, f"{angle_deg}°", color='#ffcc00', fontweight='bold', fontsize=11)
    ax.text(base_run / 2, -rise * 0.15, f"Roof Base Run = {base_run} ft", color='white', ha='center', fontweight='bold')
    ax.text(base_run * 0.42, rise * 0.62, "Strut Length = ?", color='#00ffff', ha='right', fontweight='bold')
    
    ax.set_xlim(-base_run * 0.15, base_run * 1.2)
    ax.set_ylim(-rise * 0.28, rise * 1.3)
    ax.axis('off')
    ax.set_title("BLUEPRINT: ANGLED SOLAR ARRAY STRUT", color='white', pad=8)
    return fig

def draw_guy_wire(post_h, angle_deg):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rad = math.radians(angle_deg)
    ground_d = post_h / math.tan(rad)
    
    ax.plot([0, 0], [0, post_h], color='white', linewidth=4)
    ax.plot([0, ground_d], [0, 0], color='white', linewidth=3)
    ax.plot([0, ground_d], [post_h, 0], color='#ffcc00', linestyle='--', linewidth=3)
    
    ax.add_patch(patches.Rectangle((0, 0), ground_d * 0.08, ground_d * 0.08, edgecolor='white', facecolor='none'))
    ax.text(ground_d * 0.72, post_h * 0.08, f"{angle_deg}°", color='#ffcc00', fontweight='bold', fontsize=11)
    ax.text(-ground_d * 0.06, post_h / 2, f"Post Height
= {post_h} ft", color='white', ha='right', va='center', fontweight='bold')
    ax.text(ground_d * 0.55, post_h * 0.58, "Cable Length = ?", color='#ffcc00', ha='left', fontweight='bold')
    
    ax.set_xlim(-ground_d * 0.35, ground_d * 1.2)
    ax.set_ylim(-post_h * 0.2, post_h * 1.25)
    ax.axis('off')
    ax.set_title("BLUEPRINT: STRUCTURAL GUY-WIRE CABLE", color='white', pad=8)
    return fig

def draw_crisis_trench(b1, b2, depth, length):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#591e1e')
    ax.set_facecolor('#591e1e')
    
    offset = (b1 - b2) / 2
    coords = [(0, depth), (b1, depth), (b1 - offset, 0), (offset, 0)]
    trap = patches.Polygon(coords, closed=True, edgecolor='white', facecolor='#7e2b2b', linewidth=2)
    ax.add_patch(trap)
    
    ax.text(b1 / 2, depth + depth * 0.08, f"Top Width = {b1} ft", color='#ffcc00', ha='center', fontweight='bold')
    ax.text(b1 / 2, -depth * 0.15, f"Bottom Width = {b2} ft", color='white', ha='center', fontweight='bold')
    ax.text(b1 + b1 * 0.06, depth / 2, f"Depth = {depth} ft", color='white', va='center', fontweight='bold')
    
    ax.set_xlim(-b1 * 0.2, b1 * 1.35)
    ax.set_ylim(-depth * 0.3, depth * 1.3)
    ax.axis('off')
    ax.set_title(f"🚨 CRISIS: DRAINAGE TRENCH (LENGTH: {length} FT)", color='#ffcc00', pad=8)
    return fig

def draw_crisis_gable(base, height):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#591e1e')
    ax.set_facecolor('#591e1e')
    
    coords = [(0, 0), (base, 0), (base / 2, height)]
    tri = patches.Polygon(coords, closed=True, edgecolor='white', facecolor='#7e2b2b', linewidth=2)
    ax.add_patch(tri)
    ax.plot([base / 2, base / 2], [0, height], color='#ffcc00', linestyle='--', linewidth=1.5)
    
    ax.text(base / 2, -height * 0.12, f"Roof Span (Base) = {base} ft", color='white', ha='center', fontweight='bold')
    ax.text(base / 2 + base * 0.03, height / 2, f"Height = {height} ft", color='#ffcc00', va='center', fontweight='bold')
    
    ax.set_xlim(-base * 0.15, base * 1.15)
    ax.set_ylim(-height * 0.25, height * 1.2)
    ax.axis('off')
    ax.set_title("🚨 CRISIS: DAMAGED ROOF GABLE", color='#ffcc00', pad=8)
    return fig

def draw_crisis_overhang(overhang_w, sun_angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#591e1e')
    ax.set_facecolor('#591e1e')
    
    rad = math.radians(sun_angle)
    drop = overhang_w * math.tan(rad)
    
    ax.plot([0, 0], [0, drop * 1.3], color='white', linewidth=3)
    ax.plot([0, overhang_w], [drop, drop], color='white', linewidth=4)
    ax.plot([overhang_w, 0], [drop, 0], color='#ffcc00', linestyle='--', linewidth=2)
    
    ax.add_patch(patches.Rectangle((0, drop - overhang_w * 0.08), overhang_w * 0.08, overhang_w * 0.08, edgecolor='white', facecolor='none'))
    ax.text(overhang_w * 0.65, drop * 0.85, f"{sun_angle}°", color='#ffcc00', fontweight='bold', fontsize=11)
    ax.text(overhang_w / 2, drop * 1.08, f"Overhang = {overhang_w} ft", color='white', ha='center', fontweight='bold')
    ax.text(-overhang_w * 0.08, drop / 2, "Shadow
Drop = ?", color='#00ffff', ha='right', va='center', fontweight='bold')
    
    ax.set_xlim(-overhang_w * 0.35, overhang_w * 1.25)
    ax.set_ylim(-drop * 0.2, drop * 1.45)
    ax.axis('off')
    ax.set_title("🚨 CRISIS: ROOF OVERHANG GLARE BLOCK", color='#ffcc00', pad=8)
    return fig

# --- RANDOM POSITIVE WINDFALLS ---
WINDFALL_EVENTS = [
    {"title": "Cement Supplier Surplus!", "cash": 650, "days": 0, "rep": 0,
     "msg": "🍀 **Good News!** Local cement prices dropped due to a supplier surplus—you saved **$650**!"},
    {"title": "Lumber Mill Rebate!", "cash": 500, "days": 0, "rep": 0,
     "msg": "🍀 **Good News!** Your lumber supplier issued a bulk-order rebate—you saved **$500**!"},
    {"title": "Clear Skies Ahead!", "cash": 0, "days": 2, "rep": 5,
     "msg": "☀️ **Perfect Weather!** A week of dry, sunny skies let your crew work ahead of schedule (+2 days, +5% reputation)!"},
    {"title": "Early Inspector Sign-Off!", "cash": 300, "days": 1, "rep": 5,
     "msg": "📋 **Smooth Inspection!** The county building inspector loved your framing work—saved **$300** in permit fees and gained **1 day**!"},
    {"title": "Salvaged Hardware Find!", "cash": 450, "days": 0, "rep": 0,
     "msg": "♻️ **Smart Sourcing!** You sourced surplus architectural fixtures from another job site, saving **$450**!"}
]

def apply_cash_credit(amount):
    if st.session_state.debt > 0:
        paid_off = min(st.session_state.debt, amount)
        st.session_state.debt -= paid_off
        leftover = amount - paid_off
        st.session_state.budget += leftover
        if leftover > 0:
            return f" (Paid off **${paid_off:,}** in debt and added **${leftover:,}** to your cash budget!)"
        return f" (Applied **${paid_off:,}** directly toward paying down your debt!)"
    else:
        st.session_state.budget += amount
        return ""

# --- BUILD PROJECT TIMELINE (1:4 RATIO) ---
def generate_project_queue():
    regular_events = [
        {"type": "regular", "subtype": "floor", "title": "Living Room Hardwood Order",
         "w1": random.choice([18, 20, 22]), "h1": random.choice([12, 14, 15]),
         "w2": random.choice([8, 10, 12]), "h2": random.choice([6, 8, 10]), "rate": 6},
        {"type": "regular", "subtype": "piers", "title": "Deck Foundation Piers",
         "diam": random.choice([2, 4]), "depth": random.choice([6, 8, 10]),
         "qty": random.choice([4, 6, 8]), "rate": 5},
        {"type": "regular", "subtype": "siding", "title": "Front Elevation Siding",
         "w": random.choice([24, 28, 30]), "h": random.choice([10, 12]),
         "win_w": 3, "win_h": 4, "qty_win": random.choice([2, 3]), "rate": 7},
        {"type": "regular", "subtype": "slab", "title": "Garage Concrete Pour",
         "l": random.choice([20, 22, 24]), "w": random.choice([20, 24]), "thick": 0.5, "rate": 6},
        {"type": "regular", "subtype": "window", "title": "Clerestory Window Placement",
         "dist": random.choice([12, 15, 18]), "angle": random.choice([35, 40, 50]), "rate": 120},
        {"type": "regular", "subtype": "reflection", "title": "Reflective Light Well Alignment",
         "d1": random.choice([6, 8, 10]), "d2": random.choice([8, 10, 12]),
         "angle": random.choice([38, 45, 52]), "rate": 110},
        {"type": "regular", "subtype": "strut", "title": "Solar Panel Support Strut",
         "base_run": random.choice([8, 10, 12]), "angle": random.choice([30, 35, 40]), "rate": 95},
        {"type": "regular", "subtype": "guywire", "title": "Structural Guy-Wire Anchor",
         "post_h": random.choice([12, 15, 18]), "angle": random.choice([40, 50, 55]), "rate": 85},
    ]
    
    crisis_events = [
        {"type": "crisis", "subtype": "trench", "title": "🚨 CRISIS: Flash Flood Washout!",
         "desc": "Heavy rain washed out the site access road! Fill the trapezoidal drainage trench with crushed gravel immediately so concrete trucks can reach the lot.",
         "b1": random.choice([6, 8, 10]), "b2": random.choice([2, 4]),
         "depth": random.choice([3, 4, 5]), "length": random.choice([15, 20, 25]), "rate": 4},
        {"type": "crisis", "subtype": "gable", "title": "🚨 CRISIS: High Winds Tear Roof Sheathing!",
         "desc": "A sudden windstorm ripped the sheathing off the triangular front gable before shingles were installed! Order weather-barrier panels before rain hits.",
         "base": random.choice([20, 24, 28]), "height": random.choice([8, 10, 12]), "rate": 9},
        {"type": "crisis", "subtype": "overhang", "title": "🚨 CRISIS: Solar Glare Inspection Hold!",
         "desc": "The building inspector flagged dangerous afternoon glare entering the glass entryway! Build a horizontal roof overhang that casts the exact vertical shadow drop shown below.",
         "overhang_w": random.choice([4, 5, 6]), "sun_angle": random.choice([55, 60, 65]), "rate": 140}
    ]
    
    selected_regular = random.sample(regular_events, 8)
    selected_crisis = random.sample(crisis_events, 2)
    
    # 1:4 ratio (2 crises among 8 regular milestones)
    timeline = selected_regular[:3] + [selected_crisis[0]] + selected_regular[3:6] + [selected_crisis[1]] + selected_regular[6:]
    return timeline

# --- INITIALIZE SESSION STATE ---
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.student_name = ""
    st.session_state.idx = 0
    st.session_state.budget = 45000
    st.session_state.debt = 0
    st.session_state.days = 45
    st.session_state.reputation = 100
    st.session_state.queue = generate_project_queue()
    st.session_state.history = []
    st.session_state.hints_level = {} # Tracks 0, 1, 2, or 3 hints unlocked per stage
    st.session_state.total_paid_hints = 0
    st.session_state.exact_count = 0

def reset_game():
    st.session_state.started = False
    st.session_state.idx = 0
    st.session_state.budget = 45000
    st.session_state.debt = 0
    st.session_state.days = 45
    st.session_state.reputation = 100
    st.session_state.queue = generate_project_queue()
    st.session_state.history = []
    st.session_state.hints_level = {}
    st.session_state.total_paid_hints = 0
    st.session_state.exact_count = 0

def process_transaction(cost, is_exact, msg_exact, msg_error):
    bonus = 750 if is_exact else 0
    
    if is_exact:
        st.session_state.exact_count += 1
        st.session_state.days -= 3
        st.session_state.reputation = min(100, st.session_state.reputation + 5)
        debt_note = apply_cash_credit(bonus)
        bonus_note = f" 🌟 **Precision Bonus (+$750):** Zero waste supplier rebate!{debt_note}"
        st.session_state.history.append(("success", msg_exact + bonus_note))
    else:
        st.session_state.days -= 6
        st.session_state.reputation -= 15
        st.session_state.history.append(("error", msg_error))

    st.session_state.budget -= cost
    if st.session_state.budget < 0:
        shortfall = abs(st.session_state.budget)
        interest_fee = round(shortfall * 0.15)
        borrowed_total = shortfall + interest_fee
        st.session_state.debt += borrowed_total
        st.session_state.budget = 0
        st.session_state.history.append(("warning", f"🏦 **Cost Overrun Alert!** Cash hit $0. You borrowed **${shortfall:,}** (+ ${interest_fee:,} loan fee) from your Emergency Line of Credit."))

    if st.session_state.idx + 1 < len(st.session_state.queue) and random.random() < 0.35:
        windfall = random.choice(WINDFALL_EVENTS)
        st.session_state.days += windfall["days"]
        st.session_state.reputation = min(100, st.session_state.reputation + windfall["rep"])
        extra_note = apply_cash_credit(windfall["cash"]) if windfall["cash"] > 0 else ""
        st.session_state.history.append(("info", windfall["msg"] + extra_note))

# --- TOP DASHBOARD ---
st.title("🚧 Contractor's Crisis")
c1, c2, c3, c4 = st.columns(4)
c1.metric("💰 Cash Budget", f"${st.session_state.budget:,}")
c2.metric("🏦 Credit Debt", f"${st.session_state.debt:,}", delta=f"-${st.session_state.debt:,}" if st.session_state.debt > 0 else None, delta_color="inverse")
c3.metric("📅 Days Left", f"{st.session_state.days}")
c4.metric("⭐ Reputation", f"{st.session_state.reputation}%")
st.divider()

# --- INTRO SCREEN ---
if not st.session_state.started:
    st.subheader("Welcome to Contractor's Crisis!")
    st.write("""
    You have **45 days** and **$45,000** to complete a 10-stage construction project. 
    * **Regular Milestones (8):** Order materials and size architectural fixtures accurately using 2D Area, 3D Volume, and Right-Triangle Trigonometry.
    * **Crisis Events (2):** Unexpected site emergencies will strike!
    * **Free Visual Formula Sheet:** Reference all 2D, 3D, and Trigonometry diagrams at any time for free.
    * **Progressive Engineer Hints ($250 each):** Stuck on a job? Unlock up to **3 step-by-step hints** per stage—from identifying what needs to be measured all the way to the filled-in formula.
    """)
    name_input = st.text_input("Enter Contractor / Student Name:", value=st.session_state.student_name, placeholder="e.g., Jordan Smith")
    if st.button("Break Ground ➡️"):
        st.session_state.student_name = name_input.strip() if name_input.strip() else "Anonymous Contractor"
        st.session_state.started = True
        st.rerun()

# --- GAMEPLAY LOOP ---
elif st.session_state.idx < len(st.session_state.queue):
    if st.session_state.history:
        for status, text in st.session_state.history:
            if status == "success":
                st.success(text)
            elif status == "error":
                st.error(text)
            elif status == "warning":
                st.warning(text)
            elif status == "info":
                st.info(text)

    stage_num = st.session_state.idx
    event = st.session_state.queue[stage_num]
    st.caption(f"STAGE {stage_num + 1} OF {len(st.session_state.queue)} | CONTRACTOR: {st.session_state.student_name.upper()}")
    
    if event["type"] == "crisis":
        st.subheader(event["title"])
        st.warning(event["desc"])
    else:
        st.subheader(f"🔨 Milestone: {event['title']}")

    sub = event["subtype"]
    
    # --- CONFIGURE SCENARIO TASK, BLUEPRINT, AND 3 PROGRESSIVE HINTS ---
    if sub == "floor":
        st.write(f"Determine how many square feet of hardwood flooring need to be ordered to cover the entire L-shaped room shown below. Flooring costs **${event['rate']}/sq ft**.")
        st.pyplot(draw_composite_floor(event["w1"], event["h1"], event["w2"], event["h2"]))
        correct = (event["w1"] * event["h1"]) + (event["w2"] * event["h2"])
        unit = "sq ft"
        tol = 0
        hints = [
            "**Hint 1 (Goal):** You need to find the total 2D floor area of the L-shaped room by splitting it into two separate rectangles.",
            "**Hint 2 (Formula):** Use the parallelogram/rectangle area formula **A = b · h** on the bottom section and the top alcove, then add them together.",
            f"**Hint 3 (Setup):** Bottom rectangle = **({event['w1']} × {event['h1']})** + Top alcove = **({event['w2']} × {event['h2']})**."
        ]

    elif sub == "piers":
        st.write(f"Determine how many cubic feet of cement need to be ordered to pour all **{event['qty']} cylindrical support piers** (round to the nearest whole cubic foot). Cement costs **${event['rate']}/cu ft**.")
        st.pyplot(draw_cylinder_piers(event["diam"], event["depth"], event["qty"]))
        r = event["diam"] / 2
        correct = round(math.pi * (r ** 2) * event["depth"] * event["qty"])
        unit = "cu ft"
        tol = 2
        hints = [
            "**Hint 1 (Goal):** Calculate the 3D volume of one cylindrical pier, then multiply by the total number of piers.",
            "**Hint 2 (Formula):** Use the cylinder volume formula **V = π · r² · h** (remember that radius **r** is half of the diameter!).",
            f"**Hint 3 (Setup):** Radius = **{r} ft**. Total Cement = **π · ({r}²) · {event['depth']} · {event['qty']}**."
        ]

    elif sub == "siding":
        st.write(f"Determine how many square feet of exterior siding need to be ordered to cover the front wall without covering the windows. Siding costs **${event['rate']}/sq ft**.")
        st.pyplot(draw_siding_wall(event["w"], event["h"], event["win_w"], event["win_h"], event["qty_win"]))
        correct = (event["w"] * event["h"]) - (event["qty_win"] * event["win_w"] * event["win_h"])
        unit = "sq ft"
        tol = 0
        hints = [
            "**Hint 1 (Goal):** Find the net surface area of the wall by subtracting the area of all windows from the total rectangular wall area.",
            "**Hint 2 (Formula):** Use **A = b · h** to find the full wall area, then subtract **(Number of Windows × b · h)**.",
            f"**Hint 3 (Setup):** Full Wall = **({event['w']} × {event['h']})** minus Windows = **{event['qty_win']} × ({event['win_w']} × {event['win_h']})**."
        ]

    elif sub == "slab":
        st.write(f"Determine how many cubic feet of cement need to be ordered to pour a rectangular garage foundation measuring **{event['l']} ft long × {event['w']} ft wide × {event['thick']} ft (6 inches) thick**. Cement costs **${event['rate']}/cu ft**.")
        correct = round(event["l"] * event["w"] * event["thick"])
        unit = "cu ft"
        tol = 0
        hints = [
            "**Hint 1 (Goal):** Calculate the 3D volume of the rectangular concrete foundation slab.",
            "**Hint 2 (Formula):** Use the rectangular prism volume formula **V = l · w · h** (make sure all dimensions are in feet).",
            f"**Hint 3 (Setup):** Concrete Volume = **{event['l']} × {event['w']} × {event['thick']}**."
        ]

    elif sub == "window":
        st.write(f"At noon, sunlight enters at a **{event['angle']}°** angle and must reach **{event['dist']} ft** across the floor. Determine how high above the floor (to the nearest whole foot) the top of the clerestory window must be placed. Framing costs **${event['rate']}/ft** of height.")
        st.pyplot(draw_clerestory_window(event["dist"], event["angle"]))
        correct = round(event["dist"] * math.tan(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        hints = [
            "**Hint 1 (Goal):** Find the missing vertical height (the side opposite the angle) of the right triangle formed by the sunbeam.",
            "**Hint 2 (Formula):** Since you have the Adjacent side and need the Opposite side, use **tan(θ) = Opposite / Adjacent**.",
            f"**Hint 3 (Setup):** **tan({event['angle']}°) = Height / {event['dist']}**, so Height = **{event['dist']} × tan({event['angle']}°)**."
        ]

    elif sub == "reflection":
        st.write(f"A sunbeam enters at **{event['angle']}°**, bounces off a floor mirror **{event['d1']} ft** from the left wall, and hits the opposite wall **{event['d2']} ft** away. Determine at what height (to the nearest whole foot) the reflector panel must be mounted on the right wall. Mounting costs **${event['rate']}/ft**.")
        st.pyplot(draw_light_reflection(event["d1"], event["d2"], event["angle"]))
        correct = round(event["d2"] * math.tan(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        hints = [
            "**Hint 1 (Goal):** Use the Law of Reflection (angle in = angle out) to find the vertical height on the right-hand right triangle.",
            "**Hint 2 (Formula):** On the right-hand triangle, you know the Adjacent floor distance and the angle, so use **tan(θ) = Opposite / Adjacent**.",
            f"**Hint 3 (Setup):** **tan({event['angle']}°) = Target Height / {event['d2']}**, so Target Height = **{event['d2']} × tan({event['angle']}°)**."
        ]

    elif sub == "strut":
        st.write(f"A solar panel frame spans a **{event['base_run']} ft** horizontal roof run and tilts upward at **{event['angle']}°**. Determine the required length (to the nearest whole foot) of the diagonal support strut. Steel struts cost **${event['rate']}/ft**.")
        st.pyplot(draw_solar_strut(event["base_run"], event["angle"]))
        correct = round(event["base_run"] / math.cos(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        hints = [
            "**Hint 1 (Goal):** Find the length of the slanted diagonal side (the Hypotenuse) of the right triangle.",
            "**Hint 2 (Formula):** Since you know the Adjacent horizontal run and need the Hypotenuse, use **cos(θ) = Adjacent / Hypotenuse**.",
            f"**Hint 3 (Setup):** **cos({event['angle']}°) = {event['base_run']} / Strut**, so Strut Length = **{event['base_run']} / cos({event['angle']}°)**."
        ]

    elif sub == "guywire":
        st.write(f"A **{event['post_h']} ft** tall vertical structural post must be braced by a steel guy-wire anchored to the ground at a **{event['angle']}°** angle. Determine the required cable length (to the nearest whole foot). Cable costs **${event['rate']}/ft**.")
        st.pyplot(draw_guy_wire(event["post_h"], event["angle"]))
        correct = round(event["post_h"] / math.sin(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        hints = [
            "**Hint 1 (Goal):** Find the length of the diagonal cable (the Hypotenuse) stretching from the top of the post to the ground.",
            "**Hint 2 (Formula):** Since you know the Opposite vertical height and need the Hypotenuse, use **sin(θ) = Opposite / Hypotenuse**.",
            f"**Hint 3 (Setup):** **sin({event['angle']}°) = {event['post_h']} / Cable**, so Cable Length = **{event['post_h']} / sin({event['angle']}°)**."
        ]

    elif sub == "trench":
        st.write(f"Determine how many cubic feet of crushed gravel need to be ordered to completely fill this **{event['length']}-foot-long** trapezoidal drainage trench. Gravel costs **${event['rate']}/cu ft**.")
        st.pyplot(draw_crisis_trench(event["b1"], event["b2"], event["depth"], event["length"]))
        correct = round(0.5 * (event["b1"] + event["b2"]) * event["depth"] * event["length"])
        unit = "cu ft"
        tol = 0
        hints = [
            "**Hint 1 (Goal):** Find the 3D volume of the trapezoidal prism by finding the area of its trapezoid face first, then multiplying by the trench length.",
            "**Hint 2 (Formula):** Use **A = ½(b₁ + b₂) · h** for the trapezoid cross-section, then **V = B · length**.",
            f"**Hint 3 (Setup):** Trapezoid Base Area = **0.5 × ({event['b1']} + {event['b2']}) × {event['depth']}**, then multiply by **{event['length']} ft**."
        ]

    elif sub == "gable":
        st.write(f"Determine how many square feet of weather-barrier panels need to be ordered to cover the triangular roof gable. Panels cost **${event['rate']}/sq ft**.")
        st.pyplot(draw_crisis_gable(event["base"], event["height"]))
        correct = round(0.5 * event["base"] * event["height"])
        unit = "sq ft"
        tol = 0
        hints = [
            "**Hint 1 (Goal):** Find the 2D area of the triangular front gable section.",
            "**Hint 2 (Formula):** Use the triangle area formula **A = ½ · b · h**.",
            f"**Hint 3 (Setup):** Gable Area = **0.5 × {event['base']} × {event['height']}**."
        ]

    elif sub == "overhang":
        st.write(f"When the sun is at a **{event['sun_angle']}°** angle, a **{event['overhang_w']} ft** horizontal roof overhang blocks direct glare from hitting the glass below. Determine the vertical shadow drop (to the nearest whole foot) cast along the wall. Framing costs **${event['rate']}/ft**.")
        st.pyplot(draw_crisis_overhang(event["overhang_w"], event["sun_angle"]))
        correct = round(event["overhang_w"] * math.tan(math.radians(event["sun_angle"])))
        unit = "ft"
        tol = 1
        hints = [
            "**Hint 1 (Goal):** Find the missing vertical shadow height (the side opposite the angle) on the right triangle beneath the overhang.",
            "**Hint 2 (Formula):** Since you have the Adjacent overhang width and need the Opposite vertical drop, use **tan(θ) = Opposite / Adjacent**.",
            f"**Hint 3 (Setup):** **tan({event['sun_angle']}°) = Drop / {event['overhang_w']}**, so Shadow Drop = **{event['overhang_w']} × tan({event['sun_angle']}°)**."
        ]

    # --- TWO-TIER HINT SYSTEM ---
    with st.expander("📐 Free Visual Formula Reference Sheet (2D, 3D & Trig)"):
        st.pyplot(generate_formula_sheet())

    current_hint_lvl = st.session_state.hints_level.get(stage_num, 0)
    
    col_h1, col_h2 = st.columns([1, 2])
    with col_h1:
        if current_hint_lvl < 3:
            btn_label = f"👷 Hire Engineer Hint {current_hint_lvl + 1}/3 (-$250)"
            if st.button(btn_label, key=f"hint_btn_{stage_num}"):
                st.session_state.hints_level[stage_num] = current_hint_lvl + 1
                st.session_state.total_paid_hints += 1
                st.session_state.budget -= 250
                if st.session_state.budget < 0:
                    shortfall = abs(st.session_state.budget)
                    st.session_state.debt += shortfall
                    st.session_state.budget = 0
                st.rerun()
        else:
            st.button("✅ All 3 Hints Unlocked", disabled=True, key=f"hint_done_{stage_num}")

    # Display all unlocked progressive hints for this stage
    for lvl in range(current_hint_lvl):
        st.info(hints[lvl])

    # --- STUDENT INPUT & SUBMISSION ---
    user_ans = st.number_input(f"Enter your order quantity ({unit}):", min_value=0, step=1, key=f"ans_{stage_num}")
    
    if st.button("Place Material Order 📦", key=f"btn_{stage_num}"):
        st.session_state.history = []
        base_cost = correct * event["rate"]
        
        if abs(user_ans - correct) <= tol:
            process_transaction(
                cost=base_cost,
                is_exact=True,
                msg_exact=f"✅ **Exact Measurement ({correct} {unit})!** Ordered materials for **${base_cost:,}**.",
                msg_error=""
            )
        elif user_ans < correct:
            shortage = correct - user_ans
            rush_penalty = round(shortage * event["rate"] * 1.75) + 800
            total_cost = base_cost + rush_penalty
            process_transaction(
                cost=total_cost,
                is_exact=False,
                msg_exact="",
                msg_error=f"❌ **Under-Ordered!** You entered {user_ans} {unit}, but needed **{correct} {unit}**. Rush delivery fees added **${rush_penalty:,}** (Total: ${total_cost:,}) and delayed the crew by 6 days!"
            )
        else:
            waste = (user_ans - correct) * event["rate"]
            total_cost = base_cost + waste
            process_transaction(
                cost=total_cost,
                is_exact=False,
                msg_exact="",
                msg_error=f"⚠️ **Over-Ordered!** You entered {user_ans} {unit}, but only needed **{correct} {unit}**. You wasted **${waste:,}** on surplus materials (Total: ${total_cost:,}) and lost 6 days clearing the site!"
            )
            
        st.session_state.idx += 1
        st.rerun()

# --- FINAL SUMMARY & AUDIT RECEIPT ---
else:
    for status, text in st.session_state.history:
        if status == "success":
            st.success(text)
        elif status == "error":
            st.error(text)
        elif status == "warning":
            st.warning(text)
        elif status == "info":
            st.info(text)

    st.subheader("🏁 Build Complete: Final Company Audit")
    net_profit = st.session_state.budget - st.session_state.debt
    total_stages = len(st.session_state.queue)
    accuracy_pct = round((st.session_state.exact_count / total_stages) * 100)
    
    if net_profit > 0 and st.session_state.days >= 0 and st.session_state.debt == 0:
        st.balloons()
        outcome = "MASTER CONTRACTOR (PASSED ON TIME & UNDER BUDGET)"
        st.success(f"🏆 **Master Contractor!** You finished with **${net_profit:,}** net profit, **$0 debt**, and **{st.session_state.days} days** to spare!")
    elif net_profit > 0 and st.session_state.debt > 0:
        outcome = "SURVIVED THE CRISIS (FINISHED WITH CREDIT DEBT)"
        st.warning(f"⚠️ **Survived the Crisis!** You finished with **${st.session_state.debt:,}** in remaining credit debt, leaving a net balance of **${net_profit:,}**.")
    else:
        outcome = "BUDGET OVERRUN / DEADLINE MISSED"
        st.error(f"📉 **Bankruptcy Warning!** Cost overruns and crisis events left your company **${abs(net_profit):,}** in the hole.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt_text = f"""==================================================
        CONTRACTOR'S CRISIS - FINAL AUDIT
==================================================
Contractor Name : {st.session_state.student_name}
Completion Date : {timestamp}
Project Status  : {outcome}
--------------------------------------------------
Exact Blueprints: {st.session_state.exact_count} / {total_stages} ({accuracy_pct}%)
Paid Hints Used : {st.session_state.total_paid_hints} (-${st.session_state.total_paid_hints * 250:,})
Days Remaining  : {st.session_state.days} days
Client Rating   : {st.session_state.reputation}%
--------------------------------------------------
Remaining Cash  : ${st.session_state.budget:,}
Unpaid Debt     : ${st.session_state.debt:,}
NET PROFIT      : ${net_profit:,}
==================================================
"""
    st.code(receipt_text, language="text")
    
    st.download_button(
        label="📄 Download Audit Receipt (.txt)",
        data=receipt_text,
        file_name=f"Contractors_Crisis_{st.session_state.student_name.replace(' ', '_')}.txt",
        mime="text/plain"
    )

    if st.button("Start New Contract 🔄"):
        reset_game()
        st.rerun()
