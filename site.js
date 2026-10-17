document.getElementById("yr").textContent = new Date().getFullYear();

// Gallery: list your project photos here (put files in assets/). Empty slots show a placeholder.
var PHOTOS = [
  // { src: "assets/project1.jpg", alt: "New front yard sprinkler install" },
];
(function () {
  var g = document.getElementById("gallery");
  if (!g || !PHOTOS.length) return;
  document.getElementById("work").hidden = false;
  var n = PHOTOS.length;
  for (var i = 0; i < n; i++) {
    var d = document.createElement("div");
    d.className = "shot";
    if (PHOTOS[i]) {
      var im = document.createElement("img");
      im.src = PHOTOS[i].src; im.alt = PHOTOS[i].alt || "Sprinkler project"; im.loading = "lazy";
      d.appendChild(im);
    } else {
      d.className += " empty"; d.textContent = "Project photo";
    }
    g.appendChild(d);
  }
})();

var f = document.getElementById("contact-form");
if (f) f.addEventListener("submit", function (e) {
  e.preventDefault();
  var v = function (k) { return f.elements[k].value; };
  var body = "Name: " + v("name") + "\nPhone: " + v("phone") + "\nEmail: " + v("email") +
             "\nTown/ZIP: " + v("town") + "\nService: " + v("service") + "\n\n" + v("msg");
  location.href = "mailto:info@example.com?subject=" + encodeURIComponent("Estimate request: " + v("service")) +
                  "&body=" + encodeURIComponent(body);
});
