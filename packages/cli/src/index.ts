import { CORE_PLACEHOLDER_MESSAGE } from "@graphspec/core";
import { WEB_PLACEHOLDER_MESSAGE } from "@graphspec/web";

export interface CliIo {
  error(message: string): void;
  log(message: string): void;
}

const defaultIo: CliIo = {
  error(message) {
    console.error(message);
  },
  log(message) {
    console.log(message);
  },
};

export async function runCli(
  argv: string[],
  io: CliIo = defaultIo,
): Promise<number> {
  io.log("GraphSpec CLI placeholder");
  io.log(`args: ${argv.join(" ") || "(none)"}`);
  io.log(CORE_PLACEHOLDER_MESSAGE);
  io.log(WEB_PLACEHOLDER_MESSAGE);
  io.log("Real commands will be implemented after the workflow and spec process settle.");
  return 0;
}
