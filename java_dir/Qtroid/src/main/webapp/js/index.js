// function getJSON() {
// 	var req = new XMLHttpRequest();						// XMLHttpRequest オブジェクトを生成する
// 	req.onreadystatechange = function() {				// XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
// 		if(req.readyState == 4 && req.status == 200){	// サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合

// 			var data = JSON.parse(req.responseText);	// 取得した JSON ファイルの中身を変数へ格納
// 			var len = data.length;						// JSON のデータ数を取得

// 			// JSON のデータ数分処理
// 			for(var i=0; i<len; i++) {
// 				console.log("id: " + data[i].id + ", name: " + data[i].name);
// 			}

// 		}
// 	};
// 	req.open("GET", "sample.json", false);				// HTTPメソッドとアクセスするサーバーのURLを指定
// 	req.send(null);										// 実際にサーバーへリクエストを送信
// }

// jsonとてくる
$.getJSON("test.json", function(data, status) { //url,callback
		alert("Json data:" + tag-ranking.tag-id[1].tag-name); //タグランキング1位を取ってこれるはず
	});

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

// load aboutpage
function loadWhat(){
	var $content = $('#wrapperArea');

	$content.fadeOut(600, function() {
		getPage("about.html")
	});
}

// ajax
function getPage(elm){
	$.ajax({
		type: 'GET',
		url: elm,
		dataType: 'html',
		success: function(data){
			$content.html(data).fadeIn(600);
		},
		error: function(){
			alertp();
		}
	});
}


window.addEventListener("load", function() {
	//ランキングのボタン
	var rank1ButtonElement = document.getElementById("button_1");
	rank1ButtonElement.addEventListener("click", replaceArticle, false);

	// var whatButton = document.getElementById("what");
	// whatButton.addEventListener("click", loadWhat, false);
}, false);
