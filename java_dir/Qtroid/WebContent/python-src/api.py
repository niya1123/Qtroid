from flask import Flask, jsonify
import qtroid

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま


def get_qtroid():
    return qtroid.QiitaGetRanking()

@app.route('/')
def index():
    return "Hello world!!"

@app.route('/api/get_tag_ranking')
def api_get_tag_ranking():
    qgr = get_qtroid()
    tag_ranking_data = qgr.get_tag_ranking()
    qgr.close_browser()
    return jsonify({
            'tag_ranking_data':tag_ranking_data
        })

@app.route('/api/get_tag_trend')
def api_get_tag_trend():
    qgr = get_qtroid()
    tag_trend_data = qgr.get_tag_ranking()
    qgr.close_browser()
    return jsonify({
            'tag_trend_data':tag_ranking_data
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)