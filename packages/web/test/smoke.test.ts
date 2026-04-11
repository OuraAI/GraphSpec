import { expect, test } from "bun:test";

import { WEB_PLACEHOLDER_MESSAGE, webHello } from "../src/index.ts";

test("web placeholder exposes a stable hello message", () => {
  expect(webHello()).toBe(WEB_PLACEHOLDER_MESSAGE);
});
