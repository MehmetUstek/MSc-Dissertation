import * as fs from "fs";
import * as path from "path";
import { DockerfileParser } from "dockerfile-ast";
import createDockerFileFromAST from "./create-docker-file-from-ast";
import readFileWithoutEmptyLines from "./read-file-without-empty-lines";
import validateAST from "./validate-ast";

type localInstruction = {
  instruction: string;
  arguments: any[];
};
type DockerfileStructure = {
  instructions: localInstruction[];
};

const dockerfileContent = fs.readFileSync("example.Dockerfile", "utf-8");
let dockerfile = DockerfileParser.parse(dockerfileContent);
let instructions = dockerfile.getInstructions();
let dockerfileStructure: localInstruction[] = [];
for (let instruction of instructions) {
  //   console.log(instruction.getKeyword());
  //   console.log(instruction.getInstruction());
  // console.log(instruction.getArguments());

  dockerfileStructure.push({
    instruction: instruction.getInstruction(),
    arguments: instruction.getArguments(),
  });
}

const dockerFileFromAST = createDockerFileFromAST(instructions);
const originalDockerFile = readFileWithoutEmptyLines("example.Dockerfile");
console.log(validateAST(dockerFileFromAST, originalDockerFile));

// console.log(dockerfileStructure);
const jsonString = JSON.stringify(dockerfileStructure, null, 2); // The third parameter (2) is for indentation

const filePath = path.join(__dirname, "output.json");

fs.writeFileSync(filePath, jsonString, "utf-8");

console.log(`JSON data has been saved to: ${filePath}`);
