//json
$.getJSON("http://localhost:8080/Qtroid/json/tag_ranking", function(data) {
	tag_ranking = data;
	alert('json data : '+tag_ranking.1[0]);
});

$.getJSON("http://localhost:8080/Qtroid/json/trend_data", function(data) {
	trend_data = data;
	alert('json data : trend_data.json');
});

$.getJSON("http://localhost:8080/Qtroid/json/article_data", function(data) {
	article_data = data;
	alert('json data : article_data');
});

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
	//ランキングのボタン
	$('.tag_button').on('click', replaceArticle);

	//順位の内容
	// $('#button_1').text(tag_ranking.1[0]);
	// $('#button_2').text(tag_ranking.2[0]);
	// $('#button_3').text(tag_ranking.3[0]);
	// $('#button_4').text(tag_ranking.4[0]);
	// $('#button_5').text(tag_ranking.5[0]);
});
