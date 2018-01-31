var style = "style-ebook";
var size = "size-large";
var margin = "margin-narrow";

var baseHref = window.location.toString().match(/.*\//);


var linkStringStart = "javascript:(function(){";
var linkStringEnd   = "';_readability_script=document.createElement('SCRIPT');_readability_script.type='text/javascript';_readability_script.src='" + baseHref + "js/readability.js?x='+(Math.random());document.getElementsByTagName('head')[0].appendChild(_readability_script);_readability_css=document.createElement('LINK');_readability_css.rel='stylesheet';_readability_css.href='" + baseHref + "css/readability.css';_readability_css.type='text/css';_readability_css.media='screen';document.getElementsByTagName('head')[0].appendChild(_readability_css);_readability_print_css=document.createElement('LINK');_readability_print_css.rel='stylesheet';_readability_print_css.href='" + baseHref + "css/readability-print.css';_readability_print_css.media='print';_readability_print_css.type='text/css';document.getElementsByTagName('head')[0].appendChild(_readability_print_css);})();";


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setCheckedValue(radioObj, newValue) {
	if(!radioObj)
		return;
	var radioLength = radioObj.length;
	if(radioLength == undefined) {
		radioObj.checked = (radioObj.value == newValue.toString());
		return;
	}
	for(var i = 0; i < radioLength; i++) {
		radioObj[i].checked = false;
		if(radioObj[i].value == newValue.toString()) {
			radioObj[i].checked = true;
		}
	}
}

$(document).ready(function() {
						   
	$("#bookmarkletLink").attr("href", linkStringStart + "readStyle='" + style + "';readSize='" + size + "';readMargin='" + margin + linkStringEnd);
	
	function applyChange(s,y) {
		var example = document.getElementById("example");
		var article = document.getElementById("articleContent");
		var fullbody = document.getElementById("fullBody");
	

		switch(s){
			case "style":
				style = y;
				setCookie( "style", y, 9999 );
				break
			case "size":
				size = y;
				setCookie( "size", y, 9999 );
				break
			case "margin":
				margin = y;
				setCookie( "margin", y, 9999 );
				break
			case "background":
				background = y;
				setCookie( "background", y, 9999 );
				break
		}
		example.className = style;
		article.className = margin + " " + size;
		fullbody.className = background;
		$("#bookmarkletLink").attr("href", linkStringStart + "readStyle='" + style + "';readSize='" + size + "';readMargin='" + margin + linkStringEnd);
	}

	// READ COOKIES TO RESTORE SETTINGS OF RADIO BUTTONS
	var style = getCookie( "style" ) ? getCookie( "style" ) : "style-ebook";
	var size = getCookie( "size" ) ? getCookie( "size" ) : "size-large";
	var margin = getCookie( "margin" ) ? getCookie( "margin" ) : "margin-narrow";
	var background = getCookie( "background" ) ? getCookie( "background" ) : "background-none";

	var buttons = $("#settings input" );
	var numButtons = buttons.length;
	for(var i = 0; i < numButtons; i++) {
		var currentButton = buttons[i];
		switch( currentButton.name ) {
			case "style":
				setCheckedValue( currentButton, style );
				break
			case "size":
				setCheckedValue( currentButton, size )
				break
			case "margin":
				setCheckedValue( currentButton, margin )
				break
			case "background":
				setCheckedValue( currentButton, background )
				break
		}
	}
	
	var example = document.getElementById("example");
	var article = document.getElementById("articleContent");
	var fullbody = document.getElementById("fullBody");
	example.className = style;
	article.className = margin + " " + size;
	fullbody.className = background;

	// BIND FUNCTIONS TO RADIO BUTTONS
	$("#settings input").bind("click", function(){
		applyChange(this.name, this.value);
	});
	$("#settings input").bind("click", function(){
		applyChange(this.name, this.value);
	});
	$("#bookmarkletLink").bind("click", function(){
		if($.browser.msie){
			alert("To start using Readability, right-click and select 'Add To Favorites...' to save this link to your browser's bookmarks toolbar.");
		}
		else {
			alert("To start using Readability, drag this link to your browser's bookmarks toolbar.");
		}
		return false;
	});

});

