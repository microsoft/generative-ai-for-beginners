# 7ya.io Strategic Operating Blueprint (Freeleyonayre Studio)

This document consolidates the operating system for **7ya.io / Freeleyonayre Studio** into one execution-ready plan across product, growth, operations, and fintech automation.

## 1) Executive Focus

**Mission:** convert creator attention, expertise, and community trust into predictable recurring revenue and automated long-term wealth accumulation.

**Business model:** one unified platform with four integrated engines:

1. Income Engine (SaaS + digital products)
2. Creator Engine (community + education)
3. Services Engine (productized consulting)
4. Finance Engine (automated revenue routing + investing)

## 2) Market Thesis (2026)

The operating assumptions for 7ya.io are:

- Creator businesses are shifting from sponsorship dependency to owned recurring revenue.
- Tool sprawl creates margin leakage and operational fatigue.
- AI-native operations are now a baseline requirement for speed and gross margin.
- The winning setup is a consolidated stack with direct ownership of audience and checkout paths.

## 3) Product Architecture: The Four Engines

### 3.1 Income Engine

- Hosts templates, micro-SaaS utilities, and digital products.
- Uses a fast content delivery pipeline (collect, normalize, cache, deliver).
- Prioritizes low-friction checkout and immediate value delivery.

### 3.2 Creator Engine

- Course hosting, gated newsletter, and membership access control.
- Community-led growth journey: viewer -> participant -> member -> advocate.
- Weekly cadence for office hours and iterative curriculum updates.

### 3.3 Services Engine

- Replaces custom consulting with fixed-scope, fixed-price packaged offers.
- Includes automated discovery forms, booking, payment, and kickoff workflows.
- Maintains strict delivery boundaries to preserve margin.

### 3.4 Finance Engine

- Programmatic revenue allocation (example default):
  - 50% business operations/reinvestment
  - 30% personal operating reserve
  - 20% investment allocation
- Stripe webhooks trigger allocation logic and brokerage actions.
- Investment execution is policy-driven and logged.

## 4) Tech Stack Standard

- **Frontend:** Next.js (React), SSR-first for conversion performance.
- **Backend:** FastAPI or Node/Express for async webhook/API orchestration.
- **Auth:** Supabase Auth or Firebase Auth.
- **Data:** PostgreSQL for users, subscriptions, orders, and audit logs.
- **Infra:** Vercel/Render for deployment, managed observability, automated rollbacks.
- **Payments:** Stripe + Stripe Connect.
- **Bank linking:** Plaid tokenization flows.
- **Investments:** Alpaca API (paper first, production after controls validation).

## 5) Fintech Implementation Pattern (Stripe -> Allocation -> Alpaca)

### 5.1 Webhook handling standards

- Verify Stripe signatures on every webhook.
- Idempotency required for transfer and trade execution steps.
- Structured logs with request IDs and event IDs.
- Explicit error taxonomy: payload, signature, transfer, trade, internal.

### 5.2 Example production-ready FastAPI webhook

```python
import os
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import stripe
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
INVESTMENT_PERCENTAGE = float(os.getenv("INVESTMENT_PERCENTAGE", 0.20))

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

stripe.api_key = STRIPE_SECRET_KEY
alpaca = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL, api_version="v2")

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


def place_invest_order(symbol: str, amount_usd: float):
    try:
        asset_info = alpaca.get_asset(symbol)
        if not asset_info.fractionable:
            logger.warning(f"Asset {symbol} is not fractionable")

        order = alpaca.submit_order(
            symbol=symbol,
            notional=amount_usd,
            side="buy",
            type="market",
            time_in_force="day",
        )
        logger.info(f"Invest order submitted: {order}")
        return order
    except Exception as exc:
        logger.error(f"Trade execution error: {exc}")
        raise


@app.post("/stripe-webhook")
async def stripe_webhook_handler(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        total_amount = session.get("amount_total", 0)
        invest_amount = (total_amount * INVESTMENT_PERCENTAGE) / 100.0

        logger.info(f"Checkout complete. total={total_amount} invest={invest_amount}")

        try:
            stripe.Transfer.create(
                amount=int(invest_amount * 100),
                currency="usd",
                destination=session.get("connected_account_id"),
                transfer_group=session["id"],
            )
        except Exception as exc:
            logger.error(f"Stripe transfer failed: {exc}")

        order = place_invest_order(symbol="SPY", amount_usd=invest_amount)
        return {"status": "invest_order_submitted", "order_id": getattr(order, "id", None)}

    return JSONResponse({"status": "ignored_event"})
```

## 6) Monetization Ladder

1. **$49/mo Ops Membership** (recurring base)
2. **$499 Launch Kit** (one-time, conversion accelerator)
3. **$2,500/mo Premium Retainer** (high-ticket, capped capacity)
4. Affiliate ecosystem revenue
5. Long-term investment portfolio growth via automated allocation

## 7) KPI Dashboard (Top 7 Above the Fold)

1. Monthly recurring revenue (MRR)
2. Active paying members
3. Trial-to-paid conversion
4. Churn rate
5. LTV:CAC ratio
6. Operating runway (months)
7. Investment account balance (allocated capital + performance)

Dashboard rule: if any core KPI degrades for two consecutive weeks, trigger a focused recovery sprint with a single owner.

## 8) 90-Day Execution Roadmap

### Month 1 (MVP launch)

- Ship landing page + waitlist + founding member offer.
- Publish 3-lesson mini-course lead magnet.
- Enable Stripe checkout and pre-launch email sequence.
- Close first 20 paying members and collect structured feedback.

### Month 2 (systems hardening)

- Start weekly live office hours.
- Automate top three repetitive workflows.
- Finish full course content and onboarding improvements.

### Month 3 (scaling)

- Public launch to full audience.
- Run podcast partnership outreach.
- Open limited consulting retainers.
- Start controlled paid acquisition tests with strict CAC limits.

## 9) Operational Safeguards

- Maintain a risk register across platform, compliance, and market exposure.
- Keep 3-6 months of operating expense runway in cash equivalents.
- Never store raw bank credentials; use tokenized providers.
- Run all financial automations in paper/sandbox before production rollout.
- Log and reconcile all transfer/trade events for auditability.

## 10) Weekly Operating Cadence

- **Monday:** strategy, KPI targets, priorities.
- **Wednesday:** execution review and re-prioritization.
- **Friday:** scoreboard, lessons learned, and automation queue triage.
- **Daily:** short blocker-driven standup.

This blueprint should be treated as a living operating system: update monthly based on KPI movement, customer feedback, and regulatory constraints.
