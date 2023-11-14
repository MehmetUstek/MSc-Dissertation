import { Instruction } from "dockerfile-ast";

//Outputs correct.
export default function createDockerFileFromAST(instructions: Instruction[]) {
  let str: string = "";
  for (let instruction of instructions) {
    str +=
      instruction.getInstruction() +
      " " +
      instruction
        .getArguments()
        .map((argument) => argument.getValue())
        .join(" ") +
      "\n";
  }
  console.log(str);
  return str;
}
