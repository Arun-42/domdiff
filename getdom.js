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

 // Check if the node is a text node
 if (node.nodeType === Node.TEXT_NODE) {
     // If it is, add the text content to the result
     result += node.nodeValue;
 } else {
     // If it's not, check if the node has the class 'exclude'
     if (!isHidden(node)) {
         // If it doesn't, add the node's HTML to the result
         result += '<' + node.nodeName.toLowerCase();

         // Check if the node has attributes
         if (typeof node.hasAttributes === 'function' && node.hasAttributes()) {
             for (var i = 0; i < node.attributes.length; i++) {
                var attr = node.attributes[i];
                if (attr.value) {
                    result += ' ' + attr.name + '="' + attr.value + '"';
                }
             }
         }

         result += '>';

         // Recursively traverse the node's children
         for (var i = 0; i < node.childNodes.length; i++) {
             result += traverseDOM(node.childNodes[i]);
         }

         result += '</' + node.nodeName.toLowerCase() + '>';
     }
 }

 return result;
}

body = traverseDOM(document.body)






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

 // Check if the node is a text node
 if (node.nodeType === Node.TEXT_NODE) {
     // If it is, add the text content to the result
     result += node.nodeValue;
 } else {
     // If it's not, check if the node has the class 'exclude'
     if (!isHidden(node)) {
         // If it doesn't, add the node's HTML to the result
         result += '<' + node.nodeName.toLowerCase();

         // Check if the node has attributes
         if (typeof node.hasAttributes === 'function' && node.hasAttributes()) {
             for (var i = 0; i < node.attributes.length; i++) {
                var attr = node.attributes[i];
                if (attr.value) {
                    result += ' ' + attr.name + '="' + attr.value + '"';
                }
             }
         }

         result += '>';

         // Recursively traverse the node's children
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

// Set the button's properties
button.innerHTML = "Run Me";
button.style.position = "fixed";
button.style.top = "10px";
button.style.right = "10px";
button.style.zIndex = "999";

// Attach the 'runme' function to the button's click event
button.addEventListener("click", runme);

// Append the button to the body of the document
document.body.appendChild(button);

