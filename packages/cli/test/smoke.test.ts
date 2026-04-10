import { expect, test } from "bun:test";

import { runCli } from "../src/index.ts";

test("cli placeholder prints the three skeleton messages", async () => {
  const output: string[] = [];

  const exitCode = await runCli(["hello"], {
    error(message) {
      output.push(`ERR:${message}`);
    },
    log(message) {
      output.push(message);
    },
  });

  expect(exitCode).toBe(0);
  expect(output[0]).toBe("GraphSpec CLI placeholder");
  expect(output.some((line) => line.includes("GraphSpec core placeholder"))).toBe(true);
  expect(output.some((line) => line.includes("GraphSpec web placeholder"))).toBe(true);
});
