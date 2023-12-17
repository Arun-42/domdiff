function isHidden(el) {
    try{
    var style = window.getComputedStyle(el);
    return ((style.display === 'none') || (style.visibility === 'hidden'))}
    catch{
        console.warn(el)
        return 0;
    }
}

function traverseDOM(node) {
 var result = '';

 if (node.nodeType === Node.TEXT_NODE) {
     result += node.nodeValue;
 } else {
     if (!isHidden(node)) {
         result += '<' + node.nodeName.toLowerCase();

         if (typeof node.hasAttributes === 'function' && node.hasAttributes()) {
             for (var i = 0; i < node.attributes.length; i++) {
                var attr = node.attributes[i];
                if (attr.value) {
                    result += ' ' + attr.name + '="' + attr.value + '"';
                }
             }
         }

         result += '>';

         for (var i = 0; i < node.childNodes.length; i++) {
             result += traverseDOM(node.childNodes[i]);
         }

         result += '</' + node.nodeName.toLowerCase() + '>';
     }
 }

 return result;
}

runme = () => {
  let td = traverseDOM(document.body); 
  td = td.replace(/^\s*\n/gm, "");
  navigator.clipboard.writeText(td);
}


button = document.createElement("button");

button.innerHTML = "Copy HTML";
button.style.position = "fixed";
button.style.top = "10px";
button.style.right = "10px";
button.style.zIndex = "999";

button.addEventListener("click", runme);

document.body.appendChild(button);

