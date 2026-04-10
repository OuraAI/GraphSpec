export const WEB_PLACEHOLDER_MESSAGE =
  "GraphSpec web placeholder: local visualization has not started yet.";

export function webHello(): string {
  return WEB_PLACEHOLDER_MESSAGE;
}

if (import.meta.main) {
  console.log(webHello());
}
