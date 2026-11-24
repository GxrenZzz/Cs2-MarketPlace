# ADR 002 — Primary Key Strategy

## Status

Accepted

## Context

The CS2 marketplace requires unique identifiers for its entities.

The primary-key strategy must consider:

- Storage efficiency.
- Index size.
- Identifier predictability.
- API exposure.
- Independent identifier generation.

## Decision

The marketplace will use a combination of BIGINT and UUIDv4 primary keys.

### BIGINT

The following entities will use BIGINT primary keys:

- users
- base_items
- skins
- inventory_items
- listings
- wallets
- price_points

### UUIDv4

The following entities will use UUIDv4 primary keys:

- orders
- ledger_entries

## Rationale

### BIGINT

BIGINT requires 8 bytes, compared with 16 bytes for UUID.

It provides:

- Lower identifier storage overhead.
- Smaller primary-key and foreign-key values.
- Compact indexes.
- Convenient internal identification.

### UUIDv4

UUIDv4 provides:

- Randomly generated identifiers.
- Reduced risk of sequential identifier enumeration.
- Independent identifier generation across application servers.
- Less predictable identifiers when exposed through APIs.
- An extremely low probability of identifier collisions when generated correctly.

A cryptographically secure random number generator must be used for UUID generation.

### UUIDv4 Technical Details

UUIDv4 is a 128-bit identifier.

- 6 bits are reserved for version and variant information.
- The remaining 122 bits are randomly generated.
- The probability of generating two identical UUIDv4 identifiers is extremely low.

The unique constraint or primary-key index will still enforce uniqueness at the database level, protecting against duplicate identifiers if a collision occurs.

## Security Considerations

UUIDs are not a replacement for authentication or authorization.

The application must verify that users are authorized to access the requested resource, regardless of whether its identifier is a BIGINT or UUID.

## Consequences

### Positive

- Storage-efficient identifiers for most entities.
- Less predictable public identifiers for orders and ledger entries.
- Support for independent identifier generation.
- A clear distinction between internal and externally exposed identifiers.
- Extremely low probability of UUID collisions.

### Considerations

- UUIDs require more storage than BIGINT.
- UUIDs are less convenient to read and debug manually.
- Foreign keys referencing UUID primary keys must use the UUID data type.
- UUID unpredictability does not prevent unauthorized access by itself.
- Random UUID insertion can result in less sequential B-tree index access patterns compared with sequential identifiers.