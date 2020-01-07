function getJSON(url) {
	var tmp;
  var req = new XMLHttpRequest();		  // XMLHttpRequest オブジェクトを生成する
  req.onreadystatechange = function() {		  // XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
    if(req.readyState == 4 && req.status == 200){ // サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合
			tmp = req.responseText;
    }
  };
  req.open("GET", url, false); // HTTPメソッドとアクセスするサーバーの　URL　を指定
	req.send(null);					    // 実際にサーバーへリクエストを送信
	return tmp;
}

//デバッグ
function alertp(){
	alert("ぴえん");
}

//要素いじる
function replaceArticle(){
    //ダミーの削除
    $('.dammy').remove();

		//要素の追加
		var article =
			'<div class="article">'+
			'<a class="user_Image" href="https://t.co/ORQKVSFkwD">'+
				'<img src ="./img/kindai.jpg" alt="user">'+
			'</a>'+
			'<div>'+
				'<a class="article_title" href="https://t.co/ORQKVSFkwD">近畿大学インスタはじめました！</a>'+
				'<div class="article_item">'+
					'<span class="good_count"></span>いいね999'+
				'</div>'+
				'<ul>参考URLリスト'+
					'<li>'+
						'<a href="https://t.co/ORQKVSFkwD">作成者</a>'+
					'</li>'+
					'<li>'+
						'<a href="https://t.co/ORQKVSFkwD">作成者</a>'+
					'</li>'+
				'</ul>'+
			'</div>'+
		'</div>';

		$('#goodRanking').append(article);

		// ${}
}

function replaceArticleEx(button_id, tag_name){ //button_1, python
	// 記事の判別
	// var str = $('.article').attr('class');
	// str = str.replace('article', '');

	//判定
	// if(str != tag_name){//ボタンと違う記事 削除 and 更新
		$('.article').remove();
	// }

	//trend_data取ってくる
	var trend_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/trend_data"));
	//tag_nameでfilter
	var trend_match_data = trend_data.filter(function(item, index){
		if(item.tag_name == tag_name) return true;
	});

	// ｊそんとる
	var article_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/article_data"));

	//記事本体
	var article='';
	var trend_len = trend_match_data.length;
	for(var i=trend_len; i > 0; i--){

		article =
		'<div class="article ' + tag_name +'">'+
			'<a class="user_Image" href="https://t.co/ORQKVSFkwD">'+
				'<img src ="./img/kindai.jpg" alt="user">'+
			'</a>'+
			'<div>'+
				'<a class="article_title" href='+ trend_match_data[i-1].trend_url +'>'+ trend_match_data[i-1].trend_title +'</a>'+
				'<div class="article_item">'+
					'<span class="good_count"></span>いいね '+ trend_match_data[i-1].like_count +
				'</div>'+
				'<ul>参考URLリスト';

		//記事urlを取ってくる
		//title de filer
		var url_match_data = article_data.filter(function(item, index){
			if(item.trend_title == trend_match_data[i-1].trend_title) return true;
		});
		//参考url
		var url_len = url_match_data.length;
		for(var j=0; j<url_len; j++){
			article +=
			'<li>'+
				'<a href="'+ url_match_data[j].link +'">'+ url_match_data[j].link +'</a>'+
			'</li>';
		}

		article +=
				'</ul>'+
			'</div>'+
		'</div>';

		$('#goodRanking').append(article);
	}


}// replaceArticleEx

//ロード
$(document).ready(function(){

	//json 読み込み
	var tag_ranking = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/tag_ranking"));
	// var trend_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/trend_data"));
	// var article_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/article_data"));

	//順位の内容
	$('#button_1').text(tag_ranking.ranking_1[0]);
	$('#button_2').text(tag_ranking.ranking_2[0]);
	$('#button_3').text(tag_ranking.ranking_3[0]);
	$('#button_4').text(tag_ranking.ranking_4[0]);
	$('#button_5').text(tag_ranking.ranking_5[0]);

	//ランキングのボタン
	$('.tag_button').on('click', function(){
		var id = $(this).attr("id");
		id = '#'+id;
		var tag_name = $(id).text();

		replaceArticleEx(id, tag_name); //button_1 python
	});

});
