# Y Jewelry: "Her Story" website direction

Design canvas for Y Jewelry (charm jewellery, founded by Monika Pal Sood), designed by Somya Garg (Team Pumpkin).
Exported from a Claude Design canvas, "Y Story Website Direction". ~55 artboards, each one page.

## Layout of this folder
- `project/*.dc.html`  one Design Component page per artboard (source of truth). `project/canvas.json` is the board index (positions, sizes, order).
- `assets/<id>.<ext>`  every uploaded image. In the source they appear as `/_blob/<id>`; the id is the filename stem.
- `site/*.html`        plain-HTML build of the pages (run `python3 tools/build_static.py`). Open `site/Main.html` etc. directly. 4 pages (Amy, BookCall, GiftNote, Scratch) use loops/bindings and are not built; they need the runtime.
- `reference/`         `format.md` (the .dc.html format rules), `DESIGN-TYPE-SKILL.md` (how the canvas editor expects files), `dc-runtime.js`.

## Editing rules
- Edit the `.dc.html` files, then rebuild `site/`. Keep `<x-dc>`, `<helmet>` and the `<script type="text/x-dc">` block intact if the file will go back into the canvas.
- Images stay `/_blob/<id>` in `project/` (that is what the canvas resolves). Do not inline images as data URIs there.
- Pages are fluid (fill width) and use inline styles. Mobile is a separate board, not a breakpoint, though `MainMobile` also has a `@media (max-width: 760px)` block.
- A canvas board cannot be taller than 8000px, so the mobile homepage is split into `MainMobile.dc.html` (top) and `MainMobile2.dc.html` (In their words, note, footer).

## Brand
- Indigo `#0B0A4E` (primary, text, price bars, buttons, footer). Gold dots/lines `#D9BC8C`, highlight `#E3C9A0`, ring `#C09A68`, terracotta `#8F4F42`. Backgrounds are WHITE. Do not use beige/cream page backgrounds (the designer sees them as a "Claude-made" tell). Some legacy pages still carry cream tokens (`#F8F4EC`, `#FBF8F2`, `#EFE9DE`).
- Type: Belwe Sans (embedded as base64 in each page's `<helmet>`), Cormorant Garamond, Karla, Mrs Saint Delafield (Monika's signature, handwriting) from Google Fonts.
- Voice: warm, first person from Monika. Placeholders in [brackets] are deliberate (prices [MRP], customer quotes, names). Do not invent testimonials or customer names.

## Homepage (`Main.dc.html`) section order
Header, hero (hand with rose-gold charm bracelet), category tiles (Ready to Wear Sets, Charms, Bracelets, Necklaces), "Every story, in its own time" (bracelet/necklace set tabs, cards with gold dot trackers and indigo price bars), occasion tiles (Birthday, Anniversary, Diwali, Graduation, New Beginnings), Amy the stylist, "Twelve pieces I'd wear now", gifts block (full width), "Keep this moment" (note image), "In their words", kraft-paper "A note from Monika" image with two CTAs (Monika's story, Begin your bracelet), footer with large "Y JEWELRY" wordmark cropped at the bottom.

## Known open items
- Graduation tile uses a clover charm photo; Anniversary/Diwali/Birthday/New Beginnings use product photos supplied by the designer.
- "In their words" still has placeholder quotes/names; need real, consented ones.
- Only 5 of the 12 charms in "Twelve pieces I'd wear now" have photos; its scroll bar is static.
- Occasion tiles all link to `Gift.dc.html`.
- Product page (`Product.dc.html`) is white with one necklace photo in every photo slot (gallery, thumbs, menu cards, recommendations).
- Footer wordmark is set in Belwe Sans via SVG `textLength`, so letters are stretched to full width.
