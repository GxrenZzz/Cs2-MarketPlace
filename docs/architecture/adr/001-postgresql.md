# ADR 001 — PostgreSQL

## Status
Accepted

## Context

The CS2 marketplace requires a database system capable of maintaining relational integrity, enforcing business rules and handling concurrent operations safely.

The marketplace consists of nine entities:

1. users
2. base_items
3. skins
4. inventory_items
5. listings
6. orders
7. wallets
8. ledger_entries
9. price_points

Important business requirements include:

- Preventing duplicate purchases.
- Preventing negative wallet balances.
- Maintaining accurate ownership of inventory items.
- Preserving financial transaction history.
- Supporting concurrent purchases without double spending.
- Maintaining referential integrity between related entities.

## Decision

PostgreSQL will be used as the primary relational database management system (RDBMS) for the marketplace.

## Rationale

PostgreSQL provides the database capabilities required by the marketplace, including:

- Primary keys and foreign keys for referential integrity.
- CHECK, UNIQUE and other constraints for enforcing data integrity.
- Partial unique indexes for conditional uniqueness rules.
- Transactions and row-level locking for safe concurrent operations.
- Exact numeric data types for financial calculations.
- Indexing mechanisms for efficient data retrieval.

These capabilities allow important business rules to be enforced at the database level rather than relying exclusively on application logic.

## Consequences

### Positive

- Strong relational integrity.
- Reliable transactional operations.
- Database-level enforcement of many business rules.
- Support for concurrent marketplace operations.
- Flexible indexing and query optimization.

### Considerations

- Database transactions and locking must be implemented carefully.
- Complex integrity rules may require application logic, triggers or controlled database procedures.
- Indexes require maintenance and should be designed according to actual query patterns.
- Database performance must be monitored as the marketplace grows.

## Responsibility Separation

The marketplace will follow a separation of responsibilities between the application layer and the database layer.

### Database Layer

PostgreSQL is responsible for:

- Enforcing relational integrity.
- Enforcing database constraints and uniqueness rules.
- Maintaining transactional consistency.
- Supporting concurrency control.
- Protecting stored data from invalid states.

### Application Layer

The backend application is responsible for:

- Implementing marketplace business workflows.
- Handling authentication and authorization.
- Orchestrating listing and purchase operations.
- Initiating database transactions.
- Handling application-level validation and errors.

Both layers must work together to maintain the marketplace's business rules and data integrity.