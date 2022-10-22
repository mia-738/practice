// 認証用インスタンス
var twitter = TwitterWebService.getInstance(
  'XXXXX',       // 作成したアプリケーションのConsumer Key
  'XXXXX'  // 作成したアプリケーションのConsumer Secret
);

// 認証
function authorize() {
  twitter.authorize();
}

// 認証解除
function reset() {
  twitter.reset();
}

// 認証後のコールバック
function authCallback(request) {
  return twitter.authCallback(request);
}

var sheetData = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("touhou");

var sheetData2 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("手動");

// 自動ツイート
function postUpdateTweet() {
  var cells = sheetData.getRange(2, 2, sheetData.getLastRow() - 1, 2).getValues();
  var randomValue = Math.random();

  var postMessage = "";
  for (var i = 0, il = cells.length; i < il; i++ ) {
    randomValue -= cells[i][1] / 100;
    if (randomValue < 0) {
      postMessage = cells[i][0];
      break;
    }
  }
  var service  = twitter.getService();
  var response = service.fetch('https://api.twitter.com/1.1/statuses/update.json', {
    method: 'post',
    payload: { status: postMessage }
  });
}


//　手動ツイート
function postTweet() {
  
  var service  = twitter.getService();
  var endPointUrl = 'https://api.twitter.com/1.1/statuses/update.json';
  var tweet = sheetData2.getRange('C3').getValue();

  var response = service.fetch(endPointUrl, {
    method: 'post',
    payload: {
      status: tweet,
    }
  });
}
