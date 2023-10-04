// Get ToC div
let toc = document.getElementById("ToC");

// Add a header
let tocHeader = document.createElement("h5");
tocHeader.innerText = "Table of Contents";
toc.appendChild(tocHeader);

// Create a list for the ToC entries
let tocList = document.createElement("ul");
tocList.className = "toc";

// Get the h2 and h3 tags - ToC entries
let headers = document.querySelectorAll("h2, h3");

// For each header
for (let i = 0; i < headers.length; i++) {
    // Create an id
    let name = "header" + i;
    headers[i].id = name;

    // a list item for the entry
    let tocListItem = document.createElement("li");

    // style the li according to the header level
    if (headers[i].nodeName === "H2") {
        tocListItem.style.marginLeft = "0";
    } else if (headers[i].nodeName === "H3") {
        tocListItem.style.marginLeft = "20px";
    }

    // a link for the header
    let tocEntry = document.createElement("a");
    tocEntry.setAttribute("href", "#" + name);
    tocEntry.innerText = headers[i].innerText;

    tocListItem.appendChild(tocEntry);
    tocList.appendChild(tocListItem);
}
toc.appendChild(tocList);