
function checkBoardForWinner() {
	  // Get all the cells on the board
	  var cells = document.querySelectorAll(".cell");

	  // Check for a horizontal win
	  for (var i = 0; i < cells.length; i += 3) {
	    if (
	      cells[i].dataset.value &&
	      cells[i].dataset.value === cells[i + 1].dataset.value &&
	      cells[i + 1].dataset.value === cells[i + 2].dataset.value
	    ) {
	      window.alert(cells[i].dataset.value + " wins!")
	      return true;
	    }
	  }

	  // Check for a vertical win
	  for (var i = 0; i < 3; i++) {
	    if (
	      cells[i].dataset.value &&
	      cells[i].dataset.value === cells[i + 3].dataset.value &&
	      cells[i + 3].dataset.value === cells[i + 6].dataset.value
	    ) {
	      window.alert(cells[i].dataset.value + " wins!");
	      return true;
	    }
	  }

	  // Check for a diagonal win
	  if (
	    cells[0].dataset.value &&
	    cells[0].dataset.value === cells[4].dataset.value &&
	    cells[4].dataset.value === cells[8].dataset.value
	  ) {
	    window.alert(cells[0].dataset.value + " wins!")
	    return true;
	  }

	  if (
	    cells[2].dataset.value &&
	    cells[2].dataset.value === cells[4].dataset.value &&
	    cells[4].dataset.value === cells[6].dataset.value
	  ) {
	    window.alert(cells[2].dataset.value + " wins!");
	    return true;
	  }
	  
	  var tie = true;
	  
	  for (var i = 0; i < cells.length; i++) {
	    if (!cells[i].dataset.value) {
	      tie = false;
	      break;
	    }
	  }
	  
	  if(tie){
		  window.alert("Tie, no one wins");
		  return true;
	  }
	  
	  return false;
	
}


function buttonClickDifficultyHandler() {
	addButtons();
	var normalButton = document.querySelector("#Normal");
 	var hardButton = document.querySelector("#Hard");
  	var avocadoButton = document.querySelector("#Avocado");
	

  var difficulty = -1;
  let buttonClicked = false;

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  async function waitForClick() {
    while (!buttonClicked) {
      await sleep(100);
    }
    return difficulty;
  }

  normalButton.addEventListener("click", function() {
    difficulty = 0;
    cleanUpButtons()
    buttonClicked = true;
  });

  hardButton.addEventListener("click", function() {
    difficulty = 1;
    cleanUpButtons()
    buttonClicked = true;
  });

  avocadoButton.addEventListener("click", function() {
    difficulty = 2;
    cleanUpButtons()
    buttonClicked = true;
  });

  applyDifficulty(difficulty);
  return waitForClick();
}

function applyDifficulty(difficulty){
	if(difficulty===1){
		document.getElementById("board").classList.add("spin");
		sillyBackground(1);
	}
	if(difficulty===2){
		sillyBackground(2);
	}	
}

function cleanUpButtons(){
	var normalButton = document.getElementById("Normal");
  	var hardButton = document.getElementById("Hard");
  	var avocadoButton = document.getElementById("Avocado");
  	
  	normalButton.remove();
  	hardButton.remove();
  	avocadoButton.remove();
  	container.innerHTML = "";
}

function addButtons() {
  // Get an existing element to which you want to append the new button
  const container = document.getElementById("container");

  // Create a new button element
  const newButton = document.createElement("button");
  newButton.id="Normal";
  newButton.textContent = "Normal";

  container.appendChild(newButton);
  
  const newButton2 = document.createElement("button");
  newButton2.id="Hard";
  newButton2.textContent = "Hard";
  
  container.appendChild(newButton2);
  
  const newButton3 = document.createElement("button");
  newButton3.id="Avocado";
  newButton3.textContent = "Avocado";
  
  container.appendChild(newButton3);
  
}

const randomColor=()=>{
  var color = Math.floor(Math.random() * 16777215).toString(16);
  return "#" + ("000000" + color).slice(-6);
}

const avocado=()=>{
const avocados = [
  "url(/static/tictactoe/images/Avocado1.jpg)",
  "url(/static/tictactoe/images/Avocado2.jpg)",
  "url(/static/tictactoe/images/Avocado3.jpg)",
  "url(/static/tictactoe/images/Avocado4.jpg)",
  "url(/static/tictactoe/images/Approved.jpeg)"
];

 
 return avocados[Math.floor(Math.random()*avocados.length)];
}

let interval;
function sillyBackground(difficulty){
	const body = document.body;
	let colorIndex = 0;
	var selector;
	
	if(difficulty===1){
		selector = [randomColor(), randomColor(), randomColor(), randomColor(),randomColor(), randomColor()];
	}
	if(difficulty===2){
		selector = [avocado(), avocado(), avocado(), avocado(),avocado(), avocado()];
	}

// Use setInterval to change the background color every 1 second
interval=setInterval(function() {
	//if difficulty is 1 then we change color
	if(difficulty==1){
  	// Get the color from the colors array
  	const color = selector[colorIndex];
  	// Change the background color of the body element
  	body.style.backgroundColor = color;
  }
  
  //if difficulty is 2 then change background image
  if(difficulty==2){
	console.log(selector[colorIndex]);
	body.style.backgroundImage=selector[colorIndex];
}

  // Increment the color index, and loop back to the start of the array if we reach the end
  colorIndex = (colorIndex + 1) % selector.length;
}, 500);
}

