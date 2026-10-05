# Push status — Book 1 source harvest

**Branch:** `cursor/book1-source-harvest-9ddc`  
**Commit:** `054ef6a05ba3183be1a108197b0d7f6ec1f2d429`  
**Base:** `ccr-e641566e-pl28m8` @ `63b418aaa5d21fb57366789c0b7e406194c17a7c`

## Result

`git push -u origin cursor/book1-source-harvest-9ddc` → **403** (`Permission to mdjonyrd/tahara1.git denied to cursor[bot]`).

No force-push attempted.

## Bundle

```
git bundle create book1-source-harvest-9ddc.bundle origin/ccr-e641566e-pl28m8..cursor/book1-source-harvest-9ddc
```

Bundle path (this environment): `/tmp/tahara1-harvest-bundle/book1-source-harvest-9ddc.bundle`

To import on a machine with write access:

```bash
git fetch /path/to/book1-source-harvest-9ddc.bundle cursor/book1-source-harvest-9ddc:cursor/book1-source-harvest-9ddc
git push -u origin cursor/book1-source-harvest-9ddc
```
