from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# মেইন ড্যাশবোর্ড লোডার
@app.route('/')
def home():
    return render_template('index.html')

# --- ক্যাটাগরি ১: কন্টেন্ট এনালাইসিস ---
@app.route('/api/content-score', methods=['POST'])
def content_score():
    text = request.json.get('text', '')
    word_count = len(text.split())
    # এখানে আপনার BERT বা AI লজিক বসবে
    score = min(100, (word_count / 10)) 
    return jsonify({"score": score, "status": "Optimized" if score > 70 else "Needs Work"})

# --- ক্যাটাগরি ২: টেকনিক্যাল এসইও ---
@app.route('/api/tech-audit')
def tech_audit():
    url = request.args.get('url')
    # সিকিউরিটি ও স্পিড চেক লজিক
    return jsonify({"url": url, "ssl": "Active", "load_speed": "1.2s", "mobile_friendly": True})

# --- ক্যাটাগরি ৩: কিউওয়ার্ড ও ডাটা ---
@app.route('/api/keywords')
def keywords():
    seed = request.args.get('seed')
    # এটি আপনার ৭৮+ টুলের ডাটাবেস থেকে সাজেশন দিবে
    suggestions = [f"{seed} tutorial", f"best {seed} 2026", f"how to learn {seed}"]
    return jsonify({"seed": seed, "suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
