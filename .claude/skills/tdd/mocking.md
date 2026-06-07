# When to Mock

Mock at **system boundaries** only:

- External APIs (payment, email, etc.)
- Databases (sometimes - prefer test DB like sqlite in-memory)
- Time/randomness
- File system (sometimes)

Don't mock:

- Your own classes/modules
- Internal collaborators
- Anything you control

## Designing for Mockability

At system boundaries, design interfaces that are easy to mock using `unittest.mock` or `pytest-mock`:

**1. Use dependency injection**

Pass external dependencies in rather than creating them internally:

```python
# Easy to mock
def process_payment(order: Order, payment_client: PaymentClient) -> Result:
    return payment_client.charge(order.total)

# Hard to mock
def process_payment(order: Order) -> Result:
    client = StripeClient(os.getenv("STRIPE_KEY"))
    return client.charge(order.total)
```

**2. Prefer SDK-style interfaces over generic fetchers**

Create specific functions for each external operation instead of one generic function with conditional logic:

```python
# GOOD: Each function is independently mockable
class ApiClient:
    def get_user(self, id: int) -> User:
        return httpx.get(f"/users/{id}").json()
        
    def get_orders(self, user_id: int) -> list[Order]:
        return httpx.get(f"/users/{user_id}/orders").json()

# BAD: Mocking requires conditional logic inside the mock
class ApiClient:
    def fetch(self, endpoint: str, options: dict) -> dict:
        return httpx.request(endpoint, **options).json()
```

The SDK approach means:
- Each mock returns one specific shape
- No conditional logic in test setup
- Easier to see which endpoints a test exercises
- Type safety per endpoint
