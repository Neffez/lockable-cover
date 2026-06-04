"""Lockable Cover integration.

Wraps an existing cover entity and a lock entity (switch / input_boolean /
lock) in a proxy cover. While the lock entity is "on" (locked), movement
commands (open, close, set position, tilt) sent *to this proxy cover* are
blocked, whether they come from the UI, an automation or an app. Stop is
always allowed.

Note: this only guards commands targeting the proxy entity. Commands sent
directly to the underlying source cover bypass the lock.

Configured via the `cover:` platform in YAML, e.g.:

cover:
  - platform: lockable_cover
    covers:
      office:
        name: "Office"
        cover_entity: cover.office
        lock_entity: switch.office_lock
"""

DOMAIN = "lockable_cover"
