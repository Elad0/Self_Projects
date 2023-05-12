 async function playGame(board, playerTurn){

while(true){
let modifiedBoard=board;
var bigBoard=board;
let boardState=null;

	while(boardState===null){
		if(!playerTurn){
			
			modifiedBoard=await aiPlayersTurn(board);
			
		}
		else{
			modifiedBoard= await humanPlayersTurn(board);
			
		}

		displayBoard(modifiedBoard);
		playerTurn=!playerTurn;
		boardState=await verifyBoardThroughDjango(modifiedBoard);
		board=modifiedBoard;
	}

 winner(boardState);
var board =[
			[" ", " ", " "], 
			[" ", " ", " "], 
			[" ", " ", " "], 
		];
}
}
async function aiPlayersTurn(board){
	
let modifiedBoard=await sendAndRecieveBoardFromDjango(board);
if(typeof modifiedBoard=== "undefined"){
	modifiedBoard=[
			[" ", " ", " "], 
			[" ", " ", " "], 
			[" ", " ", " "], 
		]; 
}
return modifiedBoard;
}

const winner=(winner)=>{
	window.alert(winner + " won");
}

async function humanPlayersTurn(board) {
  return new Promise((resolve, reject) => {
    const cells = document.querySelectorAll(".cell");
    cells.forEach((cell) => {
	if (cell.classList.contains("O")) {
		
	}else{
		cell.addEventListener("click", function onClick(event) {
        const row = parseInt(event.target.dataset.row);
        const col = parseInt(event.target.dataset.col);
        if (board[row][col] === " ") {
          cells.forEach((cell) => cell.removeEventListener("click", onClick));
          board[row][col]="X";
          resolve(board);
        }
      }  );
	}
    
    });
  });
}


async function sendAndRecieveBoardFromDjango(board) {
	return new Promise((resolve,reject)=>{
	  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/process-board/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4){
		if(xhr.status === 200) {
     // console.log('Board sent to Django');
      const jsonResponse = JSON.parse(xhr.responseText);
      //console.log("Board recived from Django")
      resolve(jsonResponse.board);
    }
    else{
	reject(new Error('Failed to send board at this time, please try again later'));
}
}
  };

  xhr.send(JSON.stringify({board: board}));	
	});

}

const verifyBoardThroughDjango= async (board)=>{
		return new Promise((resolve,reject)=>{
	  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/check-board-for-winner-board/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4){
		if(xhr.status === 200) {
     // console.log('Board sent to Django');
      const jsonResponse = JSON.parse(xhr.responseText);
     // console.log("Board recived from Django")
      resolve(jsonResponse.Winner);
    }
    else{
	reject(new Error('Failed to send board at this time, please try again later'));
}
}
  };

  xhr.send(JSON.stringify({board: board}));	
	});
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function displayBoard(board) {
  var boardContainer = document.getElementById("board");
  boardContainer.innerHTML = "";
  for (var i = 0; i < board.length; i++) {
    var row = document.createElement("div");
    row.className = "row";
    for (var j = 0; j < board[i].length; j++) {
      var cell = document.createElement("div");
      cell.className = "cell " + board[i][j];
      cell.dataset.row = i;
      cell.dataset.col = j;
      row.appendChild(cell);
    }
    boardContainer.appendChild(row);
  }
}