//TODO figure out after reset how to go to new difficulty

async function game(){
	//determine the difficulty
	 const difficulty = await buttonClickDifficultyHandler();
	//Create the TicTacToe board
	var board = document.getElementById("board");
	var currentPlayer = "X"; // initialize current player to X
	var ended=false;
	for (var i = 0; i < 3; i++) {
  		var row = document.createElement("div");
  		for (var j = 0; j < 3; j++) {
    		var cell = document.createElement("button");
    		cell.className = "cell";
    		cell.id = i + "_" + j;
    		
    		cell.addEventListener("click", function() {
				beep();
				
    	 	if(ended){
       	  		window.alert("The game has ended, restarting");
       	  		ended=false;
       	  		currentPlayer="X";
       	  		resetBoard();
       	  		difficulty= buttonClickDifficultyHandler();
       	  		
         	}
    	 
    	 if (this.dataset.clicked == "true") {
    		 window.alert("Cell has already been selected");
    		return; // Exit the function if cell has already been clicked
    	}
    	 this.dataset.clicked="true";
    	 
    	 
      // Handle the cell click event
      console.log("Cell clicked: " + this.id);
      if (currentPlayer === "X") {
        this.setAttribute("data-value", "X");
        this.classList.add("X"); 
        this.style.backgroundImage = "url('/static/tictactoe/images/Avocado.jpg')";
        this.style.backgroundSize = 'cover';
        currentPlayer = "O";
      } else {
        this.setAttribute("data-value", "O");
        this.classList.add("O");
         this.style.backgroundImage = `url(${"/static/tictactoe/images/Approved.jpeg"})`;
         this.style.backgroundSize = 'cover';
        currentPlayer = "X";
      }
      
      if (checkBoardForWinner(board)) {
		clearInterval(interval);
    	  ended=true
      }  
    });

    row.appendChild(cell);
  }
  board.appendChild(row);
}
applyDifficulty(difficulty);





}



function resetBoard() {
//  var cells = document.querySelectorAll(".cell");
//  for (var i = 0; i < cells.length; i++) {
//    cells[i].removeAttribute("data-value");
//    cells[i].removeAttribute("data-clicked");
//    cells[i].style.backgroundImage="none";
//    cells[i].classList.remove("X");
//    cells[i].classList.remove("O");
//  }
// document.getElementById('board').classList="";
//  document.body.style.backgroundImage="";
//  document.body.style.backgroundColor= "#ffffff";
   location.reload();
}

function beep() {
    var snd = new Audio("data:audio/wav;base64,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qJrx4KOQjahZxWbcZgztj2c49nKmkId44S71j0c8eV9yDK6uPRzx5X18eDvjvQ6yKo9ZSS6l//8elePK/Lf//IInrOF/FvDoADYAGBMGb7FtErm5MXMlmPAJQVgWta7Zx2go+8xJ0UiCb8LHHdftWyLJE0QIAIsI+UbXu67dZMjmgDGCGl1H+vpF4NSDckSIkk7Vd+sxEhBQMRU8j/12UIRhzSaUdQ+rQU5kGeFxm+hb1oh6pWWmv3uvmReDl0UnvtapVaIzo1jZbf/pD6ElLqSX+rUmOQNpJFa/r+sa4e/pBlAABoAAAAA3CUgShLdGIxsY7AUABPRrgCABdDuQ5GC7DqPQCgbbJUAoRSUj+NIEig0YfyWUho1VBBBA//uQZB4ABZx5zfMakeAAAAmwAAAAF5F3P0w9GtAAACfAAAAAwLhMDmAYWMgVEG1U0FIGCBgXBXAtfMH10000EEEEEECUBYln03TTTdNBDZopopYvrTTdNa325mImNg3TTPV9q3pmY0xoO6bv3r00y+IDGid/9aaaZTGMuj9mpu9Mpio1dXrr5HERTZSmqU36A3CumzN/9Robv/Xx4v9ijkSRSNLQhAWumap82WRSBUqXStV/YcS+XVLnSS+WLDroqArFkMEsAS+eWmrUzrO0oEmE40RlMZ5+ODIkAyKAGUwZ3mVKmcamcJnMW26MRPgUw6j+LkhyHGVGYjSUUKNpuJUQoOIAyDvEyG8S5yfK6dhZc0Tx1KI/gviKL6qvvFs1+bWtaz58uUNnryq6kt5RzOCkPWlVqVX2a/EEBUdU1KrXLf40GoiiFXK///qpoiDXrOgqDR38JB0bw7SoL+ZB9o1RCkQjQ2CBYZKd/+VJxZRRZlqSkKiws0WFxUyCwsKiMy7hUVFhIaCrNQsKkTIsLivwKKigsj8XYlwt/WKi2N4d//uQRCSAAjURNIHpMZBGYiaQPSYyAAABLAAAAAAAACWAAAAApUF/Mg+0aohSIRobBAsMlO//Kk4soosy1JSFRYWaLC4qZBYWFRGZdwqKiwkNBVmoWFSJkWFxX4FFRQWR+LsS4W/rFRb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VEFHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU291bmRib3kuZGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAwNGh0dHA6Ly93d3cuc291bmRib3kuZGUAAAAAAAAAACU=");  
    snd.play();
}
