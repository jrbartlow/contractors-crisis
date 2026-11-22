import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import math
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(page_title="Contractor's Crisis", page_icon="🚧", layout="centered")

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
    ax.set_title("BLUEPRINT: COMPOSITE SUBFLOOR", color='white', pad=8)
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
    ax.set_title(f"BLUEPRINT: CONCRETE PIERS (QTY: {qty})", color='white', pad=8)
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
    ax.set_title("BLUEPRINT: EXTERIOR SIDING ELEVATION", color='white', pad=8)
    return fig

def draw_clerestory_window(dist, angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    h = dist * math.tan(math.radians(angle))
    # Wall and floor
    ax.plot([0, 0], [0, h * 1.25], color='white', linewidth=3)
    ax.plot([0, dist * 1.2], [0, 0], color='white', linewidth=3)
    # Sunbeam hypotenuse
    ax.plot([0, dist], [h, 0], color='#ffcc00', linestyle='--', linewidth=2.5)
    # Right angle box
    sq = min(dist, h) * 0.12
    ax.plot([0, sq, sq], [sq, sq, 0], color='white', linewidth=1)
    
    ax.text(-dist * 0.08, h / 2, "Height = ? ft", color='#ffcc00', va='center', ha='right', fontweight='bold')
    ax.text(dist / 2, -h * 0.12, f"Floor Reach = {dist} ft", color='white', ha='center', fontweight='bold')
    ax.text(dist * 0.72, h * 0.08, f"{angle}°", color='#ffcc00', fontweight='bold')
    
    ax.set_xlim(-dist * 0.35, dist * 1.25)
    ax.set_ylim(-h * 0.25, h * 1.35)
    ax.axis('off')
    ax.set_title("BLUEPRINT: CLERESTORY WINDOW LIGHT ANGLE", color='white', pad=8)
    return fig

def draw_light_reflection(d1, d2, angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    h1 = d1 * math.tan(math.radians(angle))
    h2 = d2 * math.tan(math.radians(angle))
    total_w = d1 + d2
    max_h = max(h1, h2) * 1.25
    
    # Left wall, floor, right wall
    ax.plot([0, 0], [0, max_h], color='white', linewidth=3)
    ax.plot([0, total_w], [0, 0], color='white', linewidth=3)
    ax.plot([total_w, total_w], [0, max_h], color='white', linewidth=3)
    
    # Light beams
    ax.plot([0, d1], [h1, 0], color='#ffcc00', linestyle='--', linewidth=2)
    ax.plot([d1, total_w], [0, h2], color='#00ffcc', linestyle='--', linewidth=2)
    ax.plot(d1, 0, marker='o', color='#ffcc00', markersize=6)
    
    ax.text(d1 / 2, -max_h * 0.1, f"{d1} ft", color='white', ha='center', fontweight='bold')
    ax.text(d1 + d2 / 2, -max_h * 0.1, f"{d2} ft", color='white', ha='center', fontweight='bold')
    ax.text(d1 - total_w * 0.09, max_h * 0.07, f"{angle}°", color='#ffcc00', fontweight='bold')
    ax.text(d1 + total_w * 0.04, max_h * 0.07, f"{angle}°", color='#00ffcc', fontweight='bold')
    ax.text(total_w + total_w * 0.04, h2 / 2, "Target\nHeight = ?", color='#00ffcc', va='center', fontweight='bold')
    
    ax.set_xlim(-total_w * 0.15, total_w * 1.32)
    ax.set_ylim(-max_h * 0.2, max_h * 1.1)
    ax.axis('off')
    ax.set_title("BLUEPRINT: REFLECTIVE LIGHT WELL", color='white', pad=8)
    return fig

def draw_solar_strut(run, angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    rise = run * math.tan(math.radians(angle))
    # Roof base, vertical post, angled solar strut
    ax.plot([0, run], [0, 0], color='white', linewidth=3)
    ax.plot([run, run], [0, rise], color='white', linewidth=2.5)
    ax.plot([0, run], [0, rise], color='#ffcc00', linewidth=3)
    
    sq = min(run, rise) * 0.12
    ax.plot([run - sq, run - sq, run], [0, sq, sq], color='white', linewidth=1)
    
    ax.text(run / 2, -rise * 0.15, f"Roof Base Run = {run} ft", color='white', ha='center', fontweight='bold')
    ax.text(run * 0.42, rise * 0.58, "Strut Length = ?", color='#ffcc00', ha='right', fontweight='bold')
    ax.text(run * 0.18, rise * 0.06, f"{angle}°", color='#ffcc00', fontweight='bold')
    
    ax.set_xlim(-run * 0.2, run * 1.2)
    ax.set_ylim(-rise * 0.28, rise * 1.25)
    ax.axis('off')
    ax.set_title("BLUEPRINT: SOLAR ARRAY SUPPORT STRUT", color='white', pad=8)
    return fig

def draw_guy_wire(height, angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#1e3d59')
    ax.set_facecolor('#1e3d59')
    
    base = height / math.tan(math.radians(angle))
    ax.plot([0, 0], [0, height], color='white', linewidth=3.5)
    ax.plot([0, base], [0, 0], color='white', linewidth=2.5)
    ax.plot([0, base], [height, 0], color='#ffcc00', linestyle='--', linewidth=2.5)
    
    sq = min(base, height) * 0.12
    ax.plot([0, sq, sq], [sq, sq, 0], color='white', linewidth=1)
    
    ax.text(-base * 0.06, height / 2, f"Post Height\n= {height} ft", color='white', va='center', ha='right', fontweight='bold')
    ax.text(base * 0.55, height * 0.55, "Cable Length = ?", color='#ffcc00', ha='left', fontweight='bold')
    ax.text(base * 0.75, height * 0.07, f"{angle}°", color='#ffcc00', fontweight='bold')
    
    ax.set_xlim(-base * 0.35, base * 1.25)
    ax.set_ylim(-height * 0.2, height * 1.2)
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
    ax.set_title(f"🚨 CRISIS: TRENCH GRAVEL FILL (LENGTH: {length} FT)", color='#ffcc00', pad=8)
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
    ax.set_title("🚨 CRISIS: STORM-DAMAGED GABLE TARPING", color='#ffcc00', pad=8)
    return fig

def draw_crisis_glare(overhang, angle):
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#591e1e')
    ax.set_facecolor('#591e1e')
    
    drop = overhang * math.tan(math.radians(angle))
    # Wall and overhang at top
    ax.plot([0, 0], [0, drop * 1.2], color='white', linewidth=3)
    ax.plot([0, overhang], [drop, drop], color='#ffcc00', linewidth=3.5)
    # Shadow ray from overhang tip to wall
    ax.plot([overhang, 0], [drop, 0], color='#00ffcc', linestyle='--', linewidth=2)
    
    sq = min(overhang, drop) * 0.12
    ax.plot([0, sq, sq], [drop - sq, drop - sq, drop], color='white', linewidth=1)
    
    ax.text(overhang / 2, drop + drop * 0.08, f"Overhang = {overhang} ft", color='#ffcc00', ha='center', fontweight='bold')
    ax.text(-overhang * 0.08, drop / 2, "Shadow\nDrop = ?", color='#00ffcc', va='center', ha='right', fontweight='bold')
    ax.text(overhang * 0.65, drop * 0.78, f"{angle}°", color='#00ffcc', fontweight='bold')
    
    ax.set_xlim(-overhang * 0.45, overhang * 1.25)
    ax.set_ylim(-drop * 0.15, drop * 1.28)
    ax.axis('off')
    ax.set_title("🚨 CRISIS: SOLAR GLARE OVERHANG DROP", color='#ffcc00', pad=8)
    return fig

# --- RANDOM POSITIVE WINDFALLS ---
WINDFALL_EVENTS = [
    {"cash": 650, "days": 0, "rep": 0,
     "msg": "🍀 **Good News!** Local cement prices dropped due to a supplier surplus—you saved **$650**!"},
    {"cash": 500, "days": 0, "rep": 0,
     "msg": "🍀 **Good News!** Your lumber supplier issued a bulk-order rebate—you saved **$500**!"},
    {"cash": 0, "days": 2, "rep": 5,
     "msg": "☀️ **Perfect Weather!** A week of dry, sunny skies let your crew work ahead of schedule (+2 days, +5% reputation)!"},
    {"cash": 300, "days": 1, "rep": 5,
     "msg": "📋 **Smooth Inspection!** The county building inspector loved your framing work—saved **$300** in permit fees and gained **1 day**!"},
    {"cash": 450, "days": 0, "rep": 0,
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

# --- BUILD PROJECT TIMELINE (1:4 CRISIS TO REGULAR RATIO) ---
def generate_project_queue():
    regular_events = [
        {"type": "regular", "subtype": "floor", "title": "Living Room Subflooring",
         "w1": random.choice([18, 20, 22]), "h1": random.choice([12, 14, 15]),
         "w2": random.choice([8, 10, 12]), "h2": random.choice([6, 8, 10]), "rate": 6},
        {"type": "regular", "subtype": "piers", "title": "Deck Support Piers (Cement)",
         "diam": random.choice([2, 4]), "depth": random.choice([6, 8, 10]),
         "qty": random.choice([4, 6, 8]), "rate": 5},
        {"type": "regular", "subtype": "siding", "title": "Exterior Wall Siding (Subtract Windows)",
         "w": random.choice([24, 28, 30]), "h": random.choice([10, 12]),
         "win_w": 3, "win_h": 4, "qty_win": random.choice([2, 3, 4]), "rate": 7},
        {"type": "regular", "subtype": "clerestory", "title": "Clerestory Window Daylighting",
         "dist": random.choice([12, 15, 18, 20]), "angle": random.choice([35, 42, 48, 55]), "rate": 45},
        {"type": "regular", "subtype": "reflection", "title": "Reflective Light Well Alignment",
         "d1": random.choice([6, 8, 10]), "d2": random.choice([9, 12, 15]),
         "angle": random.choice([38, 45, 52]), "rate": 50},
        {"type": "regular", "subtype": "solar_strut", "title": "Solar Array Support Strut (Cosine)",
         "run": random.choice([10, 12, 14, 16]), "angle": random.choice([25, 30, 35, 40]), "rate": 55},
        {"type": "regular", "subtype": "guy_wire", "title": "Structural Guy-Wire Cable (Sine)",
         "height": random.choice([15, 18, 20, 24]), "angle": random.choice([40, 45, 50, 55]), "rate": 40},
        {"type": "regular", "subtype": "slab", "title": "Garage Concrete Slab",
         "l": random.choice([20, 22, 24]), "w": random.choice([18, 20]), "thick": 0.5, "rate": 6},
    ]
    
    crisis_events = [
        {"type": "crisis", "subtype": "trench", "title": "🚨 CRISIS: Flash Flood Washout!",
         "desc": "Heavy rain washed out the access road! Fill this trapezoidal drainage trench with crushed gravel immediately to keep supply trucks moving.",
         "b1": random.choice([8, 10, 12]), "b2": random.choice([4, 6]),
         "depth": random.choice([3, 4, 5]), "length": random.choice([20, 25, 30]), "rate": 4},
        {"type": "crisis", "subtype": "gable", "title": "🚨 CRISIS: High Winds Tear Roof Sheathing!",
         "desc": "A sudden windstorm ripped the sheathing off the triangular front gable before shingles were installed! Order emergency weather-barrier panels before rain hits.",
         "base": random.choice([20, 24, 28]), "height": random.choice([8, 10, 12]), "rate": 9},
        {"type": "crisis", "subtype": "glare", "title": "🚨 CRISIS: Client Solar Glare Complaint!",
         "desc": "Afternoon sun is blinding the client's workspace! Build a custom horizontal roof overhang that casts the exact vertical shadow drop required to block the window.",
         "overhang": random.choice([4, 5, 6]), "angle": random.choice([48, 54, 60]), "rate": 65}
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
    st.session_state.exact_count = 0
    st.session_state.hints_used = 0
    st.session_state.hint_unlocked = {}

def reset_game():
    st.session_state.started = False
    st.session_state.idx = 0
    st.session_state.budget = 45000
    st.session_state.debt = 0
    st.session_state.days = 45
    st.session_state.reputation = 100
    st.session_state.queue = generate_project_queue()
    st.session_state.history = []
    st.session_state.exact_count = 0
    st.session_state.hints_used = 0
    st.session_state.hint_unlocked = {}

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
    You have **45 days** and **$45,000** to complete a 10-stage construction build.
    * **Regular Milestones (8):** Solve 2D area, 3D volume, right-triangle light angles, reflection, and sine/cosine strut/cable blueprints.
    * **Crisis Events (2):** Unexpected storms, washouts, and solar glare emergencies will strike!
    * **Free Formulas & Paid Engineer Hints:** Use the free Formula Sheet anytime, or hire a Senior Engineer (**-$250**) for a step-by-step walkthrough.
    * **Borrowing & Recovery:** Overruns trigger an **Emergency Line of Credit** (15% fee). Exact answers earn a **$750 Precision Bonus** that pays down debt!
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

    event = st.session_state.queue[st.session_state.idx]
    st.caption(f"CONTRACTOR: {st.session_state.student_name.upper()} | STAGE {st.session_state.idx + 1} OF {len(st.session_state.queue)}")
    
    if event["type"] == "crisis":
        st.subheader(event["title"])
        st.warning(event["desc"])
    else:
        st.subheader(f"🔨 Milestone: {event['title']}")

    sub = event["subtype"]
    
    if sub == "floor":
        st.write(f"Calculate the total area of the composite L-shaped room below. Flooring costs **${event['rate']}/sq ft**.")
        st.pyplot(draw_composite_floor(event["w1"], event["h1"], event["w2"], event["h2"]))
        correct = (event["w1"] * event["h1"]) + (event["w2"] * event["h2"])
        unit = "sq ft"
        tol = 0
        formula_txt = "**Area of Composite Rectangles:** Split into two rectangles: $A = (l_1 \times w_1) + (l_2 \times w_2)$"
        paid_hint_txt = f"1. Bottom rectangle: ${event['w1']} \times {event['h1']} = {event['w1']*event['h1']}$ sq ft.\n2. Top alcove rectangle: ${event['w2']} \times {event['h2']} = {event['w2']*event['h2']}$ sq ft.\n3. Add both areas together."

    elif sub == "piers":
        st.write(f"Calculate the total volume of concrete needed for **{event['qty']} cylindrical piers** (round to nearest whole cubic foot). Concrete costs **${event['rate']}/cu ft**.")
        st.pyplot(draw_cylinder_piers(event["diam"], event["depth"], event["qty"]))
        r = event["diam"] / 2
        correct = round(math.pi * (r ** 2) * event["depth"] * event["qty"])
        unit = "cu ft"
        tol = 2
        formula_txt = "**Volume of a Cylinder:** $V = \pi r^2 h$ (Remember: radius $r = \frac{\text{diameter}}{2}$)"
        paid_hint_txt = f"1. Find radius: $r = {event['diam']} \div 2 = {r}$ ft.\n2. Volume of 1 pier: $\pi \times ({r})^2 \times {event['depth']}$.\n3. Multiply by **{event['qty']} piers** and round to the nearest whole number."

    elif sub == "siding":
        st.write(f"Calculate the net wall area requiring siding (**subtract the windows**). Siding costs **${event['rate']}/sq ft**.")
        st.pyplot(draw_siding_wall(event["w"], event["h"], event["win_w"], event["win_h"], event["qty_win"]))
        correct = (event["w"] * event["h"]) - (event["qty_win"] * event["win_w"] * event["win_h"])
        unit = "sq ft"
        tol = 0
        formula_txt = "**Net Area:** $A_{\text{net}} = (W_{\text{wall}} \times H_{\text{wall}}) - (\text{Qty} \times W_{\text{window}} \times H_{\text{window}})$"
        paid_hint_txt = f"1. Total wall area: ${event['w']} \times {event['h']} = {event['w']*event['h']}$ sq ft.\n2. One window area: ${event['win_w']} \times {event['win_h']} = {event['win_w']*event['win_h']}$ sq ft.\n3. Subtract all **{event['qty_win']} windows** from the total wall area."

    elif sub == "slab":
        st.write(f"Pour a rectangular concrete slab measuring **{event['l']} ft long × {event['w']} ft wide × {event['thick']} ft (6 inches) thick**. Concrete costs **${event['rate']}/cu ft**.")
        correct = round(event["l"] * event["w"] * event["thick"])
        unit = "cu ft"
        tol = 0
        formula_txt = "**Volume of a Rectangular Prism:** $V = l \times w \times h$"
        paid_hint_txt = f"Multiply length × width × thickness in feet: ${event['l']} \times {event['w']} \times {event['thick']}$."

    elif sub == "clerestory":
        st.write(f"To illuminate a spot **{event['dist']} ft** across the floor when the sun is at a **{event['angle']}°** elevation angle, how high up the wall must the bottom of the clerestory window be? (Round to nearest whole foot; framing costs **${event['rate']}/ft**).")
        st.pyplot(draw_clerestory_window(event["dist"], event["angle"]))
        correct = round(event["dist"] * math.tan(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        formula_txt = "**Right-Triangle Tangent:** $\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}$ *(Ensure calculator is in DEGREE mode)*"
        paid_hint_txt = f"1. Relative to the {event['angle']}° angle, the window height is **Opposite** and {event['dist']} ft is **Adjacent**.\n2. Set up: $\tan({event['angle']}^\circ) = \frac{{h}}{{{event['dist']}}}$.\n3. Solve: $h = {event['dist']} \times \tan({event['angle']}^\circ)$."

    elif sub == "reflection":
        st.write(f"A sunbeam enters a skylight, hits a floor mirror **{event['d1']} ft** from the left wall at a **{event['angle']}°** angle, and reflects across **{event['d2']} ft** to hit a solar collector on the right wall. At what height does it hit the right wall? (Round to nearest whole foot; mounting costs **${event['rate']}/ft**).")
        st.pyplot(draw_light_reflection(event["d1"], event["d2"], event["angle"]))
        correct = round(event["d2"] * math.tan(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        formula_txt = "**Law of Reflection & Tangent:** Angle of incidence = Angle of reflection ($\theta$). Use $\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}$ on the right triangle."
        paid_hint_txt = f"1. By the Law of Reflection, the reflected angle with the floor on the right is also **{event['angle']}°**.\n2. Focus on the right-hand triangle with base **{event['d2']} ft**.\n3. Calculate: $\text{Height} = {event['d2']} \times \tan({event['angle']}^\circ)$."

    elif sub == "solar_strut":
        st.write(f"An angled solar panel support strut rises at **{event['angle']}°** across a horizontal roof base run of **{event['run']} ft**. Calculate the diagonal length (hypotenuse) of the steel strut needed (round to nearest whole foot; steel costs **${event['rate']}/ft**).")
        st.pyplot(draw_solar_strut(event["run"], event["angle"]))
        correct = round(event["run"] / math.cos(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        formula_txt = "**Right-Triangle Cosine:** $\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}$ *(Ensure calculator is in DEGREE mode)*"
        paid_hint_txt = f"1. Relative to {event['angle']}°, the {event['run']} ft roof base is **Adjacent** and the strut is the **Hypotenuse**.\n2. Set up: $\cos({event['angle']}^\circ) = \frac{{{event['run']}}}{{L}}$.\n3. Solve: $L = \frac{{{event['run']}}}{{\cos({event['angle']}^\circ)}}$."

    elif sub == "guy_wire":
        st.write(f"A vertical support post is **{event['height']} ft** tall. A diagonal guy-wire cable attaches to the top of the post and anchors to the ground at a **{event['angle']}°** angle. Calculate the required cable length (round to nearest whole foot; cable costs **${event['rate']}/ft**).")
        st.pyplot(draw_guy_wire(event["height"], event["angle"]))
        correct = round(event["height"] / math.sin(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        formula_txt = "**Right-Triangle Sine:** $\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}$ *(Ensure calculator is in DEGREE mode)*"
        paid_hint_txt = f"1. Relative to {event['angle']}°, the {event['height']} ft post is **Opposite** and the cable is the **Hypotenuse**.\n2. Set up: $\sin({event['angle']}^\circ) = \frac{{{event['height']}}}{{L}}$.\n3. Solve: $L = \frac{{{event['height']}}}{{\sin({event['angle']}^\circ)}}$."

    elif sub == "trench":
        st.write(f"Calculate the volume of gravel needed to fill this **{event['length']}-foot-long** trapezoidal trench. Gravel costs **${event['rate']}/cu ft**.")
        st.pyplot(draw_crisis_trench(event["b1"], event["b2"], event["depth"], event["length"]))
        correct = round(0.5 * (event["b1"] + event["b2"]) * event["depth"] * event["length"])
        unit = "cu ft"
        tol = 0
        formula_txt = "**Volume of a Trapezoidal Prism:** $V = \frac{1}{2}(b_1 + b_2) \times h \times \text{Length}$"
        paid_hint_txt = f"1. Trapezoid cross-section area: $0.5 \times ({event['b1']} + {event['b2']}) \times {event['depth']}$.\n2. Multiply that area by the trench length (**{event['length']} ft**)."

    elif sub == "gable":
        st.write(f"Calculate the triangular area of the damaged gable end to order weather-barrier panels. Panels cost **${event['rate']}/sq ft**.")
        st.pyplot(draw_crisis_gable(event["base"], event["height"]))
        correct = round(0.5 * event["base"] * event["height"])
        unit = "sq ft"
        tol = 0
        formula_txt = "**Area of a Triangle:** $A = \frac{1}{2} \times \text{base} \times \text{height}$"
        paid_hint_txt = f"Calculate $0.5 \times {event['base']} \times {event['height']}$."

    elif sub == "glare":
        st.write(f"A horizontal overhang extends **{event['overhang']} ft** out from the wall. When the sun shines down at a **{event['angle']}°** angle from the horizontal overhang, what vertical shadow drop does it cast down the wall? (Round to nearest whole foot; materials cost **${event['rate']}/ft**).")
        st.pyplot(draw_crisis_glare(event["overhang"], event["angle"]))
        correct = round(event["overhang"] * math.tan(math.radians(event["angle"])))
        unit = "ft"
        tol = 1
        formula_txt = "**Right-Triangle Tangent:** $\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}$"
        paid_hint_txt = f"1. Relative to {event['angle']}°, the vertical shadow drop is **Opposite** and the {event['overhang']} ft overhang is **Adjacent**.\n2. Calculate: $\text{Drop} = {event['overhang']} \times \tan({event['angle']}^\circ)$."

    # --- TWO-TIER HINT SYSTEM ---
    h_col1, h_col2 = st.columns(2)
    with h_col1:
        with st.expander("📐 Free Blueprint Formula Sheet"):
            st.markdown(formula_txt)
    with h_col2:
        stage_key = f"hint_{st.session_state.idx}"
        if st.session_state.hint_unlocked.get(stage_key, False):
            st.info(f"👷 **Engineer Walkthrough:**\n\n{paid_hint_txt}")
        else:
            if st.button("👷 Hire Engineer Hint (-$250)", key=f"btn_hint_{st.session_state.idx}"):
                st.session_state.hint_unlocked[stage_key] = True
                st.session_state.hints_used += 1
                st.session_state.budget -= 250
                if st.session_state.budget < 0:
                    shortfall = abs(st.session_state.budget)
                    st.session_state.debt += round(shortfall * 1.15)
                    st.session_state.budget = 0
                st.rerun()

    st.divider()

    # --- STUDENT INPUT & SUBMISSION ---
    user_ans = st.number_input(f"Enter your calculation ({unit}):", min_value=0, step=1, key=f"ans_{st.session_state.idx}")
    
    if st.button("Place Material Order 📦", key=f"btn_{st.session_state.idx}"):
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
    accuracy_pct = round((st.session_state.exact_count / len(st.session_state.queue)) * 100)
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    if net_profit > 0 and st.session_state.days >= 0 and st.session_state.debt == 0:
        st.balloons()
        rank = "MASTER CONTRACTOR"
        st.success(f"🏆 **{rank}!** You finished with **${net_profit:,}** net profit, **$0 debt**, and **{st.session_state.days} days** to spare!")
    elif net_profit > 0 and st.session_state.debt > 0:
        rank = "CRISIS SURVIVOR"
        st.warning(f"⚠️ **{rank}!** You finished with **${st.session_state.debt:,}** in remaining credit debt, leaving a net balance of **${net_profit:,}**.")
    else:
        rank = "BUDGET OVERRUN"
        st.error(f"📉 **{rank}!** Cost overruns and crisis events left your company **${abs(net_profit):,}** in the hole.")

    receipt_text = f"""========================================
   CONTRACTOR'S CRISIS - AUDIT RECEIPT
========================================
Contractor Name : {st.session_state.student_name}
Date Completed  : {timestamp}
Final Standing  : {rank}
----------------------------------------
Blueprint Accuracy : {st.session_state.exact_count}/{len(st.session_state.queue)} ({accuracy_pct}%)
Paid Hints Used    : {st.session_state.hints_used} (-${st.session_state.hints_used * 250:,})
Days Remaining     : {st.session_state.days} days
Client Reputation  : {st.session_state.reputation}%
----------------------------------------
Remaining Cash     : ${st.session_state.budget:,}
Credit Debt Owed   : ${st.session_state.debt:,}
NET PROJECT PROFIT : ${net_profit:,}
========================================
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
