function run() {
    
}

function hambergerNav() {
    var top_nav = document.getElementById("myTopnav")
    if (top_nav.className === "topnav") {
        top_nav.className += "responsive";
    } else {
        top_nav.className = "topnav"
    }
}

run()