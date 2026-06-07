# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts. Use `pytest`.

```python
# GOOD: Tests observable behavior
async def test_user_can_checkout_with_valid_cart():
    cart = create_cart()
    cart.add(product)
    result = await checkout(cart, payment_method)
    assert result.status == "confirmed"
```

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```python
# BAD: Tests implementation details
async def test_checkout_calls_payment_service_process(mocker):
    mock_payment = mocker.patch.object(payment_service, 'process')
    await checkout(cart, payment)
    mock_payment.assert_called_with(cart.total)
```

Red flags:

- Mocking internal collaborators
- Testing private methods
- Asserting on call counts/order
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface

```python
# BAD: Bypasses interface to verify
async def test_create_user_saves_to_database(db_session):
    await create_user({"name": "Alice"})
    row = await db_session.execute("SELECT * FROM users WHERE name = 'Alice'")
    assert row.fetchone() is not None

# GOOD: Verifies through interface
async def test_create_user_makes_user_retrievable():
    user = await create_user({"name": "Alice"})
    retrieved = await get_user(user.id)
    assert retrieved.name == "Alice"
```
