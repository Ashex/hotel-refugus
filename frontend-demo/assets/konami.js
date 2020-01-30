//Long story short: Create a listener that listens for the Konami code,
//then make the element 'dirtylittlesecret' visible and replace the invisible 'dirtylittlesecret' div with
// the music player that plays the song

var isInternetExplorer = navigator.appName.indexOf("Microsoft") != -1;
var bShowing=false;
function showKonami() {
    if(bShowing) return;
	setTimeout(function() {toggleVisibility();},500);
	ReplaceContentInContainer('secret','<audio controls="controls" loop="loop" autoplay="autoplay"><source src="./assets/nyan.mp3" type="audio/mp3" />></audio>');
    bShowing=true;

}

var kkeys = [];
var konamiString = "38,38,40,40,37,39,37,39,66,65";
// up, up, down, down, left, right, left, right, B, A

function setupStuff() {
    if (window.addEventListener) {
        //alert("firefox");
        window.addEventListener('keydown', function(e) {
            kkeys.push(e.keyCode );
            if (kkeys.toString().indexOf(konamiString) >= 0 )
                showKonami();
        }, true)
    }
    else if(document.body.attachEvent) {
        //alert("ie detected");
	    document.body.attachEvent('onkeydown', function(e){
            kkeys.push(e.keyCode);
            if (kkeys.toString().indexOf(konamiString) >= 0)
                showKonami();
	    }, true)
    }
}

function toggleVisibility() {
document.getElementById("kc").style.display = "block";
}

function ReplaceContentInContainer(id,content) {
var container = document.getElementById(id);
container.innerHTML = content;
}
