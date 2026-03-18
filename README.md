# Reading Group Curriculum

[![ORGAN-VI: Koinonia](https://img.shields.io/badge/ORGAN--VI-Koinonia-4a148c?style=flat-square)](https://github.com/organvm-vi-koinonia)
[![Access: Private](https://img.shields.io/badge/Access-Private%20%2F%20Invitation--Only-333333?style=flat-square)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-4caf50?style=flat-square)]()

> Curriculum design, curated reading lists, discussion guides, and structured intellectual programming for the organvm community — spanning all eight organs.

[Purpose](#purpose) | [Participation Model](#participation-model) | [Curriculum Architecture](#curriculum-architecture) | [Sample Curricula](#sample-curricula) | [Reading List Philosophy](#reading-list-philosophy) | [Discussion Guide Framework](#discussion-guide-framework) | [Output Expectations](#output-expectations) | [Archive Structure](#archive-structure) | [Community Guidelines](#community-guidelines) | [Access & Invitations](#access--invitations) | [Contributing](#contributing) | [Channels & Platforms](#channels--platforms) | [Code of Conduct](#code-of-conduct) | [Inspirations & Lineage](#inspirations--lineage) | [Author & Contact](#author--contact)

---

## Purpose

The reading group curriculum provides the intellectual scaffolding for sustained, structured inquiry within the organvm community. Where the [salon archive](https://github.com/organvm-vi-koinonia/salon-archive) captures event-based gatherings, the reading group operates on a longer arc: multi-week programs that build understanding progressively, session by session, text by text, conversation by conversation.

Reading groups serve a distinct function within the eight-organ system. Theory (ORGAN-I) produces frameworks; art (ORGAN-II) instantiates them; commerce (ORGAN-III) tests them against market reality. But none of these organs provides a structured space for participants to *study together* — to read the same texts, grapple with the same questions, and develop shared interpretive capacity over time. The reading group fills this gap. It is the organ of slow, cumulative understanding in a system that also values rapid production and deployment.

The curricula in this repository are not syllabi imposed on passive students. They are structured invitations to collaborative inquiry. Each curriculum provides a curated path through a body of work — books, papers, artworks, codebases — with discussion questions, exercises, and output expectations designed to produce genuine understanding rather than surface familiarity. Participants are expected to read, reflect, write, and discuss. The reading group's value comes from the discipline of sustained engagement, and the curriculum is the infrastructure that makes that discipline possible.

This repository is also designed with potential external adoption in mind. While the primary audience is the organvm community, the curricula are structured for portability: a university seminar, an artist residency program, or an independent study group could adapt any curriculum for their own context. The reading lists, discussion guides, and output frameworks are self-contained and transferable.

## Participation Model

Reading group participation is invitation-based, following the same principles as the broader ORGAN-VI community. Groups are kept small — typically six to twelve participants — to ensure that every member has space to contribute substantively in discussion sessions.

Each curriculum runs as a cohort. Participants commit to the full program duration (typically 8-12 weeks) and are expected to complete readings and preparatory work before each session. This commitment structure is essential: the reading group format depends on shared preparation. A participant who has not read the assigned text cannot contribute to the discussion at the level the format requires, and their presence dilutes the experience for those who have prepared.

New reading group cohorts are announced through the ORGAN-VI community channels. Prospective participants express interest and, if the group is oversubscribed, the facilitator selects participants based on background diversity, relevant expertise, and demonstrated commitment to the kind of sustained engagement the format demands. Priority is given to participants who can bring perspectives from different parts of the eight-organ system — a theorist from ORGAN-I, an artist from ORGAN-II, and a product builder from ORGAN-III reading the same text will produce a richer discussion than a homogeneous group.

Repeat participation across multiple curricula is encouraged. The reading group is designed as an ongoing intellectual practice, not a one-time event. Over time, the cohort develops shared references and deepening capacity for the kind of cross-disciplinary thinking the organvm system values.

## Curriculum Architecture

Each curriculum in this repository follows a consistent structure designed for clarity, portability, and facilitation.

```
curricula/
  curriculum-slug/
    overview.md              # Curriculum description, learning goals, prerequisites
    schedule.md              # Week-by-week session plan
    reading-list.md          # Complete annotated reading list
    sessions/
      week-01/
        readings.md          # Specific readings for this week
        discussion-guide.md  # Facilitator questions and discussion structure
        exercises.md         # Activities, writing prompts, or creative exercises
        notes.md             # Post-session notes (populated after the session)
      week-02/
        ...
    outputs/
      guidelines.md          # Output expectations and formats
      submissions/           # Participant outputs (with attribution)
    evaluation/
      self-assessment.md     # Participant self-evaluation framework
      facilitator-notes.md   # Facilitator observations and curriculum feedback
```

Each curriculum is self-contained: a facilitator should be able to run the full program using only the materials in its directory, without requiring additional context or external coordination. The structure is designed for both synchronous and asynchronous use — a group meeting weekly on video call uses the same materials as a group working through the curriculum asynchronously with periodic check-ins.

### Curriculum Metadata

Every curriculum carries a metadata header that supports indexing and cross-referencing.

```yaml
curriculum:
  title: "Recursive Systems: Theory and Practice"
  slug: recursive-systems-theory-and-practice
  duration_weeks: 10
  session_frequency: weekly
  session_duration_minutes: 90
  prerequisites:
    - "Familiarity with at least one programming language"
    - "Willingness to engage with philosophical texts"
  organ_alignment:
    primary: ORGAN-I
    secondary: [ORGAN-II, ORGAN-IV]
  difficulty: intermediate
  facilitator: "@4444J99"
  cohort_size: 8-12
  status: active
  created: 2026-02-11
```

## Sample Curricula

The following curricula are either active, in development, or proposed. Each represents a sustained inquiry into a domain that spans multiple organs of the organvm system.

### Curriculum 1: Recursive Systems — Theory and Practice

**Duration:** 10 weeks | **Organ alignment:** ORGAN-I (primary), ORGAN-II, ORGAN-IV | **Difficulty:** Intermediate

An investigation of recursive and self-referential systems — from Hofstadter's strange loops to autopoiesis to the recursive-engine framework in ORGAN-I. The curriculum traces recursion from its mathematical foundations through its philosophical implications to its practical instantiation in creative and institutional systems.

**Weeks 1-3:** Foundations — formal recursion, self-reference in logic and mathematics, Godel's incompleteness theorems as framing. Readings include Hofstadter (*Godel, Escher, Bach*, selected chapters), Nagel and Newman (*Godel's Proof*), and primary engagement with ORGAN-I's recursive-engine--generative-entity codebase.

**Weeks 4-6:** Biological and philosophical recursion — autopoiesis (Maturana and Varela), enactivism (Thompson), recursive self-improvement in AI systems. Discussion focuses on where formal recursion meets embodied, situated systems.

**Weeks 7-9:** Applied recursion — recursive governance (how ORGAN-IV's orchestration system uses recursive validation), recursive aesthetics (how ORGAN-II's generative art systems employ self-referential processes), and the meta-question: is the eight-organ system itself a recursive structure?

**Week 10:** Synthesis and output — participants produce a short essay, code sketch, or conceptual design that applies recursive thinking to a domain of their choice.

### Curriculum 2: Generative Art Philosophy

**Duration:** 8 weeks | **Organ alignment:** ORGAN-II (primary), ORGAN-I | **Difficulty:** Beginner to Intermediate

An exploration of the philosophical foundations of generative and algorithmic art, from early computer art (Vera Molnar, Manfred Mohr, Harold Cohen) to contemporary practices in AI-assisted creation. The curriculum pairs historical and theoretical readings with direct engagement with ORGAN-II repositories.

Key readings include Galanter ("What is Generative Art?"), Boden and Edmonds (*The Creative Mind*), Zeilinger (*Tactical Entanglements*), and primary source engagement with Processing Foundation publications. Each session pairs a theoretical text with examination of a specific ORGAN-II project, grounding abstract discussion in concrete creative systems.

### Curriculum 3: Digital Commons Governance

**Duration:** 10 weeks | **Organ alignment:** ORGAN-IV (primary), ORGAN-III, ORGAN-V | **Difficulty:** Intermediate

How do digital communities govern shared resources? This curriculum traces the intellectual history from Ostrom's commons theory through open source governance models to contemporary questions about AI-generated content, platform cooperativism, and institutional design for creative systems.

Readings span Ostrom (*Governing the Commons*), Kelty (*Two Bits*), Schneider (*Governable Spaces*), and primary engagement with ORGAN-IV's governance rules and the organvm registry system. The curriculum treats the eight-organ system itself as a case study in digital commons governance — asking participants to evaluate, critique, and propose improvements to the system's institutional design.

### Curriculum 4: AI-Human Creative Practice

**Duration:** 12 weeks | **Organ alignment:** Cross-organ (I, II, III, V) | **Difficulty:** Advanced

An advanced curriculum examining the evolving relationship between human creativity and AI systems. The curriculum is structured in three arcs: technical (how current AI systems work and what they can and cannot do), philosophical (what creativity means in the context of human-AI collaboration), and practical (building creative workflows that integrate AI tools meaningfully rather than decoratively).

This curriculum draws on the organvm system's own AI-conductor workflow model — in which AI generates volume and human directs and refines — as a primary case study. Readings include Crawford (*Atlas of AI*), Bratton (*The Stack*), and Chiang (selected essays), alongside technical documentation from the organvm implementation process itself.

## Reading List Philosophy

The reading lists in each curriculum are curated according to several principles that distinguish them from typical academic syllabi.

**Cross-medium inclusion.** Reading lists include books and papers, but also artworks, codebases, recorded talks, and interactive experiences. A curriculum on generative art includes Processing sketches alongside philosophical texts. A curriculum on recursive systems includes code from ORGAN-I alongside Hofstadter. The conviction is that intellectual understanding emerges from engaging with ideas in multiple media, not just prose.

**Primary sources over surveys.** Where possible, participants read the original texts rather than summaries or interpretations. Godel's proof rather than a popularization of it. Ostrom's fieldwork rather than a Wikipedia article about commons theory. The reading group format provides the scaffolding (discussion guides, facilitator context) that makes primary source engagement accessible.

**Organ-system integration.** Every curriculum includes direct engagement with organvm repositories as "texts" to be read alongside published works. This is not decorative self-reference — the system's own repos are treated as primary sources that demonstrate the ideas under discussion in practical form.

**Manageable scope.** Weekly reading loads are calibrated for participants with full professional lives. Typically 40-80 pages of text per week, or equivalent time investment for non-text materials. The goal is depth of engagement, not coverage breadth. It is better to read one chapter carefully than three chapters superficially.

**Annotated entries.** Every item on a reading list includes a brief annotation explaining why it is included, what to focus on, and how it connects to the curriculum's larger arc. Participants should never open a reading without understanding why it was assigned.

## Discussion Guide Framework

Each weekly session is supported by a discussion guide that provides structure for the facilitator and orientation for participants.

**Opening question (5 minutes).** A single question designed to surface initial reactions and establish the session's focus. Opening questions are deliberately broad: "What surprised you in this week's reading?" or "Where did you disagree with the author?"

**Core discussion (45-60 minutes).** Three to five prepared questions that move from comprehension through analysis to application. The progression is intentional: early questions verify understanding, middle questions invite critical engagement, and closing questions connect the material to participants' own work and to the eight-organ system.

**Cross-organ connection (15 minutes).** A dedicated segment that explicitly links the session's material to work in other organs. This prevents the reading group from becoming insular — every session includes a moment of asking "how does this connect to what we're building?"

**Synthesis (10 minutes).** Facilitated summary of key insights, open questions, and threads to carry forward. The facilitator captures these in the session's `notes.md` for archival.

Facilitators are encouraged to adapt the guide based on the group's energy and the natural direction of discussion. The guide is scaffolding, not script — it ensures that essential ground is covered while leaving space for the kind of productive tangent that makes reading groups generative.

## Output Expectations

Each curriculum defines output expectations — concrete artifacts that participants produce as a result of their engagement. Outputs serve several purposes: they deepen individual understanding (writing is thinking), they create sharable artifacts that enrich the archive, and they provide evidence of the reading group's intellectual productivity.

**Standard output formats include:**

- **Response essays** (800-1,500 words): critical engagement with a specific reading or theme. Not summaries but arguments — participants take a position and develop it.
- **Creative responses**: artworks, code sketches, designs, or performances that respond to the curriculum's themes through making rather than writing.
- **System proposals**: governance proposals, architectural designs, or workflow specifications that apply the curriculum's ideas to the organvm system.
- **Annotated bibliographies**: curated reading lists with extended annotations, suitable for sharing beyond the reading group.

Output submission is not graded — this is not an academic course. But it is expected. The commitment to producing output is what distinguishes a reading group from a book club. Participants who consistently do not produce outputs may be asked whether the format is serving their needs, and alternative modes of participation may be discussed.

## Archive Structure

Completed curriculum runs are archived in the [salon archive](https://github.com/organvm-vi-koinonia/salon-archive) with cross-references linking reading group sessions to the broader ORGAN-VI archive. The curriculum repository retains the canonical curriculum materials (reading lists, discussion guides, exercises), while participant outputs and session notes from specific cohort runs are archived in the salon archive's session structure.

This separation keeps the curriculum repository clean and reusable — a future cohort can run the same curriculum without wading through a previous cohort's discussion notes — while ensuring that the intellectual output of each cohort is preserved and discoverable.

## Community Guidelines

Reading group participants observe the same community guidelines as the broader ORGAN-VI community, with additional norms specific to the reading group format.

**Do the reading.** The single most important norm. The reading group format collapses without shared preparation. If life intervenes and you cannot complete a week's reading, communicate this to the facilitator. Occasional gaps are understood; persistent non-preparation is incompatible with the format.

**Engage charitably.** Approach both the assigned texts and your fellow participants' interpretations with generosity. Critique the argument, not the person. Assume that a puzzling claim may reflect understanding you have not yet reached.

**Share airtime.** Discussion is collaborative, not competitive. If you notice you have spoken more than others, create space. If you notice someone has not spoken, invite (not pressure) their contribution. The facilitator manages this actively, but participants share the responsibility.

**Honor the arc.** Each curriculum builds progressively. Resist the urge to jump ahead or to dismiss early-stage material as "too basic." The foundations matter. Trust the curriculum's design while remaining free to critique it.

**Attribute generously.** When an insight emerges from discussion, acknowledge its collaborative origin. When you use an idea from the reading group in your own work, credit the source.

## Access & Invitations

Access to this repository is limited to ORGAN-VI community members. The reading lists and curriculum overviews may be shared publicly (and are designed to be useful as standalone resources), but the full discussion guides, facilitator notes, and participant outputs remain within the community.

To join a reading group cohort, express interest through the ORGAN-VI community channels when a new cohort is announced. Cohort composition is curated by the facilitator to balance expertise, perspective, and organ-system affiliation. There is no formal application; a brief message indicating your interest and relevant background is sufficient.

For external organizations (universities, residency programs, independent study groups) interested in adapting a curriculum, contact the ORGAN-VI community steward. The curricula are designed for portability, and adaptation is encouraged with appropriate attribution.

## Contributing

Contributions to the curriculum repository are welcome in several forms.

**New curriculum proposals.** Community members may propose new curricula by submitting an `overview.md` with the curriculum metadata, a draft reading list, and a rationale for how the curriculum serves the eight-organ system's intellectual goals. Proposals are reviewed by the ORGAN-VI steward and, if accepted, developed collaboratively.

**Reading list additions.** Suggesting new texts, artworks, codebases, or other materials for existing curricula. Each suggestion should include an annotation explaining its relevance and recommended placement in the curriculum arc.

**Discussion guide refinement.** Improving existing discussion questions based on facilitation experience. The best contributions come from facilitators who have run a curriculum and observed which questions produce generative discussion and which fall flat.

**Translation and adaptation.** Adapting curricula for different contexts — shorter formats, different audiences, specific disciplinary focuses. Adaptations are stored alongside the original curriculum with clear attribution.

**Output curation.** Helping to select and organize standout participant outputs for inclusion in the archive's public-facing materials, with participant consent.

## Channels & Platforms

Reading group logistics and coordination use the same platform infrastructure as the broader ORGAN-VI community.

**Cohort coordination** — scheduling, material distribution, and logistics are managed through the community Discord. Each active reading group cohort has a dedicated channel.

**Synchronous sessions** — weekly discussions take place via video call. Links are distributed through the cohort's Discord channel prior to each session.

**Asynchronous discussion** — between sessions, participants use the Discord channel for ongoing conversation, sharing supplementary materials, and discussing the readings informally.

**Repository access** — curriculum materials, discussion guides, and output submission use standard Git workflows through this GitHub repository. Participants should be comfortable with basic Git operations or willing to learn them as part of their participation.

## Code of Conduct

All reading group participants are bound by the [organvm Code of Conduct](https://github.com/organvm-vi-koinonia/.github/blob/main/CODE_OF_CONDUCT.md).

The reading group context adds specific expectations. Intellectual disagreement is not only permitted but expected — a reading group in which everyone agrees is not doing its job. But disagreement is conducted with respect for the person and rigor toward the idea. Dismissive language, personal attacks, and argumentative grandstanding are incompatible with the collaborative inquiry the format is designed to support.

The facilitator serves as the first point of contact for any concerns about group dynamics. If a participant feels that the guidelines are not being observed, they should raise the issue with the facilitator directly. Persistent violations are addressed through the ORGAN-VI community governance process.

## Inspirations & Lineage

The reading group curriculum draws on several models for structured intellectual community.

**Bard College's seminar tradition** — small-group, discussion-based engagement with primary texts, where the facilitator guides rather than lectures and every participant is expected to contribute. The Bard model demonstrates that rigorous intellectual work is possible outside the conventional lecture format.

**Santa Fe Institute reading groups** — cross-disciplinary study groups that bring together researchers from different fields to read texts at the boundaries of their expertise. The SFI model demonstrates that the most productive reading groups are those that combine diverse disciplinary perspectives around shared questions.

**Mess Hall (Chicago, 2003-2013)** — a collectively-run experimental cultural center that hosted reading groups, skill shares, and collaborative projects. Mess Hall's model of "free, open, and collectively organized" intellectual programming influences this curriculum's emphasis on non-hierarchical participation and output production.

**The Public School (various cities, 2007-present)** — a school with no curriculum that instead uses proposals from participants to build classes. The Public School's emphasis on participant-driven intellectual programming informs this curriculum's contributor model, in which community members propose new curricula based on their own questions and interests.

These models share a conviction that sustained, structured intellectual engagement in community produces understanding that solitary study cannot. The reading group curriculum is the infrastructure that makes this kind of engagement possible within the organvm system, at the scale and pace that a distributed creative-institutional project requires.

## Author & Contact

**Maintained by:** [@4444J99](https://github.com/4444J99)
**Organization:** [organvm-vi-koinonia](https://github.com/organvm-vi-koinonia)
**Part of:** The [organvm eight-organ system](https://github.com/meta-organvm) — a creative-institutional framework spanning theory, art, commerce, orchestration, public process, community, and marketing.

For questions about the reading group program, curriculum proposals, or community membership, reach out through the organvm community channels or open a discussion in this repository.

---

*ORGAN-VI is where the organvm system's ideas are studied, debated, and deepened through shared inquiry. The reading group curriculum provides the structure for that study — not as academic exercise, but as creative practice.*

<!-- SYSTEM-NAV-START -->

---

<sub>[Portfolio](https://4444j99.github.io/portfolio/) · [System Directory](https://4444j99.github.io/portfolio/directory/) · [ORGAN VI · Koinonia](https://organvm-vi-koinonia.github.io/) · Part of the <a href="https://4444j99.github.io/portfolio/directory/">ORGANVM eight-organ system</a></sub>

<!-- SYSTEM-NAV-END -->
