# 7ya.io Workflow Product Module

מודול זה ממפה SOP-ים חוזרים ומריץ אותם כסוכני Workflow שניתנים למכירה כרישוי מוצר.

## SOP Mapping (Recurring Processes)

### 1) Lead Qualification
- **Inputs:** `lead_id`, `budget_usd`, `decision_authority`, `need_score`, `timeline_days`
- **Rules:** ניקוד דטרמיניסטי לפי תקציב, סמכות קבלת החלטה, רמת צורך, ודחיפות זמן.
- **Decisions:** `sales-qualified` / `marketing-qualified` / `unqualified`
- **Outputs:** `qualification`, `next_action`, `score`, `reasoning`

### 2) Content Repurposing
- **Inputs:** `asset_id`, `source_type`, `source_word_count`, `target_channel`
- **Rules:** פורמטים נגזרים לפי סוג מקור, הרחבה לתוכן ארוך, וטון לפי ערוץ.
- **Decisions:** בחירת חבילת פורמטים, טון, וסטטוס.
- **Outputs:** `output_formats`, `recommended_tone`, `workflow_status`

### 3) Client Onboarding
- **Inputs:** `signed_contract`, `package_type`, `primary_goal`, `stack`
- **Rules:** חייב חוזה חתום; checklist לפי חבילה.
- **Decisions:** אישור kickoff / השלמת נתונים / ניתוב discovery טכני.
- **Outputs:** `onboarding_status`, `kickoff_tasks`, `owner_assignment`

### 4) Campaign Reporting
- **Inputs:** `channel_metrics`, `period_start`, `period_end`, `targets`
- **Rules:** חישוב variance מול יעדים + חריגות מעל 15%.
- **Decisions:** Healthy / Needs optimization / Escalate.
- **Outputs:** `summary`, `flags`, `recommended_actions`

## Implemented Workflow Agents

1. **Lead Qualification Agent**
2. **Content Repurposing Agent**

מימושים נמצאים ב-`src/workflow_product_module.py` כולל לוגיקה, לוגים ו-KPI.

## Logs + KPI Metrics

כל ריצת Agent נשמרת כ-`TaskLog` עם:
- `decision_accuracy`
- `duration_ms`
- `cost_usd`

המודול מחשב אגרגציות:
- `avg_decision_accuracy`
- `avg_duration_ms`
- `avg_cost_usd`
- `total_tasks`

## Product Packaging (API + Dashboard)

המודול נארז כשרת HTTP בסיסי:
- `GET /api/sops`
- `POST /api/run/lead-qualification`
- `POST /api/run/content-repurposing`
- `GET /api/metrics`
- `POST /api/igor/brief` (builds a strategic single-agent execution brief)
- `GET /dashboard`

להרצה:

```bash
python -m src.workflow_product_module
```

כך ניתן לספק רישוי כמוצר מודולרי ולא רק שירות ידני.


## Igor Assistant Brief Output

`POST /api/igor/brief` converts live module KPIs into a compact operating brief for a single-source AI execution model.

Request body fields:
- `risk_level`: `normal` | `elevated` | `crisis`
- `strategic_goal`: free-text strategy target (example: `increase_mrr`, `stabilize_churn`)

Response includes:
- `identity_core`
- `kpi_snapshot`
- `alerts`
- `priority_queue`
- `execution_protocol`
