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

This is not a quiz and not a points-based exam. The learner enters an explainable Gulf business scenario, makes one primary decision, sees the consequence first, receives knowledge cards, and accumulates evidence only from observable behavior.

Use it for:

- onboarding for sales, project, legal, compliance, and delivery roles;
- scenario-based observation in interviews;
- sales practice when a rep knows the product but not how to judge buyers, partners, or risk;
- consistent internal training on business language, escalation, and stop conditions.

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

Evidence ranges from E0 (not observed) to E3 (strong evidence, including conflict handling, verification boundaries, and revision under new evidence). Reasons embedded in an answer option do not count as independent reasoning.

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

The helper scripts require only the Python 3 standard library. Without Python, the TXT/CSV knowledge files remain readable.

## Arabic audio

The package includes 379 Arabic term entries and 369 MP3 files covering greetings, hospitality, business, compliance, and industry terms. Scenario turns can create a combined pronunciation link for the terms used in that turn.

The audio is machine-generated with the macOS Majed voice, not human-recorded. All 379 entries remain marked as not individually human-reviewed, and the project does not claim zero pronunciation errors.

## Test evidence

<div align="center">
  <img src="docs/images/test-training.png" alt="Country training validation results" width="100%">
</div>

The release check validates frontmatter, local links, 33 knowledge files, 1,931 indexed records, 379 audio term paths and SHA-256 values, 369 MP3 files, and a local term lookup. GitHub Actions runs the same check on every push and pull request.

Passing tests prove package integrity and asset consistency. They do not constitute a large-scale study of training effectiveness.

## Privacy

- Personal notes are private by default.
- HR or team reports require explicit authorization.
- Progress may be described as saved only after a successful storage write.
- Private notes, answers, and learner profiles must never be written back into the distributable Skill files.

## Fact boundary

Rules and policies inside training scenarios are practice material. Real quotes, bids, shipments, customs clearance, assignments, tax, medical, product-safety, cross-border data, and sanctions questions trigger live verification against current official sources.

The Skill includes no search entitlement, API key, or background service.

## Companion project

Use the separate [GulfGate Country Analysis](https://github.com/origami3521905038-hash/gulfgate-country-analysis) Skill for real research, market-entry planning, and pre-action checks.

## Co-creators

This project was jointly created by [@origami3521905038-hash](https://github.com/origami3521905038-hash) and [@18719203981lkr-spec](https://github.com/18719203981lkr-spec).

Contributions are welcome through issues and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

No open-source license is attached yet. Copyright remains with the co-creators. Written permission is required before public reuse, commercial use, or redistribution.

