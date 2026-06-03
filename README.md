# Treevis-Mirror

[View the live mirror here](https://xyvir.github.io/Treevis-Mirror/)

This is a modified, single-file monolithic HTML mirror of the excellent chess opening visualization tool, [Treevis](https://www.treevis.org/), originally created by Alex (Lehrer Böhler).

> **License Exception Notice:**
> The original Treevis project is distributed under the CC BY-NC-ND 4.0 license. This specific modified fork is hosted publicly as a free, unadvertised personal project with the **explicit, written permission of the original author**.

## Modifications in this Mirror
This version was adapted primarily for seamless offline and local usage. The key technical deviations from the main branch include:

* **Single-File Monolith:** Repackaged to run entirely from a single HTML document.
* **Engine Swap:** Replaced the Stockfish WASM implementation with `js-chess-engine` to maintain single-file compatibility.
* **Local Opening Database:** Bypassed the authenticated Lichess Explorer API by integrating a locally-mirrored SCID Opening Book Blitz database from Lumbras Gigabase.
* **URL Payload Support:** Current PGNs are dynamically encoded directly into the URL query string. This allows for easy bookmarking and sharing of specific lines (e.g., `?pgn=MS4gZTQgZ...`).

## Credits
All core logic, design, and UI/UX credit belongs entirely to Alex. If you find this tool useful, please consider using and supporting the original project at [Treevis.org](https://www.treevis.org/).
