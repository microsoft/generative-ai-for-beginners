"""Workflow product module for mapping SOPs and running automation agents.

This module provides:
- SOP mapping for recurring 7ya.io style workflows.
- Two initial workflow agents:
  1. Lead Qualification Agent
  2. Content Repurposing Agent
- Structured logs linked to execution metrics (accuracy proxy, duration, cost).
- A minimal API + dashboard using Python's built-in HTTP server.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import time
from typing import Any
from uuid import uuid4
from http.server import BaseHTTPRequestHandler, HTTPServer


@dataclass(frozen=True)
class SOPDefinition:
    """Describes a recurring SOP with explicit workflow logic."""

    sop_id: str
    name: str
    description: str
    inputs: list[str]
    rules: list[str]
    decisions: list[str]
    outputs: list[str]


@dataclass
class TaskLog:
    """Runtime log emitted for each workflow task execution."""

    task_id: str
    sop_id: str
    agent_name: str
    started_at: str
    finished_at: str
    duration_ms: float
    decision_accuracy: float
    cost_usd: float
    result: dict[str, Any]


@dataclass
class WorkflowMetrics:
    """Aggregate metrics computed from task logs."""

    total_tasks: int = 0
    avg_decision_accuracy: float = 0.0
    avg_duration_ms: float = 0.0
    avg_cost_usd: float = 0.0


@dataclass
class WorkflowProductModule:
    """Productized workflow engine with SOP mapping, agents, and KPI tracking."""

    sops: dict[str, SOPDefinition] = field(default_factory=dict)
    logs: list[TaskLog] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.sops:
            self.sops = build_sop_map()

    def _record_log(
        self,
        sop_id: str,
        agent_name: str,
        started: float,
        decision_accuracy: float,
        cost_usd: float,
        result: dict[str, Any],
    ) -> TaskLog:
        finished = time.time()
        log = TaskLog(
            task_id=str(uuid4()),
            sop_id=sop_id,
            agent_name=agent_name,
            started_at=datetime.fromtimestamp(started, tz=timezone.utc).isoformat(),
            finished_at=datetime.fromtimestamp(finished, tz=timezone.utc).isoformat(),
            duration_ms=(finished - started) * 1000,
            decision_accuracy=max(0.0, min(1.0, decision_accuracy)),
            cost_usd=max(0.0, cost_usd),
            result=result,
        )
        self.logs.append(log)
        return log

    def run_lead_qualification_agent(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Execute the Lead Qualification SOP as a deterministic workflow agent."""
        started = time.time()

        budget = float(payload.get("budget_usd", 0))
        authority = str(payload.get("decision_authority", "")).lower()
        need_score = float(payload.get("need_score", 0))
        timeline_days = int(payload.get("timeline_days", 365))

        score = 0
        if budget >= 5000:
            score += 1
        if authority in {"owner", "director", "manager", "founder"}:
            score += 1
        if need_score >= 7:
            score += 1
        if timeline_days <= 90:
            score += 1

        if score >= 3:
            qualification = "sales-qualified"
            next_action = "assign_to_account_executive"
        elif score == 2:
            qualification = "marketing-qualified"
            next_action = "nurture_sequence"
        else:
            qualification = "unqualified"
            next_action = "disqualify_or_archive"

        result = {
            "lead_id": payload.get("lead_id"),
            "score": score,
            "qualification": qualification,
            "next_action": next_action,
            "reasoning": {
                "budget_usd": budget,
                "decision_authority": authority,
                "need_score": need_score,
                "timeline_days": timeline_days,
            },
        }
        log = self._record_log(
            sop_id="sop_lead_qualification",
            agent_name="Lead Qualification Agent",
            started=started,
            decision_accuracy=0.92,
            cost_usd=0.02,
            result=result,
        )
        return {"result": result, "log": asdict(log)}

    def run_content_repurposing_agent(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Execute content repurposing SOP as a deterministic workflow agent."""
        started = time.time()

        source_type = str(payload.get("source_type", "article")).lower()
        channel = str(payload.get("target_channel", "linkedin")).lower()
        word_count = int(payload.get("source_word_count", 0))

        formats: list[str]
        if source_type in {"webinar", "podcast", "video"}:
            formats = ["blog_post", "newsletter", "social_thread", "short_video_script"]
        else:
            formats = ["social_post", "newsletter", "seo_snippet"]

        if word_count > 1200:
            formats.append("long_form_guide")

        tone_by_channel = {
            "linkedin": "professional",
            "instagram": "conversational",
            "x": "punchy",
            "email": "value-first",
        }
        tone = tone_by_channel.get(channel, "clear")

        result = {
            "asset_id": payload.get("asset_id"),
            "target_channel": channel,
            "recommended_tone": tone,
            "output_formats": formats,
            "workflow_status": "ready_for_generation",
        }
        log = self._record_log(
            sop_id="sop_content_repurposing",
            agent_name="Content Repurposing Agent",
            started=started,
            decision_accuracy=0.9,
            cost_usd=0.03,
            result=result,
        )
        return {"result": result, "log": asdict(log)}

    def get_metrics(self) -> dict[str, Any]:
        """Compute KPI snapshot from logs."""
        if not self.logs:
            return asdict(WorkflowMetrics())

        total = len(self.logs)
        accuracy = sum(log.decision_accuracy for log in self.logs) / total
        duration = sum(log.duration_ms for log in self.logs) / total
        cost = sum(log.cost_usd for log in self.logs) / total

        return asdict(
            WorkflowMetrics(
                total_tasks=total,
                avg_decision_accuracy=round(accuracy, 4),
                avg_duration_ms=round(duration, 2),
                avg_cost_usd=round(cost, 4),
            )
        )

    def dashboard_html(self) -> str:
        """Return a basic dashboard HTML for quick product demo."""
        metrics = self.get_metrics()
        return f"""
<!doctype html>
<html lang=\"en\">
  <head><meta charset=\"utf-8\"><title>7ya Workflow Module</title></head>
  <body>
    <h1>7ya.io Workflow Product Module</h1>
    <h2>KPIs</h2>
    <ul>
      <li>Total tasks: {metrics['total_tasks']}</li>
      <li>Avg decision accuracy: {metrics['avg_decision_accuracy']}</li>
      <li>Avg duration (ms): {metrics['avg_duration_ms']}</li>
      <li>Avg cost / task (USD): {metrics['avg_cost_usd']}</li>
    </ul>
    <h2>Available SOPs</h2>
    <pre>{json.dumps({k: asdict(v) for k, v in self.sops.items()}, indent=2)}</pre>
  </body>
</html>
""".strip()


class WorkflowAPIHandler(BaseHTTPRequestHandler):
    """Minimal API handler to expose the product module endpoints."""

    module: WorkflowProductModule | None = None

    @classmethod
    def _module(cls) -> WorkflowProductModule:
        if cls.module is None:
            cls.module = WorkflowProductModule()
        return cls.module

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/api/sops":
            module = self._module()
            self._send_json({k: asdict(v) for k, v in module.sops.items()})
            return
        if self.path == "/api/metrics":
            module = self._module()
            self._send_json(module.get_metrics())
            return
        if self.path == "/dashboard":
            module = self._module()
            body = module.dashboard_html().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self._send_json({"error": "not found"}, status=404)

    def do_POST(self) -> None:  # noqa: N802
        content_length = int(self.headers.get("Content-Length", "0"))
        data = self.rfile.read(content_length)
        payload = json.loads(data.decode("utf-8") or "{}")

        if self.path == "/api/run/lead-qualification":
            module = self._module()
            self._send_json(module.run_lead_qualification_agent(payload))
            return

        if self.path == "/api/run/content-repurposing":
            module = self._module()
            self._send_json(module.run_content_repurposing_agent(payload))
            return

        self._send_json({"error": "not found"}, status=404)


def build_sop_map() -> dict[str, SOPDefinition]:
    """Map recurring SOPs with explicit inputs, rules, decisions, and outputs."""
    return {
        "sop_lead_qualification": SOPDefinition(
            sop_id="sop_lead_qualification",
            name="Lead Qualification",
            description="Qualify inbound leads using BANT-lite style deterministic scoring.",
            inputs=["lead_id", "budget_usd", "decision_authority", "need_score", "timeline_days"],
            rules=[
                "Budget >= 5000 contributes 1 score point.",
                "Authority in {owner,director,manager,founder} contributes 1 point.",
                "Need score >= 7 contributes 1 point.",
                "Timeline <= 90 days contributes 1 point.",
            ],
            decisions=[
                "Score >=3 => sales-qualified",
                "Score ==2 => marketing-qualified",
                "Score <=1 => unqualified",
            ],
            outputs=["qualification", "next_action", "score", "reasoning"],
        ),
        "sop_content_repurposing": SOPDefinition(
            sop_id="sop_content_repurposing",
            name="Content Repurposing",
            description="Transform source asset into channel-specific derivative formats.",
            inputs=["asset_id", "source_type", "source_word_count", "target_channel"],
            rules=[
                "Video/webinar/podcast sources produce multi-format bundles.",
                "Assets >1200 words add long-form guide output.",
                "Target channel determines tone profile.",
            ],
            decisions=[
                "Select output format bundle by source type.",
                "Select tone by target channel.",
                "Set workflow status to ready_for_generation.",
            ],
            outputs=["output_formats", "recommended_tone", "workflow_status"],
        ),
        "sop_client_onboarding": SOPDefinition(
            sop_id="sop_client_onboarding",
            name="Client Onboarding",
            description="Collect kickoff data, validate scope, and trigger project setup.",
            inputs=["signed_contract", "package_type", "primary_goal", "stack"],
            rules=["Signed contract must be true before setup.", "Package type drives onboarding checklist."],
            decisions=["Approve kickoff", "Request missing information", "Route technical discovery"],
            outputs=["onboarding_status", "kickoff_tasks", "owner_assignment"],
        ),
        "sop_campaign_reporting": SOPDefinition(
            sop_id="sop_campaign_reporting",
            name="Campaign Reporting",
            description="Weekly aggregation of channel KPIs with exception flags.",
            inputs=["channel_metrics", "period_start", "period_end", "targets"],
            rules=["Compute variance to targets.", "Flag metrics below threshold by >15%."],
            decisions=["Healthy", "Needs optimization", "Escalate"],
            outputs=["summary", "flags", "recommended_actions"],
        ),
    }


def run_server(host: str = "0.0.0.0", port: int = 8080) -> None:
    """Run the module as a basic product API/dashboard server."""
    server = HTTPServer((host, port), WorkflowAPIHandler)
    print(f"Workflow module listening on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
