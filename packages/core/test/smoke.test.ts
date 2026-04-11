import { expect, test } from "bun:test";

import { CORE_PLACEHOLDER_MESSAGE, coreHello } from "../src/index.ts";

test("core placeholder exposes a stable hello message", () => {
  expect(coreHello()).toBe(CORE_PLACEHOLDER_MESSAGE);
});
