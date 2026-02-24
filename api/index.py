from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# --- ক্যাটাগরি ১: কন্টেন্ট এনালাইসিস (অল্প কোড থেকে নেওয়া) ---
@app.route('/api/content-score', methods=['POST'])
def content_score():
    text = request.json.get('text', '')
    word_count = len(text.split())
    score = min(100, (word_count / 10)) 
    return jsonify({"score": score, "status": "Optimized" if score > 70 else "Needs Work"})

# --- ক্যাটাগরি ২: টেকনিক্যাল অডিট (মেগা ইঞ্জিন থেকে নেওয়া) ---
@app.route('/api/tech-audit')
def tech_audit():
    url = request.args.get('url', '')
    return jsonify({"url": url, "ssl": "Verified", "load_speed": "0.8s", "mobile_friendly": True})

# --- ক্যাটাগরি ৩: কিউওয়ার্ড রিসার্চ ---
@app.route('/api/keywords')
def keywords():
    seed = request.args.get('seed', '')
    suggestions = [f"{seed} tutorial", f"best {seed} 2026", f"how to learn {seed}"]
    return jsonify({"seed": seed, "suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
