//Navigation bar
function hideIconBar() {
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display: none;");
    navigation.classList.remove("hide");
}
function showIconBar() {
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display: block;");
    navigation.classList.add("hide");
}



function showComment() {
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.remove("hide");

}
// function hideComment() {
//     var commentArea = document.getElementById("comment-area");
//     commentArea.classList.add("hide");
// }
function showReply(id) {
    var replyArea = document.getElementById(id);
    replyArea.classList.remove("hide");

}
// function hideReply() {
//     var commentArea = document.getElementById("reply-area");
//     commentArea.classList.add("hide");
// }
