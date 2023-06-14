
var screenWidth = window.screen.width;
var screenHeight = window.screen.height;

document.write("Screen resolution: " + screenWidth + "x" + screenHeight + "<br>");

document.documentElement.style.width = screenWidth + "px";
document.documentElement.style.height = screenHeight + "px";

class MediaFiles {
  constructor() {
    this.files = [];
  }

  readFiles() {
    const allowedExtensions = ['.png', '.jpg', '.webp', '.mp4', '.wav'];
    const folder = '../Video/';

    fetch(folder)
      .then(response => response.text())
      .then(data => {
        const parser = new DOMParser();
        const htmlDocument = parser.parseFromString(data, 'text/html');
        const links = htmlDocument.querySelectorAll('a');

        links.forEach(link => {
          const fileName = link.textContent;
          const fileExtension = fileName.slice(fileName.lastIndexOf('.'));

          if (allowedExtensions.includes(fileExtension)) {
            this.files.push(fileName);
          }
        });

        return this.files;
      });
  }
}

const mediaFiles = new MediaFiles();
mediaFiles.readFiles();

document.write(mediaFiles.readFiles + "<br>")
