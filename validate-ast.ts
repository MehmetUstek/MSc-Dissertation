export default function validateAST(
  dockerFileFromAST: string,
  originalDockerFile: string
) {
  return dockerFileFromAST === originalDockerFile;
}
