# Cover Lock

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

A small Home Assistant **custom integration** that adds a **lock** to a cover.

## What it does

`cover_lock` creates a proxy cover entity that mirrors an existing cover
(state, position, tilt, supported features) but **blocks all movement commands
while a lock entity is `on`** — no matter the source (UI, automation, app,
voice). `stop` is always allowed as a safety measure.

It pairs nicely with the companion
[Lockable Cover Card](https://github.com/neffez/lockable-cover-card), which
renders the open/stop/close controls plus a position slider and a lock toggle
directly on the card. The card also works standalone, but this integration is
what enforces the lock at the backend level.

## Installation

### HACS (recommended)

1. In Home Assistant go to **HACS → ⋮ → Custom repositories**.
2. Add `https://github.com/neffez/lockable-cover` with category
   **Integration**.
3. Install **Cover Lock**.
4. **Restart** Home Assistant (a full restart is required for a new platform —
   a reload is not enough).

### Manual

Copy the `custom_components/cover_lock` folder into your Home Assistant
`config/custom_components/` directory and restart.

## Configuration (YAML)

```yaml
# configuration.yaml
cover:
  - platform: cover_lock
    covers:
      office_lockable:
        name: "Office"
        cover_entity: cover.office_rollladen
        lock_entity: switch.office_beschattung_sperren   # switch / input_boolean / lock
        invert: true   # optional: lock entity is ON when *unlocked*
```

| Option | Required | Description |
|---|---|---|
| `cover_entity` | yes | The underlying cover to wrap. |
| `lock_entity` | yes | The entity used as the lock (switch / input_boolean / lock). |
| `name` | no | Friendly name for the proxy cover. |
| `invert` | no | `true` if the lock entity is `on` when *unlocked* (e.g. KNX shading-release group objects). Default `false` (on = locked). |

The config slug becomes the entity_id, so the example above creates
`cover.office_lockable` named "Office".

Extra attributes exposed on the proxy entity: `locked`, `lock_entity`,
`source_entity`.

## Companion card

[Lockable Cover Card](https://github.com/neffez/lockable-cover-card) renders a
native cover tile with a lock chip in the corner (and a tile-feature variant).
It auto-reads the `locked` / `lock_entity` attributes from this integration's
proxy entity.

## License

[MIT](./LICENSE)
