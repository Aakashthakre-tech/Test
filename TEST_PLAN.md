# Safe test plan

1. Extract this ZIP into a disposable folder outside your PatchGuard project.
2. Point PatchGuard's scanner at this folder using its supported repository-scan workflow.
3. Confirm it reports the f-string SQL query in `app.py`.
4. Generate a patch for this separate repository.
5. Verify the patch in the sandbox and approve it.
6. Use PatchGuard's **test-copy workflow** if available. Do not bypass protected-path checks.
7. Confirm the patched query uses parameterized SQL and that the original extracted `app.py` remains unchanged when applying to a copy.
8. Run `python app.py` in the patched copy and confirm the injection-style test no longer returns all users.

This is a deliberately vulnerable fixture. Never deploy it or connect it to real data.
