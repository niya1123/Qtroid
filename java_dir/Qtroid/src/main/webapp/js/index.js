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
    $('.article_dammy').remove();

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

function replaceArticleEx(button_id){ //button_1
	if()
	//ダミーの削除
	$('.article_dammy').remove();

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

//ロード
$(document).ready(function(){

	//json 読み込み
	var tag_ranking = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/tag_ranking"));
	var trend_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/trend_data"));
	var article_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/article_data"));

	//順位の内容
	$('#button_1').text(tag_ranking.ranking_1[0]);
	$('#button_2').text(tag_ranking.ranking_2[0]);
	$('#button_3').text(tag_ranking.ranking_3[0]);
	$('#button_4').text(tag_ranking.ranking_4[0]);
	$('#button_5').text(tag_ranking.ranking_5[0]);

	//ランキングのボタン
	$('.tag_button').on('click', function(){
		var id = $(this).attr("id");
		replaceArticle(id); //button_1
	});

	//記事の設定
	// $('#button_1').on('click', function(){
		
	// });
});
