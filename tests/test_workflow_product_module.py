from src.workflow_product_module import WorkflowProductModule, build_sop_map


def test_sop_mapping_contains_required_structures():
    sops = build_sop_map()
    assert "sop_lead_qualification" in sops
    assert "sop_content_repurposing" in sops

    lead_sop = sops["sop_lead_qualification"]
    assert lead_sop.inputs
    assert lead_sop.rules
    assert lead_sop.decisions
    assert lead_sop.outputs


def test_lead_qualification_agent_sales_qualified():
    module = WorkflowProductModule()
    output = module.run_lead_qualification_agent(
        {
            "lead_id": "lead-1",
            "budget_usd": 12000,
            "decision_authority": "Founder",
            "need_score": 8,
            "timeline_days": 30,
        }
    )
    assert output["result"]["qualification"] == "sales-qualified"
    assert module.get_metrics()["total_tasks"] == 1


def test_content_repurposing_agent_returns_formats_and_logs_cost():
    module = WorkflowProductModule()
    output = module.run_content_repurposing_agent(
        {
            "asset_id": "asset-1",
            "source_type": "webinar",
            "source_word_count": 1500,
            "target_channel": "linkedin",
        }
    )

    assert "long_form_guide" in output["result"]["output_formats"]
    metrics = module.get_metrics()
    assert metrics["total_tasks"] == 1
    assert metrics["avg_cost_usd"] > 0


def test_dashboard_contains_kpi_labels():
    module = WorkflowProductModule()
    module.run_lead_qualification_agent(
        {
            "lead_id": "lead-2",
            "budget_usd": 1000,
            "decision_authority": "intern",
            "need_score": 2,
            "timeline_days": 120,
        }
    )
    html = module.dashboard_html()
    assert "Avg decision accuracy" in html
    assert "Avg cost / task" in html


def test_igor_assistant_brief_contains_execution_protocol_and_identity_core():
    module = WorkflowProductModule()
    module.run_lead_qualification_agent(
        {
            "lead_id": "lead-3",
            "budget_usd": 6000,
            "decision_authority": "owner",
            "need_score": 9,
            "timeline_days": 14,
        }
    )

    brief = module.build_igor_assistant_brief(risk_level="elevated", strategic_goal="stabilize_churn")

    assert brief["identity_core"]["operating_mode"] == "single_source_ai_integration"
    assert brief["identity_core"]["risk_level"] == "elevated"
    assert brief["identity_core"]["strategic_goal"] == "stabilize_churn"
    assert "context_design" in brief["execution_protocol"]
    assert len(brief["priority_queue"]) == 3
