# QUG: Questifying Uncertainty Game

QUG is a Discord agent prompt for running short, game-structured roleplay sessions around long-term uncertainty.

Instead of trying to remove uncertainty before action, QUG helps a user translate a recent stuck moment into a small playable quest, observe the situation from a slight distance, and return with one manageable next step.

This repository currently contains the agent definition for use with [`discord-agent-hub`](https://github.com/ks91/discord-agent-hub).

## Repository Contents

- `sg-qug-agent.md` - Discord agent hub agent definition and full QUG prompt.
- `LICENSE` - Project license.

## What QUG Does

QUG acts as a lightweight game master. It takes a real-world difficulty and temporarily recasts it as a parallel quest world while preserving the underlying pressure structure of the original situation.

The aim is not to give better advice or solve the user's problem directly. The aim is to reorganize an oversized action demand into a smaller, legitimate local move.

Examples of this shift include:

- From choosing a whole career path to testing one appealing possibility.
- From asking only after full understanding to asking one specific question.
- From restarting study properly to touching the material for one minute.
- From fixing a relationship to trying one bounded repair utterance.

## Session Structure

A typical QUG session follows this loop:

1. Ask for one recent stuck moment.
2. Identify the pressure structure behind the situation.
3. Translate that structure into a parallel quest world.
4. Run two or three short choice-bearing scenes.
5. Ask what felt closest to reality.
6. Return to real-world language.
7. Shape one side quest for the next 24-72 hours.

The prompt emphasizes bounded choice, observer-mode distance, local consequence, safe-to-fail progression, and explicit closure.

## Using With Discord Agent Hub

Use `sg-qug-agent.md` as an import-ready agent definition for [`discord-agent-hub`](https://github.com/ks91/discord-agent-hub).

The file includes an `agent` metadata block:

```agent
id: sg-qug-agent
name: QUG
provider: openai_responses
model: gpt-5.4-mini
description: Questifying Uncertainty Game
enabled: true
tools:
  web_search: false
  code_execution: false
```

In Discord, import the Markdown file with the `/agent-import` slash command. After the agent is imported, start a Discord thread with QUG using `/chat agent_id:sg-qug-agent`, then send messages inside the created thread.

If you update `sg-qug-agent.md`, re-import it with `/agent-import` and `overwrite:true` to replace the existing agent definition.

The agent is designed to open with a short introduction, ask for one current difficulty, and guide the user through the quest loop.

## Design Principles

QUG should:

- Start from a concrete recent scene rather than an abstract life goal.
- Preserve the pressure structure while changing the surface setting.
- Avoid copying the user's real workplace, family, school, or project too literally.
- Keep each scene short and choice-bearing.
- Let the user observe the protagonist before mapping the quest back to reality.
- Return to ordinary real-world language before deciding the next step.
- End with one small side quest, including what to do, when to do it, and what counts as completion.

QUG should not:

- Act as a therapist or counselor.
- Promise treatment, anxiety reduction, or emotional recovery.
- Turn the session into generic advice.
- Ask the user to rate uncertainty with numbers.
- Over-specify the user's real-world next move without confirmation.

## Research Background

QUG is based on the idea that lightweight game structures can function as epistemic tools for uncertain long-term activity. The key claim is that game structure can make continued action feel thinkable and legitimate while uncertainty remains unresolved.

The design is informed by serious games, epistemic games, reflective play, self-distancing, and LLM-based roleplay agents.

## Status

This is an exploratory prompt prototype. It is intended for research, design exploration, and small-scale piloting rather than clinical, therapeutic, or high-stakes decision support.
