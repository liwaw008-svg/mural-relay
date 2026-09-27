# Mural Relay / Permit pending

**Wall purpose:** a neighborhood mural assembled one juried panel at a time on GenLayer.

## Wall brief

The permit holder freezes the community brief, palette language, forbidden motifs, and wall length. Each wallet may paint once. Validators independently decide whether the proposal continues the accepted wall, serves the brief, and avoids every forbidden motif. Code then fills exactly the next bay or adds one fracture. A full wall is `UNVEILED`; three fractures make it `SCRAPPED`.

## Relay protocol

`permit_mural` creates the wall. `paint_next` performs the only panel mutation. The public surface reads `get_mural`, paged critiques, paged murals, and the summary. IDs are normalized, duplicate walls fail, panel counts remain between three and eight, and closed walls reject paint.

## Jury marks

Consensus is essential because visual continuity and community meaning are contextual. The verifier rejudges the original brief, palette, forbidden list, accepted panels, and exact proposal. Shape-only approval is not accepted.

## Worksite commands

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
cd frontend
npm install
npm run typecheck
npm run build
```

The static Next.js wall uses `genlayer-js`; the contract is its only backend. The screenprint wall, rolling bay reveal, scaffold frame, and critique ribbon define the visual system. It is a collaborative fiction tool, not municipal approval or commissioned-art evidence.

## Unveiling record

- Contract: `0x7d4a5c281dbAA4607d6750AE5C666b6dd4B313CD`
- Deployment: `0x36d3d1554d92e86c11cc4cdd1ce13d35c4a791f9509ae3b1f643c346eb1200c8`
- Repository: https://github.com/liwaw008-svg/mural-relay
- Public wall: https://liwaw008-svg-mural-relay.pages.dev/
