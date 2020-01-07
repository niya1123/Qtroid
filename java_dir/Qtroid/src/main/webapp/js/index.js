var tag_ranking;

function getJSON(url) {
	var tmp;
  var req = new XMLHttpRequest();		  // XMLHttpRequest オブジェクトを生成する
  req.onreadystatechange = function() {		  // XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
    if(req.readyState == 4 && req.status == 200){ // サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合
			// alert(req.responseText);		          // 取得した JSON ファイルの中身を表示
			tmp = req.responseText;
    }
  };
  req.open("GET", url, false); // HTTPメソッドとアクセスするサーバーの　URL　を指定
	req.send(null);					    // 実際にサーバーへリクエストを送信
	return tmp;
}

//json
// var tag_ranking
// function setPreference(){
// 	$.ajaxSetup({async: false});//同期通信(json取ってくるまで待つ)
// 	$.getJSON("http://localhost:8080/Qtroid/json/tag_ranking", function(data){
// 		tag_ranking = data.param;
// 	});
// 	$.ajaxSetup({async: true});
// 	alert(tag_ranking.ranking_1[0]);
// }

// $.getJSON("http://localhost:8080/Qtroid/json/trend_data", function(data) {
// 	trend_data = data;
// 	alert('json data : trend_data.json');
// });

// $.getJSON("http://localhost:8080/Qtroid/json/article_data", function(data) {
// 	article_data = data;
// 	alert('json data : article_data');
// });

// jsonとてくる
// $.getJSON("http://localhost:8080/Qtroid/json/tag_ranking", function(data, status) { //url,callback
// 		alert("Json data:" + tag-ranking.tag-id[1].tag-name); //タグランキング1位を取ってこれるはず
// 	});

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

// // load aboutpage
// function loadWhat(){
// 	var $content = $('#wrapperArea');

// 	$content.fadeOut(600, function() {
// 		getPage("about.html")
// 	});
// }

// // ajax
// function getPage(elm){
// 	$.ajax({
// 		type: 'GET',
// 		url: elm,
// 		dataType: 'html',
// 		success: function(data){
// 			$content.html(data).fadeIn(600);
// 		},
// 		error: function(){
// 			alertp();
// 		}
// 	});
// }

//ロード
$(document).ready(function(){

	//json 読み込み
	var tag_ranking = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/tag_ranking"));
	var trend_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/trend_data"));
	var article_data = JSON.parse(getJSON("http://localhost:8080/Qtroid/json/article_data"));

	//ランキングのボタン
	$('.tag_button').on('click', replaceArticle);

	//順位の内容
	$('#button_1').text(tag_ranking.ranking_1[0]);
	$('#button_2').text(tag_ranking.ranking_2[0]);
	$('#button_3').text(tag_ranking.ranking_3[0]);
	$('#button_4').text(tag_ranking.ranking_4[0]);
	$('#button_5').text(tag_ranking.ranking_5[0]);
});
