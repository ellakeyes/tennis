import sys, json, hashlib, dataclasses
from pathlib import Path
src = Path(sys.argv[1]); queue = Path(sys.argv[2])
sys.path.insert(0, str(src))
from agent_control.supervisor import supervisor as sv
text = queue.read_text()
tasks, errors = sv.parse_ready_tasks_with_errors(text)
out = {
  "queue_path": str(queue), "queue_sha256": hashlib.sha256(text.encode()).hexdigest(),
  "parser_commit": "4b93bb0ece81e4933b7e1649d9651e4fdd722fb5",
  "dispatchable_tasks_parsed_ok": [dataclasses.asdict(t) for t in tasks],
  "parse_errors": [dataclasses.asdict(e) for e in errors],
}
print(json.dumps(out, indent=1, default=str))
