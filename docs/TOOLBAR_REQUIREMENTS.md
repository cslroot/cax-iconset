# CAX toolbar requirements, 2026-10-25

This bounded acceptance list covers all 18 requested groups and 46 individual meanings. It adds 44 glyphs and reuses 2 exact existing meanings. The 714-icon baseline remains byte-for-byte unchanged.

**Not consumer deployment:** Studio/viewer were inspected read-only. No imports, toolbar buttons or command handlers were modified. pdxadv, cnc-sim, cable-sim routes and BIM integration were not independently verified. This is not a claim of all-product GUI completeness.

## Binding precedence

Specific IDs in [toolbar-bindings.json](../toolbar-bindings.json) supersede generic menu-icon suggestions for these toolbar choices. Keep selected states, accessible names and tooltips; labels must not substitute for visually distinct button glyphs. Existing 180-row binding review and frozen audit remain historical source-scoped evidence.

## Acceptance checklist

| Group | Priority | Meanings | Dedicated new / exact reuse |
|---|---|---|---|
| 1 | high | Depth display; Hidden-line display; Shaded display; Shaded display with edges; Surface-normal display; Tessellation display; Wireframe display | 7 / 0 |
| 2 | high | Back view; Bottom view; Front view; Left view; Right view; Top view | 6 / 0 |
| 3 | high | Select edges only; Select vertices only | 2 / 0 |
| 4 | high | Create box primitive | 1 / 0 |
| 5 | high | Reset CAD work coordinates; Set CAD work coordinates | 2 / 0 |
| 6 | high | Assembly mates; Geometric constraints | 2 / 0 |
| 7 | high | Fly navigation; Turntable navigation | 2 / 0 |
| 8 | medium | Close sketch contour; Mirror sketch geometry; Scale sketch geometry | 3 / 0 |
| 9 | medium | Create lattice; Fill volume with lattice | 2 / 0 |
| 10 | medium | Make geometry editable; Set planar face distance; Stretch 3D region | 3 / 0 |
| 11 | medium | Make assembly from part | 0 / 1 |
| 12 | medium | Fasten two solids | 0 / 1 |
| 13 | medium | generic cable; minimum clearance; robot dresspack | 3 / 0 |
| 14 | medium | open sample | 1 / 0 |
| 15 | medium | Set face-normal condition; Toggle axis triad; Toggle navigation cube | 3 / 0 |
| 16 | low | Bloom glow; Matcap shading; Rendered reflections | 3 / 0 |
| 17 | low | BIM building; BIM space; BIM storey | 3 / 0 |
| 18 | low | generic report export | 1 / 0 |

## Important semantic checks

- Face distance edits geometry by moving a planar face to the requested separation, not measuring clearance.
- Fasten binds two solids as a fixed mate; it does not insert bolts or fuse solids. It reuses cad-fixed-joint.
- Release source enables independent editing while dropping source names, layers and drawings. Undo behavior remains the consumer responsibility.
- Face-normal condition uses a direction and minimumCosine threshold; it is separate from normal rendering.
- Edge and vertex filters restrict pick eligibility, not object visibility. Vertex is a requested complement, not a verified current Studio toolbar button.
- BIM glyphs denote spatial hierarchy objects. They do not assert implemented IFC import/export or object creation routes.

## Sources and per-meaning mapping

See [CSV](TOOLBAR_REQUIREMENTS.csv) and [binding JSON](../toolbar-bindings.json) for immutable commit/line URLs and source limitations.

## Validation

The regression suite pins every prior714 catalog record and both SVG variants, accounts for each new glyph, checks all18 groups, and requires distinct IDs and artwork for display modes, views, filters, navigation modes, gadget toggles and effects. Raster previews are native16/24/32px in both themes. These checks are not consumer browser or accessibility integration tests.
