const tesseract = require("node-tesseract-ocr");
const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");

const file="prova.PNG"
const imgs = [path.join(__dirname, "prova.PNG")];

const config = {
  lang: "por",
  oem: 1,
  psm: 3,
};

async function main() {
  const textos = await tesseract.recognize(imgs, config);
  console.log(textos);

  const filePath = "./1.png";
  fs.writeFileSync(filePath, textos);
  console.log(`Texto salvo em: ${filePath}`);

  exec(`notepad.exe "${filePath}"`, (error) => {
    if (error) {
      console.error(`Erro ao abrir o arquivo: ${error}`);
      return;
    }
    console.log(`Arquivo aberto com sucesso: ${filePath}`);
  });
}

main();