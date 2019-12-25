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

@app.route('/get_tag_ranking')
def api_get_tag_ranking():
    qgr = get_qtroid()
    tag_ranking_data = qgr.get_tag_ranking()
    qgr.close_browser()
    return jsonify({
            'tag_ranking_data':tag_ranking_data
        })

@app.route('/get_tag_trend')
def api_get_tag_trend():
    qgr = get_qtroid()
    tag_trend_data = qgr.get_tag_ranking()
    qgr.close_browser()
    return jsonify({
            'tag_trend_data':tag_ranking_data
        })

@app.route('/get_article')
def api_get_article():
    qgr = get_qtroid()
    tag_ranking = qgr.get_tag_ranking()
    trend_data = qgr.get_trend_data(tag_ranking)
    article_data = qgr.get_article_data(trend_data)
    qgr.close_browser()
    return jsonify({
            'tag_trend_data':article_data
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)