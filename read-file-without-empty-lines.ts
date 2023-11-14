const fs = require("fs");

export default function readFileWithoutEmptyLines(filePath: string) {
  try {
    // Read the content of the file
    let content = fs.readFileSync(filePath, "utf-8");

    // Remove inline comments (#)
    content = content.replace(/#.*$/gm, "");

    // Remove empty lines
    content = content.replace(/^\s*[\r\n]/gm, "");

    // Join the non-empty lines back into a string
    // const newContent = nonEmptyLines.join("\n");
    console.log(content);
    return content;
  } catch (error: any) {
    console.error("Error:", error.message);
  }
}
