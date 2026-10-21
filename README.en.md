# GulfGate Country Training Skill

<p><a href="README.md"><u>简体中文</u></a> · <a href="README.en.md"><u>English</u></a> · <a href="README.ar.md"><u>العربية</u></a></p>

<div align="center">
  <img src="docs/images/hero-training.png" alt="GulfGate Country Training Skill hero" width="100%">
</div>

> Let new international-business hires practice judgment in safe scenarios, see the consequences, and enter customer-facing work with traceable behavioral evidence.

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Scenarios](https://img.shields.io/badge/scenarios-38-c18b49)](#training-routes)
[![Arabic](https://img.shields.io/badge/Arabic%20audio-379%20terms-1f6f50)](#arabic-audio)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

The learner enters an explainable Gulf business scenario, makes one primary decision, sees the commercial consequence, receives knowledge cards, and builds evidence from observable behavior. Every session creates a concrete basis for coaching and role development.

Use it for:

- onboarding for sales, project, legal, compliance, and delivery roles;
- scenario-based observation in interviews;
- sales teams turning product knowledge into buyer, partner, and risk judgment;
- consistent internal training on business language, escalation, and stop conditions.

## One session, four concrete outcomes

- **Immediate feedback:** see the business consequence, critical judgment, and stronger next action;
- **Ability evidence:** capture A1–A6 performance across demonstrated, developing, and unobserved skills;
- **Custom route:** combine countries, industries, roles, and session length automatically;
- **Training report:** produce personal review, strengths, development themes, and the next training plan.

## Three high-frequency training cases

<div align="center">
  <img src="docs/images/cases-training.png" alt="Three Gulf business training use cases" width="100%">
</div>

1. **Renewable-energy sales hire · 20-minute quick route:** build a working framework across customer meetings, partner checks, access, and collection.
2. **Legal / compliance role · role route:** practice evidence, escalation, and professional judgment across licensing, contracts, data, sanctions, and crisis.
3. **HR / team development · panorama:** complete module profiles, identify shared development themes, and produce an authorized training report.

## Demo

<div align="center">
  <img src="docs/images/demo-training.png" alt="Country training demo session" width="100%">
</div>

Example request:

```text
Use $gulfgate-country-training.
I am a new renewable-energy sales hire focused on Saudi Arabia and the UAE.
Train partner assessment, product access, and collection risk in a 20-minute quick route.
```

See the complete public-safe interaction in [examples/training-demo.md](examples/training-demo.md).

## Six abilities

| Ability | Training focus |
| --- | --- |
| A1 Country judgment | Country, emirate, free zone, project jurisdiction, and fact validity |
| A2 Cross-cultural communication | Relationship, context, introductions, meetings, and progression signals |
| A3 Access judgment | Product, entity, project, platform, and supplier eligibility as separate layers |
| A4 Compliance awareness | Permits, anti-corruption, tax, data, and personnel boundaries |
| A5 Risk governance | Evidence design, stage gates, escalation, and exit criteria |
| A6 Delivery execution | Quote, contract, logistics, installation, acceptance, and collection as one chain |

The assessment highlights E2 effective evidence and E3 strong evidence across OBSERVE, REASON, DECIDE, ACT, VERIFY, ESCALATE, and REVISE, so feedback reflects the learner’s own judgment, reasoning, and action.

## Training routes

| Route | Scenarios | Best for |
| --- | ---: | --- |
| `quick` | 7 | A 20-minute introduction or team warm-up |
| `role` | 18–28 | A role-specific sales, legal, project, or compliance route |
| `panorama` | 38 | A complete business-chain walkthrough |

The seven modules cover market opportunity, commercial ecosystems, cross-cultural engagement, access and tendering, contracts and collection, delivery and local operations, and compliance and crisis management.

## Install

```bash
git clone https://github.com/origami3521905038-hash/gulfgate-country-training.git
mkdir -p ~/.codex/skills
cp -R gulfgate-country-training ~/.codex/skills/
```

Run the offline release check:

```bash
cd gulfgate-country-training
python tests/validate_package.py
```

The package includes lookup tools built on the Python 3 standard library, and the TXT/CSV knowledge files are available for direct reading.

## Arabic audio

The package includes 379 Arabic term entries and 369 MP3 files covering greetings, hospitality, business, compliance, and industry terms. Scenario turns can create a combined pronunciation link for the terms used in that turn.

The player supports combined turn vocabulary, full-library filtering, and individual playback while keeping audio separate from training progress, notes, and learner profiles.

## Test evidence

<div align="center">
  <img src="docs/images/test-training.png" alt="Country training validation results" width="100%">
</div>

The release check validates frontmatter, local links, 33 knowledge files, 1,931 indexed records, 379 audio term paths and SHA-256 values, 369 MP3 files, and a local term lookup. GitHub Actions runs the same check on every push and pull request.

Every content update automatically revalidates knowledge indexes, audio paths, hashes, and lookup tools, keeping the training material and release version consistent.

## Privacy

- Personal notes stay private by default and follow the user’s authorization scope.
- HR and team reports support explicit authorization and scope control.
- Progress is confirmed after a successful storage write for reliable review records.
- Chat-only environments maintain progress within the current context.
- Private notes, answers, and learner profiles remain separate from distributable Skill files.

## Real-time verification

When training involves real quotes, bids, shipments, customs, assignments, tax, medical products, product safety, cross-border data, or sanctions, the workflow enters LIVE_VERIFY and uses the competent authority and official source text as the factual basis.

Hosts with web search and page-reading access can complete a live check, while the packaged knowledge base continues to support scenario context, business reasoning, and evidence checklists.

## Companion project

Use the separate [GulfGate Country Analysis](https://github.com/origami3521905038-hash/gulfgate-country-analysis) Skill for real research, market-entry planning, and pre-action checks.

## Co-creators

This project was jointly created by [@origami3521905038-hash](https://github.com/origami3521905038-hash) and [@18719203981lkr-spec](https://github.com/18719203981lkr-spec).

Contributions are welcome through issues and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Copyright is jointly held by both co-creators. Contact the authors to discuss enterprise training, custom courses, industry expansion, or partnership licensing.

